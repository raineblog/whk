# WHK 仓库瘦身（Slim）操作手册

本文档完整记录 2026-10-12 对 `whk` 仓库执行的瘦身（slim）操作：动机、原理、每一步的确切命令、期望输出、验收标准、回滚方法与全部踩坑记录。写作目标是：**任何人在任何时间打开仓库，不依赖任何口头上下文，照本文即可完整复现、修复或回滚**。

所有命令均在 Windows + PowerShell 7（`pwsh`）下实际执行验证。本项目约定 Git 命令可加 `rtk` 前缀节省输出（如 `rtk git status`），本文为追求精确一律使用原生写法，加不加 `rtk` 不影响结果。

## 概述

### 背景

瘦身前的 `whk` 仓库存在严重的体积问题：

- `.git` 历史体积 **1.16 GiB**（packed 1.16 GiB，`.git` 目录 1273.7 MB），每次 clone / CI checkout / VPS 拉取都要传输全部分支的完整历史
- 而当前实际内容（工作区 `docs/` 目录）只有 **39.6 MB**
- 网站构建需要每个 `.md` 文件的 git 提交日期（日期计算依赖 git 历史），因此不能简单丢弃历史

### 目标与最终形态

保留 `.md` 文件的**全部 git 历史**（提交、作者、日期、提交信息逐条不变），其他文件只保留**当前版本的一个快照提交**，从此历史不再膨胀。

瘦身完成后的验收形态（以 2026-10-12 执行时为准，后续正常提交会使提交数自然增长）：

| 指标 | 瘦身前 | 瘦身后 |
| :--- | :--- | :--- |
| `main` 提交数 | 1548 | 909（908 个含 .md 改动的提交 + 1 个快照提交） |
| 跟踪文件数 | 1090 | 1090（217 个 `.md` + 873 个非 `.md`） |
| pack 体积 | 1.16 GiB | 44.13 MiB |
| `.md` 文件的最后修改日期 | 基线 | 与基线逐文件完全一致 |
| 非 `.md` 文件内容 | 旧版本 | 与旧 HEAD 逐字节一致（未改动任何仓库文件） |

### 适用范围

- **复现**：仓库再次变胖（例如回滚过、或历史被重新污染）时，从头执行「核心操作流程」
- **修复**：只出了局部问题（分支混乱、GitHub Desktop 提示 publish、本地体积回升等），直接查「踩坑速查表」对症处理
- **回滚**：随时可退回到瘦身前的胖仓库，见「回滚方案」

## 原理与关键决策

### 仓库为什么胖

对全部分支历史做对象统计（`git rev-list --objects --all`），blob 体积按顶层路径聚合如下：

| 路径 / 文件 | 历史 blob 合计 | blob 数 |
| :--- | :--- | :--- |
| `science/`（旧博客系统的根路径，HEAD 已不存在） | 1550.1 MB | 13178 |
| `docs/`（图片被反复提交的多个版本） | 638.3 MB | 5839 |
| `.smart-env/` | 118.1 MB | 580 |
| `cultural/`（旧根路径） | 72.3 MB | 1771 |
| `script/`（旧字体目录） | 68.7 MB | 99 |
| `assets/`（旧根路径） | 55.0 MB | 1353 |
| `feed_rss_created.xml`、`feed_rss_updated.xml` | 87.2 MB | 514 |
| `home/`（旧根路径） | 34.4 MB | 545 |
| `feed_json_created.json`、`feed_json_updated.json` | 66.6 MB | 352 |
| `pandoc-3.9.0.2-1-amd64.deb` | 32.4 MB | 1 |

关键结论：

- **`main` 分支本身并不跟踪 RSS feed 文件**（`git log -- feed_rss_created.xml` 在 main 上无任何记录）；它们只存在于 `gh-pages` 和 `backup/mkdocs-legacy` 分支
- 体积主体是「旧博客系统遗留路径 + 图片的反复提交版本 + gh-pages 分支的整站产物」
- 工作区中 `.venv`（400.2 MB）、`node_modules`（138.5 MB）是本地依赖，本就被 `.gitignore` 忽略，与 clone 慢无关

### 为什么必须保留 `.md` 历史

站点构建时按文件读取 git 提交日期（`git log -1 -- <file>`）来生成页面日期，因此：

- `.md` 的提交历史必须原样保留，日期才能与瘦身前一模一样
- 非 `.md` 文件（图片、脚本、配置）没有任何按日期的依赖，可以只要当前版本

### 过滤策略：按 commit 保留 `.md` 修改

使用 `git filter-repo --path-glob '*.md' --prune-empty always`：

- `--path-glob '*.md'`：逐个提交重放 diff，**只保留路径以 `.md` 结尾的改动**，同一提交里的图片 / 脚本修改直接丢弃
- `--prune-empty always`：过滤后变成空提交的提交（原本只改了非 `.md` 文件）自动删除，避免留下无意义的历史节点
- 默认重写**所有 ref**（本地分支、标签、远程跟踪引用），因此 `gh-pages`、`imgbot` 等分支在本地也会一起变瘦；远端在推送前不受影响

### CI：保持 `git add .` 不动

`.github/workflows/ci.yml` 构建末尾的 `git add .` 自动提交机制**必须保留原样，禁止修改**。图片压缩动作、描述生成脚本等构建产物依赖它做持久化记录。

2026-10-12 的教训：瘦身时曾一度把它改成 `git add -u -- '*.md'`，用户明确要求改回——脚本的记录功能优先于历史纯净度。

由此带来的已知行为（用户已确认接受）：CI 每次运行会把压缩后的图片等非 `.md` 产物提交回 `main`，因此非 `.md` 文件的历史会从瘦身后的下一个 CI 提交开始**缓慢重新累积**（每次只增量变化的部分）。`.md` 历史不受影响。

如果未来想两者兼得（既保留 `git add .` 的记录能力，又阻止纯生成物落库），正确做法是在 `.gitignore` 中排除具体生成物路径，**而不是改 `git add .`**。2026-10-12 时 main 并不跟踪 RSS feed 文件，暂无迫切需要排除的路径。

## 操作前准备

### 环境要求

- Windows + PowerShell 7
- 已安装 `git`、`uv`
- 仓库路径 `D:\Github\blog\whk`，远程 `git@github.com:raineblog/whk.git`

### 工具安装

```powershell
uv tool install git-filter-repo
```

期望输出包含 `git-filter-repo==2.47.0`（或更新版本）。

### 三重备份（缺一不可，先备份再动手）

1. **本地 mirror 全量克隆**（最完整的保险，包含所有分支的旧历史）：

```powershell
git clone --mirror . "D:\Github\blog\whk-backup-mirror.git"
```

2. **远程备份分支**：瘦身前先把当前 `main` 强制推送到 `origin/backup/blog-rebuilt`：

```powershell
git push origin main:backup/blog-rebuilt --force
```

3. **HEAD 文件快照**：用 `git checkout-index` 导出全部跟踪文件（1090 个）：

```powershell
$tmp = "C:\Users\PPR21\AppData\Local\Temp\kilo\whk-rewrite"
$snap = "$tmp\snapshot"
New-Item -ItemType Directory -Path $tmp, $snap -Force | Out-Null
git checkout-index -a -f --prefix="$snap\"
```

第三种备份的完整性判定：快照文件数必须等于 `git ls-files | Measure-Object -Line` 的行数（2026-10-12 时为 1090）。

> 注意：不要用 `git archive HEAD | tar -x` 做快照。Windows 自带 tar 处理中文文件名会报 `Invalid empty pathname` 并漏文件（实测漏 31 个中文名文件）。`git checkout-index` 由 git 内部处理编码，最可靠。

### 记录基线（日期验收的依据）

```powershell
git ls-files '*.md' | ForEach-Object { $d = & git log -1 --format=%ai -- "$_" 2>$null; "$_|$d" } | Set-Content "$tmp\baseline-md-dates.txt" -Encoding utf8
```

同时记录旧 HEAD 的 SHA（重写后做 tree 比对要用）：

```powershell
git rev-parse HEAD | Out-File "$tmp\old-sha.txt" -Encoding utf8
```

2026-10-12 的基线值：`.md` 文件 217 个，旧 SHA 为 `21bfafa199126abd34ce4b326e5eff6e20cbb2f0`。

## 核心操作流程

以下七步按顺序执行，每步都给出判定标准，不达标不要进入下一步。

### 第一步：执行历史重写

```powershell
git filter-repo --path-glob '*.md' --prune-empty always --force
```

命令要点：

- `--force`：filter-repo 默认拒绝在非 fresh clone 上运行，必须加
- 预计数秒完成，输出 `Parsed N commits` 与 `New history written`

执行后会发生三件事，全部在意料之中：

1. **`origin` 远程被删除**（filter-repo 的防误推设计），下一步立刻恢复
2. 所有远程跟踪引用被迁移为同名**本地分支**（`backup/blog-rebuilt`、`gh-pages`、`imgbot` 等），这些是重写后的 slim 影子分支，不是真实的远程状态，最后统一清理
3. 工作区被 reset 到新的 `.md`-only HEAD，非 `.md` 文件从磁盘消失（快照里有，别慌）

判定标准：

```powershell
git rev-list --count HEAD    # 期望 908（2026-10-12 实测）
git ls-files | Measure-Object -Line   # 期望 217（全部为 .md）
```

### 第二步：恢复 origin

```powershell
git remote add origin git@github.com:raineblog/whk.git
git remote -v
```

### 第三步：恢复非 `.md` 快照

> 若换了新的 PowerShell 会话，变量 `$tmp`、`$snap`、`$dst` 已丢失，先按「操作前准备 - 三重备份」中的定义重新声明再执行。

#### 3.1 复制非 `.md` 文件回工作区

```powershell
$dst = "D:\Github\blog\whk"
Get-ChildItem $snap -Recurse -File | Where-Object { $_.Extension -ne '.md' } | ForEach-Object {
    $rel = $_.FullName.Substring($snap.Length + 1)
    $target = Join-Path $dst $rel
    New-Item -ItemType Directory -Path (Split-Path $target -Parent) -Force | Out-Null
    Copy-Item -LiteralPath $_.FullName -Destination $target -Force
    $rel
} | Set-Content "$tmp\restore-list.txt" -Encoding utf8
```

> 必须用 `Copy-Item -LiteralPath`。位置参数形式的 `-Path` 会把文件名里的 `[1]` 当通配符，实测静默漏掉 `Construction_triangle_Reuleaux[1].svg` 和 `Reinhardt_15-gons[1].svg` 两个文件。

#### 3.2 增量校验，补齐漏网文件

```powershell
$missing = @()
Get-ChildItem $snap -Recurse -File | ForEach-Object {
    $rel = $_.FullName.Substring($snap.Length + 1)
    if (-not (Test-Path -LiteralPath (Join-Path $dst $rel))) { $missing += $rel }
}
if ($missing.Count -gt 0) {
    $missing | ForEach-Object {
        $target = Join-Path $dst $_
        New-Item -ItemType Directory -Path (Split-Path $target -Parent) -Force | Out-Null
        Copy-Item -LiteralPath (Join-Path $snap $_) -Destination $target -Force
    }
}
"仍缺失: $missing.Count 个（必须为 0）"
```

#### 3.3 暂存（只加清单内文件，用字面路径）

```powershell
(Get-Content "$tmp\restore-list.txt" -Encoding utf8) | ForEach-Object { ":(literal)" + ($_ -replace '\\','/') } | Set-Content "$tmp\restore-list-literal.txt" -Encoding utf8
git add -f --pathspec-from-file="$tmp\restore-list-literal.txt"
git diff --cached --name-only | Measure-Object -Line
```

判定标准：暂存数 = 873（2026-10-12 实测，即全部非 `.md` 文件）。

> `:(literal)` 前缀和正斜杠分隔符都不能省：文件名里的 `[1]` 会被 pathspec 通配符解释导致 `did not match any files`；反斜杠分隔符在字面路径模式下不匹配。`git add` 没有 `--literal-pathspecs` 选项，只能靠 `:(literal)`。
>
> `-f` 的作用是允许加入 `.gitignore` 覆盖但历史上被跟踪的文件（例如 `.kilo/` 下的部分文件）。因为显式列出了清单，`-f` 不会误伤未跟踪文件；切勿图省事用 `git add -A`，那会把 `.env`、`.kilo/`、`*.log` 等未跟踪文件一起提交进去。

### 第四步：提交快照

**不要修改 `.github/workflows/ci.yml`**（2026-10-12 用户明确要求保留 `git add .`，原因见「CI：保持 `git add .` 不动」）。直接提交快照：

```powershell
git commit -m "chore: 一次性合入非 Markdown 项目文件（无历史）"
```

判定标准：

```powershell
git rev-list --count HEAD                       # 期望 909
git ls-files | Measure-Object -Line             # 期望 1090
git count-objects -vH                           # size-pack 约 49 MiB
```

### 第五步：全面验证（三项全过才算成功）

#### 5.1 日期比对（`.md` 历史零损失的核心证据）

```powershell
git ls-files '*.md' | ForEach-Object { $d = & git log -1 --format=%ai -- "$_" 2>$null; "$_|$d" } | Set-Content "$tmp\new-md-dates.txt" -Encoding utf8
Compare-Object (Get-Content "$tmp\baseline-md-dates.txt" -Encoding utf8) (Get-Content "$tmp\new-md-dates.txt" -Encoding utf8)
```

判定标准：**无任何输出**（2026-10-12 实测 217 个文件全部一致）。

#### 5.2 文件树逐对象比对（`.md` 与非 `.md` 内容零损失）

```powershell
$oldSha = (Get-Content "$tmp\old-sha.txt" -Encoding utf8).Trim()
$new = (git ls-tree -r -z HEAD) -split "`0" | Where-Object { $_ }
$old = (git --git-dir="D:\Github\blog\whk-backup-mirror.git" ls-tree -r -z $oldSha) -split "`0" | Where-Object { $_ }
Compare-Object $new $old
```

判定标准：**1090 个文件的 mode、blob 哈希、路径全部一致**（不改 `ci.yml` 的情况下零差异；2026-10-12 首次执行时唯一差异是当时被误改的 `ci.yml`，已随后恢复）。

#### 5.3 残留清理

```powershell
git gc --prune=now
git count-objects -vH
```

判定标准：`garbage` 为 0，`size-pack` 约 44 MiB。

### 第六步：强制推送

```powershell
git push origin main --force
```

推送策略（2026-10-12 用户确认版）：**只推 `main`**。`origin/backup/blog-rebuilt` 等远端分支保持原样，作为胖历史备份继续存在。远端瘦身后的 `main` 形如 `998bd0c508bf421e2152cd818750a29016d369ef`（以实际推送结果为准）。

推送后验证：

```powershell
git ls-remote origin main refs/heads/backup/blog-rebuilt
```

判定标准：`refs/heads/main` 与本地 `git rev-parse main` 一致；`refs/heads/backup/blog-rebuilt` 仍为旧 SHA。

### 第七步：本地环境清理（拉直分支、修复 Desktop）

重写后本地会残留 6 个 slim 影子分支，可能还有一堆远程跟踪引用。**先把 fetch 收窄再同步，可以避免白白重新下载远端胖分支**。按顺序执行：

1. **收窄 fetch 范围**（放在第一步，防止后续任何 fetch 把远端所有胖分支拉回来）：

```powershell
git config remote.origin.fetch '+refs/heads/main:refs/remotes/origin/main'
```

2. **删除多余的远程跟踪引用**（`git remote prune origin` 删不动仍然存在于远端的分支，必须用 `-rd`；先用 `git branch -r` 看有哪些，提示 `not found` 的就是不存在，跳过即可）：

```powershell
git branch -r
git branch -rd origin/backup/blog-rebuilt origin/backup/mkdocs-legacy origin/gh-pages origin/imgbot origin/resize/update
```

3. **同步 main**（此时 fetch 只会拉 `main` 一个分支，体积很小）：

```powershell
git fetch origin main
git reset --hard origin/main
```

4. **删除 6 个重写残留的本地分支**（内容均可从远端重新派生，mirror 也有全量备份，删除无损失）：

```powershell
git branch -D backup/blog-rebuilt backup/mkdocs-legacy dependabot/uv/uv-0f75c6e56a gh-pages imgbot resize/update
```

5. **gc 清理**：

```powershell
git gc --prune=now
git count-objects -vH
```

6. **重设上游（关键，不设 GitHub Desktop 会要求 publish 且无法推送）**：

```powershell
git branch --set-upstream-to=origin/main main
git status -sb
git push
```

判定标准：`git status -sb` 显示 `## main...origin/main`；`git push` 输出 `Everything up-to-date`；`git branch -vv` 只剩 `* main`。

## 验收清单

全部通过则瘦身成功，可交付使用：

- [ ] `git rev-list --count HEAD` 为 909（含 1 个快照提交；之后正常提交会自然增长）
- [ ] `git ls-files | Measure-Object -Line` 为 1090（217 个 `.md` + 873 个非 `.md`）
- [ ] 第五步 5.1 日期比对无差异
- [ ] 第五步 5.2 tree 比对应无差异（未改 `ci.yml` 时）
- [ ] `git count-objects -vH` 的 `size-pack` 小于 50 MiB 且 `garbage` 为 0
- [ ] `git status -sb` 为 `## main...origin/main`，工作区 clean
- [ ] `git branch -vv` 只剩 `main`，且带 `[origin/main]` 跟踪信息
- [ ] `git push` 输出 `Everything up-to-date`
- [ ] 本地 mirror 备份 `D:\Github\blog\whk-backup-mirror.git` 存在且未被删
- [ ] 远端 `backup/blog-rebuilt` 仍指向旧 SHA（胖历史备份仍在）

## 回滚方案

回滚会把 `main` 恢复成瘦身前的胖仓库（约 1.16 GiB），仅在整个瘦身决策被推翻时使用。

方式一：直接按旧 SHA 推送（本地需拥有该对象，否则先 `git fetch origin backup/blog-rebuilt`，会重新下载约 1.16 GiB）：

```powershell
git push origin +21bfafa199126abd34ce4b326e5eff6e20cbb2f0:main --force
```

方式二：从本地 mirror 恢复：

```powershell
git clone "D:\Github\blog\whk-backup-mirror.git" "$env:TEMP\whk-restore"
git -C "$env:TEMP\whk-restore" remote set-url origin git@github.com:raineblog/whk.git
git -C "$env:TEMP\whk-restore" push origin main --force
```

回滚后若想重新瘦身，从「核心操作流程」第一步完整重做（备份步骤也请重做，旧基线已变化）。

## 踩坑速查表

| 症状 | 原因 | 处置 |
| :--- | :--- | :--- |
| `git archive \| tar` 报 `Invalid empty pathname`，快照缺文件 | Windows tar 处理中文文件名乱码 | 用 `git checkout-index -a -f --prefix=` 代替 |
| 复制后工作区缺 2 个文件，`Test-Path` 为 False | `Copy-Item` 位置参数 `-Path` 把 `[1]` 当通配符 | 一律 `Copy-Item -LiteralPath ... -Destination ...`，并在复制后跑一次 3.2 增量校验 |
| `git add` 报 `pathspec '...[1].svg' did not match any files` | `[` `]` 是 pathspec 通配符 | 清单每行加 `:(literal)` 前缀，并把 `\` 换成 `/` |
| `git add` 报 `unknown option 'literal-pathspecs'` | `git add` 没有这个选项 | 删掉该选项，只用 `:(literal)` 前缀 |
| `git checkout-index` 后 Compare-Object 报中文名不一致 | Unicode NFC/NFD 归一化差异，实际文件在位 | 以文件计数为准，最终以 5.2 的 blob 哈希比对为准 |
| filter-repo 后 `origin` 消失 | filter-repo 的设计行为 | 立即 `git remote add origin git@github.com:raineblog/whk.git` |
| filter-repo 后冒出一堆陌生本地分支 | 远程跟踪引用被迁移成本地分支 | 第七步统一 `git branch -D` 删除 |
| `git count-objects -vH` 的 garbage 持续增长、`git gc` 删不掉 | VS Code / Desktop 后台 `git fetch` 正在下载胖历史，临时文件被占用 | 先 `Get-CimInstance Win32_Process -Filter "Name='git.exe'"` 找到 `git fetch`、`git index-pack` 进程并 `Stop-Process -Id <pid> -Force`，再删 `.git/objects/pack/tmp_pack_*`，最后 `git gc --prune=now`；并用 `git config remote.origin.fetch` 收窄 refspec 根治 |
| `git remote prune origin` 后跟踪引用还在 | prune 只清理远端已删除的引用 | 用 `git branch -rd origin/<branch>` 直接删 |
| GitHub Desktop 提示 main 需要 publish、无法推送 | filter-repo 删 remote 导致 `branch.main.remote`、`branch.main.merge` 配置丢失 | `git branch --set-upstream-to=origin/main main`，然后在 Desktop 里 Fetch origin 一次刷新状态 |
| 本地体积莫名回到几百 MiB | 跑过 `git fetch origin main` 也会顺带下载其他分支（实测拉回 783 MiB），或后台自动 fetch 作祟 | 先收窄 refspec（`git config remote.origin.fetch '+refs/heads/main:refs/remotes/origin/main'`），删掉多余跟踪引用，再 `git gc --prune=now`；后台进程占用时先按上一行处置 |

## 日常维护与监控

1. **发现体积异常时先诊断**（勿直接动手）：

```powershell
git count-objects -vH
```

2. **定位大对象**（按体积排序取前 25 个）：

```powershell
git rev-list --objects --all | git cat-file --batch-check='%(objecttype) %(objectsize) %(objectname) %(rest)' | Select-String '^blob' | ForEach-Object { ($_ -split ' ')[1] + " " + ($_ -split ' ')[3] } | Sort-Object { [double]($_ -split ' ')[0] } -Descending | Select-Object -First 25
```

3. **定期校准 `.md` 日期基线**（建议每次怀疑日期异常时做，而非等出事）：

```powershell
git ls-files '*.md' | ForEach-Object { $d = & git log -1 --format=%ai -- "$_" 2>$null; "$_|$d" } | Set-Content "$tmp\current-md-dates.txt" -Encoding utf8
Compare-Object (Get-Content "$tmp\baseline-md-dates.txt" -Encoding utf8) (Get-Content "$tmp\current-md-dates.txt" -Encoding utf8)
```

新提交会改变少数文件的日期，这是正常现象；异常是指**大批量**日期丢失或回退。

4. **禁止事项（红线）**：

    - 禁止修改 `.github/workflows/ci.yml` 的 `git add .`（构建产物记录机制，2026-10-12 用户明确要求保留）
    - 禁止在本地运行 `mkdocs` / `mkpandocs` 的 `build` / `serve`（项目 AGENTS.md 规定），本文所有验证均通过 git 命令完成，无需构建
    - 禁止用 `git add -A` 或 `git add .` 恢复快照，会误提交 `.env`、`.kilo/`、`*.log`
    - 禁止删除远端 `backup/blog-rebuilt` 分支（它是用户指定的胖历史备份）和本地 `whk-backup-mirror.git`
    - 禁止在验证未全部通过前执行 force push

## 本次执行存档（2026-10-12）

| 项目 | 值 |
| :--- | :--- |
| 旧 `main` SHA | `21bfafa199126abd34ce4b326e5eff6e20cbb2f0`（1548 提交，1.16 GiB） |
| 新 `main` SHA | `998bd0c508bf421e2152cd818750a29016d369ef`（909 提交，44.13 MiB） |
| 本地 mirror 备份 | `D:\Github\blog\whk-backup-mirror.git` |
| 临时工作目录 | `C:\Users\PPR21\AppData\Local\Temp\kilo\whk-rewrite`（含 `baseline-md-dates.txt`、`old-sha.txt`、`snapshot\`、`restore-list.txt`） |
| 使用的工具 | `git-filter-repo 2.47.0`（`uv tool install`） |
| 有意修改的文件 | 无。曾误改 `.github/workflows/ci.yml`（`git add .` → `git add -u -- '*.md'`），当日即按用户要求恢复原样；该文件的 CI 记录机制禁止再动 |
| 远端保留的胖备份分支 | `backup/blog-rebuilt`（= 旧 SHA）、`backup/mkdocs-legacy`、`gh-pages`、`imgbot`、`resize/update` |
| 已知历史增长点 | CI 的 `git add .` 会持续提交图片压缩等产物；`google_indexing.json`（`seo-push.yml`，约 22.6 KB） |

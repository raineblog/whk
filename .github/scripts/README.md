# Lychee 链接检查工具配置和脚本

本目录包含用于处理 Lychee 链接检查结果的脚本和配置。

## 文件说明

### 配置文件

- **`lychee.toml`** (位于仓库根目录): Lychee 链接检查器的配置文件
    - 接受 403 状态码（忽略 Forbidden 错误）
    - 禁用 SSL 证书验证（忽略 SSL 证书错误）
    - 配置超时、重试、重定向等参数

### 脚本文件

#### 1. `process-lychee-report.py`

**自动运行** - 在 GitHub Actions workflow 中自动执行

**功能：**
- 清理 `.github/lychee.md` 报告文件，移除以下内容：
    - `[403]` 错误（Forbidden）
    - `[ERROR]` SSL 证书验证失败
    - `[200]` 已成功跟随的重定向
- 提取重定向映射并保存到 `redirects.txt`

**运行方式：**
```bash
# 自动运行（在 GitHub Actions 中）
python .github/scripts/process-lychee-report.py .github/lychee.md

# 手动运行
python .github/scripts/process-lychee-report.py [报告文件路径]
```

#### 2. `replace-redirects.py`

**手动运行** - 需要手动触发（修改文件内容，建议谨慎使用）

**功能：**
- 读取 `redirects.txt` 中的重定向映射
- 自动替换 `docs/` 目录下所有 Markdown 文件中的重定向链接为最终 URL
- 支持 Markdown 链接格式 `[text](url)` 和纯 URL

**运行方式：**
```bash
# 交互式运行（会要求确认）
python .github/scripts/replace-redirects.py

# 指定自定义路径
python .github/scripts/replace-redirects.py [映射文件路径] [文档目录路径]

# 非交互式运行（在 workflow 中）
python .github/scripts/replace-redirects.py .github/scripts/redirects.txt docs
```

**⚠️ 警告：** 此脚本会直接修改 Markdown 文件，建议：
1. 提交前先检查 `redirects.txt` 中的映射是否正确
2. 使用 Git 查看修改 (`git diff`)
3. 确认无误后再提交

## Workflow 集成

在 `.github/workflows/checker.yml` 中的集成流程：

```yaml
- name: Validate hyperlink integrity
  uses: lycheeverse/lychee-action@v2
  with:
    args: --config lychee.toml docs/**/*.md
    output: .github/lychee.md
    fail: false

- name: Process link checker report
  if: always()
  run: |
    python .github/scripts/process-lychee-report.py .github/lychee.md
  continue-on-error: true
```

## 生成的文件

- **`.github/lychee.md`**: Lychee 检查报告（自动清理后的版本）
- **`.github/scripts/redirects.txt`**: 检测到的重定向映射

## 使用场景

### 场景 1: 仅清理报告（默认）

当前配置已自动清理报告，无需额外操作。每次运行 workflow 后：
- 403 错误会被忽略
- SSL 证书错误会被忽略
- 成功的重定向会从报告中移除
- 重定向映射会保存到 `redirects.txt`

### 场景 2: 手动替换重定向链接

如果你想将重定向链接替换为最终 URL：

1. 等待 workflow 运行完成
2. 检查 `.github/scripts/redirects.txt` 中的映射
3. 本地运行替换脚本：
   ```bash
   python .github/scripts/replace-redirects.py
   ```
4. 检查修改：`git diff`
5. 确认无误后提交

### 场景 3: 在 Workflow 中自动替换（可选）

如果你想在 workflow 中自动替换，可以在 `checker.yml` 中添加：

```yaml
- name: Process link checker report
  if: always()
  run: |
    python .github/scripts/process-lychee-report.py .github/lychee.md
  continue-on-error: true

# 添加这一步
- name: Replace redirected links (optional)
  if: always()
  run: |
    python .github/scripts/replace-redirects.py .github/scripts/redirects.txt docs
  continue-on-error: true
```

## 配置说明

### 忽略特定链接

如果需要忽略特定链接，编辑 `.lycheeignore` 文件：

```
https://example.com/some-problematic-url
```

### 调整接受的状态码

编辑 `lychee.toml` 中的 `accept` 参数：

```toml
accept = [200, 201, 202, 203, 204, 206, 300, 301, 302, 303, 304, 307, 308, 403, 429]
```

### 禁用/启用 SSL 验证

编辑 `lychee.toml`：

```toml
# 禁用 SSL 验证（忽略证书错误）
insecure = true

# 启用 SSL 验证（严格检查证书）
insecure = false
```

## 故障排查

### 问题：脚本运行失败

**解决方案：**
- 检查 Python 是否安装（需要 Python 3.7+）
- 检查文件路径是否正确
- 查看 workflow 日志获取详细错误信息

### 问题：重定向映射不正确

**解决方案：**
- 检查 `.github/scripts/redirects.txt`
- 手动编辑或删除不正确的映射
- 重新运行处理脚本

### 问题：某些链接仍然报错

**解决方案：**
1. 检查 `lychee.toml` 中的 `accept` 配置
2. 将问题链接添加到 `.lycheeignore`
3. 调整 `timeout` 或 `max_retries` 参数

## 参考资料

- [Lychee 官方文档](https://github.com/lycheeverse/lychee)
- [Lychee Action 文档](https://github.com/lycheeverse/lychee-action)

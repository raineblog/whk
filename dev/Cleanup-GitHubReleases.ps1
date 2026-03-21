# 强制开启 UTF8 支持
$OutputEncoding = [Console]::OutputEncoding = [System.Text.Encoding]::UTF8

Write-Host "======================================================" -ForegroundColor Cyan
Write-Host "   GitHub Release 终极清理工具 (多线程版)" -ForegroundColor Cyan
Write-Host "======================================================" -ForegroundColor Cyan

# 1. 环境检查
if (!(Get-Command gh -ErrorAction SilentlyContinue)) {
    Write-Host "[错误] 未找到 gh CLI，请先安装: https://cli.github.com/" -ForegroundColor Red
    return
}

# 2. 引导用户输入天数
Write-Host "建议选项: [0] 全部, [1] 一天前, [7] 一周前, [30] 一个月前, [365] 一年前" -ForegroundColor Gray
$daysInput = Read-Host "请输入要删除多少天前的 Release"

if ($daysInput -eq "0") {
    $cutoffDate = (Get-Date).AddDays(1)
} elseif ($daysInput -match "^\d+$") {
    $cutoffDate = (Get-Date).AddDays(-[int]$daysInput)
} else {
    Write-Host "[错误] 输入无效。" -ForegroundColor Red; return
}

# 3. 获取列表
Write-Host "[读取] 正在扫描 GitHub 远程数据..." -ForegroundColor Cyan
$releases = gh release list --limit 1000 --json tagName,createdAt | ConvertFrom-Json
$targets = $releases | Where-Object { $_.tagName -notlike 'v*' -and ([DateTime]$_.createdAt -lt $cutoffDate) }

if ($null -eq $targets -or $targets.Count -eq 0) {
    Write-Host "[结果] 没有发现符合条件的项目。" -ForegroundColor Green
    return
}

# 4. 显示列表
Write-Host "`n待处理列表:" -ForegroundColor White
$targets | ForEach-Object { Write-Host " - $($_.tagName)" -ForegroundColor Gray }
$total = $targets.Count
Write-Host "`n共计: $total 个项目" -ForegroundColor Yellow

# 5. 三重确认 (y -> n -> y)
if ((Read-Host "[确认 1/3] 是否确认删除上述项目? (y)") -ne "y") { Write-Host "已退出"; return }
if ((Read-Host "[确认 2/3] 您确定【不】取消操作吗? (n)") -ne "n") { Write-Host "已退出"; return }
Write-Host "!!! 终极警告：此操作将永久抹除远程 Release 和 Tag !!!" -BackgroundColor DarkRed -ForegroundColor White
if ((Read-Host "[确认 3/3] 确认执行? (y)") -ne "y") { Write-Host "已退出"; return }

# 6. 开始并行删除
Write-Host "`n[开始] 启动加速引擎，并行执行中..." -ForegroundColor Cyan

# 初始化计数器（用于跨线程计算进度）
$counter = [hashtable]::Synchronized(@{ Current = 0 })

# 检查是否支持并行执行 (PowerShell 7+)
$useParallel = $PSVersionTable.PSVersion.Major -ge 7

if ($useParallel) {
    # 多线程加速模式
    $targets | ForEach-Object -Parallel {
        $tag = $_.tagName
        $sync = $using:counter
        $totalCount = $using:total
        $success = $false
        $attempts = 0

        while (-not $success -and $attempts -lt 5) {
            $attempts++
            gh release delete $tag --cleanup-tag --yes 2>$null
            if ($LASTEXITCODE -eq 0) {
                $success = $true
            } else {
                Start-Sleep -Seconds (1 * $attempts) # 失败后退避
            }
        }

        # 更新进度
        $sync.Current++
        $percent = [math]::Round(($sync.Current / $totalCount) * 100, 1)
        
        if ($success) {
            Write-Host "[$percent%] [成功] $tag (尝试 $attempts 次)" -ForegroundColor Green
        } else {
            Write-Host "[$percent%] [失败] $tag (已重试 5 次)" -ForegroundColor Red
        }
    } -ThrottleLimit 5 # 同时运行 5 个任务
} else {
    # 兼容模式 (旧版 PowerShell)
    Write-Host "[提示] 当前环境不支持并行，改用顺序模式..." -ForegroundColor Yellow
    foreach ($item in $targets) {
        $tag = $item.tagName
        $counter.Current++
        $success = $false
        $attempts = 0
        while (-not $success -and $attempts -lt 5) {
            $attempts++
            gh release delete $tag --cleanup-tag --yes 2>$null
            if ($LASTEXITCODE -eq 0) { $success = $true }
        }
        $percent = [math]::Round(($counter.Current / $total) * 100, 1)
        Write-Host "[$percent%] 处理: $tag"
    }
}

Write-Host "`n======================================================" -ForegroundColor Cyan
Write-Host "   清理完成！进度: 100% " -ForegroundColor Green
Write-Host "======================================================" -ForegroundColor Cyan
pause
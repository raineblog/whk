# 删除 raineblog-whk 的所有部署，只保留当前最新的 Production 部署
# 自动循环直到删完

$round = 0
while ($true) {
    $round++
    Write-Host "`n===== 第 $round 轮 =====" -ForegroundColor Magenta

    # 获取部署列表
    $response = bunx wrangler pages deployment list --project-name raineblog-whk --json 2>&1
    if ($LASTEXITCODE -ne 0) {
        Write-Error "获取部署列表失败: $response"
        exit 1
    }

    try {
        $deployments = $response | ConvertFrom-Json
    } catch {
        Write-Error "解析部署列表失败: $_"
        exit 1
    }

    if ($deployments.Count -eq 0) {
        Write-Host "没有部署了，完成！" -ForegroundColor Green
        break
    }

    # 找出最新的 Production 部署（保留它）
    $latestProd = $deployments | Where-Object { $_.Environment -eq "Production" } | Select-Object -First 1
    $keepId = if ($latestProd) { $latestProd.Id } else { "" }

    # 找出所有需要删除的
    $toDelete = $deployments | Where-Object { $_.Id -ne $keepId }

    if ($toDelete.Count -eq 0) {
        Write-Host "完成！保留了 Production 部署: $keepId" -ForegroundColor Green
        break
    }

    Write-Host "本轮删除 $($toDelete.Count) 个部署（保留: $keepId）" -ForegroundColor Yellow

    foreach ($d in $toDelete) {
        $id = $d.Id
        Write-Host "  删除: $id [$($d.Environment)]"

        $output = bunx wrangler pages deployment delete "$id" --project-name raineblog-whk --force 2>&1

        if ($output -match "Successfully deleted") {
            Write-Host "    ✓ 已删除" -ForegroundColor Green
        } elseif ($output -match "active production deployment") {
            Write-Host "    ⚠ 跳过活跃的 Production 部署" -ForegroundColor Cyan
        } else {
            Write-Warning "    未知情况: $output"
        }
    }
}

Write-Host "`n所有操作完成！" -ForegroundColor Green

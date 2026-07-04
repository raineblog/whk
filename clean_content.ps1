<#
.SYNOPSIS
深度清理 Markdown：删除不可见字符、精准修正乱码/异体字、规范全角英文、保留中文标点、统一换行符
#>

$targetDir = "docs"

if (-not (Test-Path $targetDir)) {
    Write-Host "错误: 找不到文件夹 '$targetDir'！" -ForegroundColor Red
    exit
}

# 1. 不可见字符、乱码占位符正则
$badCharsRegex = '[\x00-\x08\x0B\x0C\x0E-\x1F\x7F\uFFFD\u200B-\u200F\u2028-\u202F\u2060-\u206F\uFEFF]'

# 2. 自定义标点规范化字典 (可按需修改)
$punctuationRules = [ordered]@{
    '，，+'  = '，'           # 多个中文逗号合并
    '。。+'  = '。'           # 多个中文句号合并
}

$files = Get-ChildItem -Path $targetDir -Filter "*.md" -Recurse -File
$utf8NoBom = New-Object System.Text.UTF8Encoding $false
$processedCount = 0

foreach ($file in $files) {
    Write-Host "正在处理: $($file.FullName)" -ForegroundColor Cyan
    
    # 读取文件
    $content = [System.IO.File]::ReadAllText($file.FullName)
    
    # 步骤一：清理不可见字符和乱码 (\uFFFD)
    $content = [regex]::Replace($content, $badCharsRegex, '')
    
    # 步骤二：外科手术级字符规范 (解决中文逗号被误伤的问题)
    
    # 2.1 精准转换：全角英文字母、数字 -> 半角 (ASCII)
    # 利用 Unicode 编码偏移量：全角字符比半角字符的编码恰好大 0xFEE0 (65248)
    $content = [regex]::Replace($content, '[０-９Ａ-Ｚａ-ｚ]', {
        param($match)
        return [char]([int][char]$match.Value - 0xFEE0)
    })
    
    # 2.2 精准修复：CJK兼容表意文字 (U+F900-U+FAFF 区间的奇葩异体字/Big5乱象)
    # 仅对这些异体字应用 NFKC 规范，使其变成标准简体/繁体中文
    $content = [regex]::Replace($content, '[\uF900-\uFAFF]', {
        param($match)
        return $match.Value.Normalize([System.Text.NormalizationForm]::FormKC)
    })
    
    # 2.3 全局应用温和的 NFC 规范 (合并音调符号，绝对不会破坏中文标点)
    $content = $content.Normalize([System.Text.NormalizationForm]::FormC)
    
    # 步骤三：自定义标点和正则规范替换
    foreach ($rule in $punctuationRules.GetEnumerator()) {
        $content = [regex]::Replace($content, $rule.Name, $rule.Value)
    }
    
    # 步骤四：统一换行符为 \n (LF)
    $content = $content -replace "`r`n", "`n"
    $content = $content -replace "`r", "`n"
    
    # 覆盖写入文件
    [System.IO.File]::WriteAllText($file.FullName, $content, $utf8NoBom)
    
    $processedCount++
}

Write-Host "`n完美！共深度清理了 $processedCount 个 .md 文件。" -ForegroundColor Green
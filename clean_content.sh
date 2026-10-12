#!/usr/bin/env bash

# 目标文件夹路径
TARGET_DIR="docs"

# 检查文件夹是否存在
if [ ! -d "$TARGET_DIR" ]; then
    echo -e "\033[31m错误: 找不到文件夹 '$TARGET_DIR'！请确保在正确的目录下运行此脚本。\033[0m"
    exit 1
fi

# 定义内嵌的 Perl 处理逻辑
# 这里完美复刻了 PowerShell 版本的所有细节
PERL_SCRIPT='
use utf8;
use Encode qw(decode encode);
use Unicode::Normalize;

# 开启 slurp 模式，一次性读取整个文件（为了能处理跨行的 \r\n）
undef $/; 
my $content = <>;
$content = decode("UTF-8", $content);

# 步骤一：清理不可见字符和乱码 (\x{FFFD})
$content =~ s/[\x{00}-\x{08}\x{0B}\x{0C}\x{0E}-\x{1F}\x{7F}\x{FFFD}\x{200B}-\x{200F}\x{2028}-\x{202F}\x{2060}-\x{206F}\x{FEFF}]//g;

# 步骤二：外科手术级字符规范
# 2.1 精准转换：全角英文字母、数字 -> 半角 (利用 Unicode 偏移量 0xFEE0)
$content =~ s/([０-９Ａ-Ｚａ-ｚ])/chr(ord($1) - 0xFEE0)/ge;

# 2.2 精准修复：CJK兼容表意文字 (U+F900-U+FAFF 区间) 应用 NFKC 规范
$content =~ s/([\x{F900}-\x{FAFF}])/NFKC($1)/ge;

# 2.3 全局应用温和的 NFC 规范 (合并音调符号，不破坏中文标点)
$content = NFC($content);

# 步骤三：自定义标点和正则规范替换
$content =~ s/，{2,}/，/g;  # 多个中文逗号合并
$content =~ s/。{2,}/。/g;  # 多个中文句号合并

# 步骤四：统一换行符为 \n (LF)
$content =~ s/\r\n/\n/g;
$content =~ s/\r/\n/g;

# 原路输出（写回 UTF-8，无 BOM）
print encode("UTF-8", $content);
'

count=0

# 使用 find 查找所有 .md 文件 (-print0 防止文件名中有空格)
echo "开始扫描 '$TARGET_DIR' 文件夹..."

while IFS= read -r -d '' file; do
    echo -e "\033[36m正在处理: $file\033[0m"
    
    # 使用 perl 原地修改 (-i) 文件
    perl -i -e "$PERL_SCRIPT" "$file"
    
    ((count++))
done < <(find "$TARGET_DIR" -type f -name "*.md" -print0)

echo -e "\n\033[32m完美！共深度清理了 $count 个 .md 文件。\033[0m"
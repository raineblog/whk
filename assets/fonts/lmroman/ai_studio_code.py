import os
from fontTools.ttLib import TTFont

# 目标转换格式
TARGET_EXT = '.woff2'

def convert_to_woff2():
    # 获取当前目录下所有文件
    files = [f for f in os.listdir('.') if f.endswith('.otf')]
    
    if not files:
        print("未找到 .otf 文件！请确保脚本放在字体文件夹内。")
        return

    print(f"找到 {len(files)} 个字体文件，开始转换...")
    
    for filename in files:
        name_without_ext = os.path.splitext(filename)[0]
        output_name = name_without_ext + TARGET_EXT
        
        # 如果目标文件已存在，跳过
        if os.path.exists(output_name):
            print(f"[跳过] {output_name} 已存在")
            continue
            
        try:
            # 加载字体
            font = TTFont(filename)
            # 另存为 woff2
            font.flavor = 'woff2'
            font.save(output_name)
            print(f"[成功] {filename} -> {output_name}")
        except Exception as e:
            print(f"[失败] {filename}: {e}")

    print("\n所有转换完成！")

if __name__ == '__main__':
    convert_to_woff2()
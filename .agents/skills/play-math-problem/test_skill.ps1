# test_skill.ps1
# 测试 play-math-problem skill 脚本

$env:POE_API_KEY = "test_api_key_for_validation"
cd .agents/skills/play-math-problem

Write-Host "=== 测试 1: 列出模型 ==="
.venv/Scripts/python.exe generate_answer.py --list-models

Write-Host "`n=== 测试 2: 检查语法 ==="
.venv/Scripts/python.exe -m py_compile generate_answer.py
Write-Host "语法检查通过"

Write-Host "`n=== 测试 3: 模板渲染 ==="
.venv/Scripts/python.exe -c "
from pathlib import Path
from generate_answer import render_prompt, load_default_exploration

# 测试模板加载
template_dir = Path('.')
exploration = load_default_exploration(template_dir)
print(f'探索模板加载: {len(exploration)} 字符')

# 测试提示词渲染
prompt = render_prompt('求函数 f(x) = x^2 的极值', exploration)
print(f'提示词渲染: {len(prompt)} 字符')
print('提示词渲染成功!')
"

Write-Host "`n=== 测试 4: 验证 API 调用（会失败因为是虚假 key）==="
.venv/Scripts/python.exe generate_answer.py -p "1+1" 2>&1 | Select-Object -First 5

Write-Host "`n所有基础测试完成!"

generate:
	python script/generate.py

serve:
	python script/generate.py
	zensical serve

build:
	python script/generate.py
	mkdocs build --strict --clean
	python -c "import shutil; shutil.copytree('public', 'site', dirs_exist_ok=True)"

pull:
	git submodule update --remote

generate:
	python script/generate.py

serve:
	python script/generate.py
	zensical serve

build:
	python script/generate.py
	mkdocs build --strict --clean
	touch site/.nojekyll

pull:
	git submodule update --remote

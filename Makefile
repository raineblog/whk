generate:
	python script/generate.py

serve:
	python script/generate.py
	mkdocs serve --livereload --dirty

build:
	python script/generate.py
	mkdocs build --strict --clean
	touch site/.nojekyll

export2pdf:
	python script/generate.py
	mkdocs build --strict --clean
	python script/export.py

pull:
	git submodule update --remote

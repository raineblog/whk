generate:
	python script/generate.py

serve:
	python script/generate.py
	mkdocs serve --livereload --dirty

build:
	python script/generate.py
	mkdocs build --strict
	touch site/.nojekyll

export2pdf:
	python script/export.py

pull:
	git submodule update --remote

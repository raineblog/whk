mkdocs.yml:
	uv run script/generate.py

serve: mkdocs.yml
	mkdocs serve --livereload --dirty

build: mkdocs.yml
	mkdocs build --strict

export2pdf:
	python script/export.py

pull:
	git submodule update --remote

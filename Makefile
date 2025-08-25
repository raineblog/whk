serve: mkdocs.yml
	mkdocs serve --dirty

build: mkdocs.yml
	git rev-parse --short HEAD | xargs -I % sed -i "s/githash: ''/githash: '%'/g" mkdocs.yml
	mkdocs build --strict

mkdocs.yml: info.json
	python script/generate_mkdocs_yml.py

export:
	typst -V
	export TYPST_FONT_PATHS="./script/fonts"
	python ./script/export.py

update:
	git submodule update --remote

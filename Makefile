serve: mkdocs.yml
	mkdocs serve --livereload --dirty

build: mkdocs.yml
	git rev-parse --short HEAD | xargs -I % sed -i "s/githash: ''/githash: '%'/g" mkdocs.yml
	mkdocs build --strict

mkdocs.yml: info.json
	python script/generate_mkdocs_yml.py

toc: info.json
	python script/toc.py

update:
	git submodule update --remote

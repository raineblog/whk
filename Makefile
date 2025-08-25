serve: mkdocs.yml
	mkdocs serve --dirty

build: mkdocs.yml
	git rev-parse --short HEAD | xargs -I % sed -i "s/githash: ''/githash: '%'/g" mkdocs.yml
	mkdocs build --strict

toc: info.json
	python script/toc.py

mkdocs.yml: info.json
	python script/generate_mkdocs_yml.py

update:
	git submodule update --remote

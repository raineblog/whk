serve:
	docker run --rm -it --init -p 8000:8000 -v $(CURDIR):/app/workspace -w /app/workspace ghcr.io/raineblog/mkdocs-docker:latest mkdocs-serve

build:
	docker run --rm -v $(CURDIR):/app/workspace -w /app/workspace ghcr.io/raineblog/mkdocs-docker:latest mkdocs-build

pull:
	git submodule update --remote

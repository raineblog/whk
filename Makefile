
.PHONY: serve build lint pull

IMAGE := ghcr.io/raineblog/mkdocs-docker:latest

serve:
	docker run --rm -it --init -p 8000:8000 \
		-v $(CURDIR):/app/workspace -w /app/workspace \
		$(IMAGE) mkdocs-serve

build:
	docker run --rm \
		-v $(CURDIR):/app/workspace -w /app/workspace \
		$(IMAGE) mkdocs-build

lint:
	docker run --rm \
		-v $(CURDIR):/app/workspace -w /app/workspace \
		$(IMAGE) mkdocs-lint

pull:
	docker pull $(IMAGE)

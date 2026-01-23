IMAGE := ghcr.io/raineblog/mkdocs-docker:latest

serve:
	docker run --rm -it -p 8000:8000 \
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

sub-update:
	git submodule update --remote --init --recursive

sub-sync:
	git submodule sync --recursive
	git submodule update --init --recursive

DOCKER_LOCAL_AUTOBLOG = docker run --rm -it \
	-v $(CURDIR):/app/workspace \
	-w /app/workspace \
	--env-file .env \
	mkdocs-autoblog:latest

autoblog:
	$(DOCKER_LOCAL_AUTOBLOG)

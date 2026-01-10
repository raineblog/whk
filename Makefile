generate:
	python script/generate.py

serve:
	python script/generate.py
	zensical serve

build:
	python script/generate.py
	mkdocs build --strict --clean
	@if [ "$(OS)" = "Windows_NT" ]; then \
		if [ -d "public" ]; then \
			xcopy /E /I /Y public site >nul 2>&1 || robocopy public site /E /IS /NP >nul 2>&1 || true; \
		fi; \
	else \
		if [ -d "public" ]; then \
			cp -r public/* site/ 2>/dev/null || true; \
		fi; \
	fi

pull:
	git submodule update --remote

# whk

```
git submodule add https://github.com/raineblog/mkdocs-material material
git submodule add https://github.com/raineblog/mkdocs-script script
git submodule add https://github.com/raineblog/intro docs/intro/
git submodule update --remote


check:
name: Check
runs-on: ubuntu-latest
steps:
    - name: Checkout main
    uses: actions/checkout@v4
    - name: Config Git
    run: |
        git config user.name github-actions[bot]
        git config user.email 41898282+github-actions[bot]@users.noreply.github.com
    - name: Update Submodule
    run: |
        git submodule sync
        git submodule update --init --recursive
        git submodule update --remote
        if [[ `git status --porcelain` ]]; then
        git add .
        git commit -m "Update Submodule"
        git push
        else
        echo pass
        fi
```

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

```html
.{.{ read_csv('path_to_table.csv') }.}.
<details>
<summary>点击查看代码</summary>

</details>

???+ warning
    请记得在文本前面添加 4 个空格。其他的语法还是与 Markdown 语法一致。

    不添加 4 个空格的话，文本就不会出现在 Details 文本框里了。

    这个 `???` 是什么的问题会在下文解答。

???+ note
    阿斯蒂
    阿斯蒂芬

??? note "点击查看代码"

## 外部链接[^note1]

## 参考资料与注释

[^note1]: （冒号）表示总结上文。


### My Great Heading {#custom-id}

[Heading IDs](#heading-ids)	

- [x] Write the press release
- [ ] Update the website
- [ ] Contact the media

I need to highlight these ==very important words==.

In a hole in the ground there lived a hobbit. Not a nasty, dirty, wet hole, filled with the ends
of worms and an oozy smell, nor yet a dry, bare, sandy hole with nothing in it to sit down on or to
eat: it was a [hobbit-hole][1], and that means comfort.

[1]: <https://en.wikipedia.org/wiki/Hobbit#Lifestyle> "Hobbit lifestyles"



```

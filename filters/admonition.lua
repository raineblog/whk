function CodeBlock(el)
    -- 1. 检查语言是否为 md 或 markdown
    if el.classes:includes('md') or el.classes:includes('markdown') then
        
        -- 2. 获取 admonition 属性（得益于标准的 key="value" 写法，这里现在绝对稳定）
        local admonition_type = el.attributes['admonition']
        
        if admonition_type then
            
            -- 获取 title 属性
            local title_raw = el.attributes['title']
            
            -- 【细节优化】如果是 details 且没有传 title，默认给一个 "Details"
            if admonition_type == "details" and not title_raw then
                title_raw = "Details"
            else
                title_raw = title_raw or "Admonition"
            end

            -- 3. 将 title 作为 Markdown 重新解析（支持行内公式等）
            local title_doc = pandoc.read(title_raw, "markdown")
            local title_inlines = pandoc.List()
            if #title_doc.blocks > 0 and title_doc.blocks[1].content then
                title_inlines = title_doc.blocks[1].content

                
            end

            local title_doc = pandoc.read(title_raw, "markdown")
            local title_blocks = title_doc.blocks

            -- 第二个参数 {pandoc.Space()} 是块与块之间的分隔符
            -- 它会自动遍历所有 block 并提取它们的 inline 内容
            local title_inlines = pandoc.utils.blocks_to_inlines(title_blocks, {pandoc.Space()})

            -- 4. 将代码块内的文本同样作为 Markdown 重新解析
            local content_doc = pandoc.read(el.text, "markdown")
            local content_blocks = content_doc.blocks

            -- ==========================================
            -- 分支 A：处理 admonition="details" (折叠块)
            -- ==========================================
            if admonition_type == "details" then
                
                -- 构造 <summary>...</summary> 的行内元素
                local summary_inlines = pandoc.List()
                summary_inlines:insert(pandoc.RawInline("html", "<summary>"))
                summary_inlines:extend(title_inlines)
                summary_inlines:insert(pandoc.RawInline("html", "</summary>"))
                
                -- 放入纯文本段落中，防止被包进多余的 <p>
                local summary_p = pandoc.Plain(summary_inlines)

                -- 组装默认收缩的 <details> 区块
                local final_blocks = pandoc.List()
                final_blocks:insert(pandoc.RawBlock('html', '<details>'))
                final_blocks:insert(summary_p)
                final_blocks:extend(content_blocks)
                final_blocks:insert(pandoc.RawBlock('html', '</details>'))

                -- 返回包裹好的 Div
                return pandoc.Div(final_blocks, pandoc.Attr("", {"details-wrapper"}))

            -- ==========================================
            -- 分支 B：处理常规 admonition (note, warning 等)
            -- ==========================================
            else
                -- 构造 <p class="admonition-title">...</p>
                local p_start = pandoc.RawInline("html", '<p class="admonition-title">')
                local p_end   = pandoc.RawInline("html", '</p>')
                
                local p_content = pandoc.List({p_start})
                p_content:extend(title_inlines)
                p_content:insert(p_end)

                -- 必须使用 Plain (纯文本块)
                local title_p = pandoc.Plain(p_content)

                -- 组装 admonition 区块
                local final_blocks = pandoc.List({title_p})
                final_blocks:extend(content_blocks)

                -- 返回 <div class="admonition {type}">...</div>
                return pandoc.Div(final_blocks, pandoc.Attr("", {"admonition", admonition_type}))
            end
        end
    end
    
    -- 如果不是目标代码块，原样返回
    return nil
end
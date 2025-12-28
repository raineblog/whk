#import "@preview/min-book:1.2.0": book

#let sans = ("Noto Sans", "Noto Sans CJK SC", "Noto Sans SC")
#let serif = ("New Computer Modern", "Noto Serif CJK SC", "Noto Serif SC")

#set text(font: serif, lang: "zh", region: "CN")

#let book-data = json("toc.json")

#show: book.with(
  title: text(font: serif, book-data.title),
  subtitle: text(font: serif, book-data.subtitle),
  authors: book-data.authors.join(", "),
  date: datetime.today(),
  cover: auto,
  titlepage: auto,
  // catalog: none,
  // errata: "暂时没有纠错内容",
  dedication: "献给佐倉杏子",
  acknowledgements: [
    #align(center)[
      #text(weight: "bold", size: 2em)[本书简介]
    ]
    
    #for paragraph in book-data.info.abstract [
      #paragraph
    
    ]
    
    #align(center + bottom)[
      #book-data.info.publishing
    ]
  ],
  // epigraph: "右下角斜体",
  toc: true,
  part: "Chapter",
  chapter: "Detail",
  cfg: (
    numbering: (
      "{1:1}\n",
      "{1:1}.{2}.",
    ),
    page: "a4",
    lang: "zh",
    justify: true,
    line-space: 0.75em,
    line-indentfirst: 2em,
    par-margin: 1.25em,
    margin: (x: 15.142857142857144%, y: 8.552188552188552%),
    font-usedefaults: true,
    cover-back: true,
    toc-stdindent: true,
    toc-bold: true,
    chapter-numrestart: true,
    two-sided: false,
    paper-links: true,
  ),
)

#set page(footer: none)

#for chapter in book-data.content [
  #heading(level: 1, outlined: true)[
    #chapter.title
  ]
  #for section in chapter.sections [
    #set page(margin: 0pt, header: none, footer: none)
    #place(dx: -1000pt, dy: -1000pt, heading(level: 2, outlined: true)[
      #section.title
    ])
    #for page in section.pages [
      #image(page, width: 100%, height: 100%, fit: "cover")
    ]
  ]
]

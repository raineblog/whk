#import "@preview/min-book:0.1.0": *

#let sans = ("Noto Sans", "Noto Sans CJK SC")
#let serif = ("New Computer Modern", "Noto Serif CJK SC")
#set text(font: serif, lang: "zh", region: "CN")

#let book-data = json("toc.json")

#show: book.with(
  title: [ \ \ \ \ #text(font: serif, book-data.title) ],
  subtitle: [ \ #text(font: serif, book-data.subtitle) ],
  authors: book-data.authors.join(", "),
  date: datetime.today(),
  titlepage: true,
  // cover: image("cover.png"),
  paper: "a4",
  part: "Chapter",
  chapter: "Detail",
)

#set par(first-line-indent: 2em)

= #text(font: sans, "序言", size: 1.5em)

#set page(footer: none)

#align(center)[
  #text(weight: "bold", size: 1.5em, font: sans)[本书简介]
]

#for paragraph in book-data.info.abstract [
  #text(font: serif, paragraph)

]

#align(center + bottom)[
  #text(font: serif, book-data.info.publishing)
]

#for chapter in book-data.content [
  #heading(level: 1, outlined: true)[
    #text(font: serif, chapter.title, size: 1.5em)
  ]
  #for section in chapter.sections [
    #set page(margin: 0pt, header: none, footer: none)
    #place(dx: -1000pt, dy: -1000pt, heading(level: 2, outlined: true)[
      #text(font: serif, section.title)
    ])
    #for page in section.pages [
      #image(page, width: 100%, height: 100%, fit: "cover")
    ]
  ]
]

// pdf2svg test.pdf 如何使用.%d.svg all

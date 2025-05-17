from playwright.sync_api import sync_playwright
import os

def convertHtmlToPdf(items):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context()
        
        def m_download(htmlPath, pdfPath):
            if os.path.exists(pdfPath):
                os.remove(pdfPath)
            print(f'Downloading [{htmlPath}]', end=' ')
            page = context.new_page()

            page.goto(htmlPath, wait_until='networkidle')
            page.pdf(
                path=pdfPath,
                format="A4",
                margin={
                    "top": "25.5mm",
                    "bottom": "25.5mm",
                    "left": "19mm",
                    "right": "19mm"
                },
                print_background=True
            )

            page.close()
            print(f'Successful, see [{pdfPath}]!')

        for item in items:
            m_download(item[0], item[1])

        print("Successful!")
        browser.close()

def Main():
    pass
    # convertHtmlToPdf([
    #     ["https://raineblog.github.io/whk/mathematics/vector/1/", "平面向量.pdf"],
    #     ["https://raineblog.github.io/whk/mathematics/vector/3/", "复数.pdf"],
    #     ['https://raineblog.github.io/whk/mathematics/trigonometric/1/', '三角函数1.pdf'],
    #     ['https://raineblog.github.io/whk/mathematics/trigonometric/2/', '三角函数2.pdf'],
    #     ['https://raineblog.github.io/whk/mathematics/trigonometric/3/', '三角函数3.pdf'],
    # ])

if __name__ == "__main__":
    Main()

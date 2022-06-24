import PyPDF2  # 调用pypdf2库

pdf = open('picture/test.pdf', 'rb')  # 打开文件
pdfreader = PyPDF2.PdfFileReader(pdf)

# 读取内容
for i in range(0, pdfreader.getNumPages()):
    text = pdfreader.getPage(i).extractText()
    print(text)
    print('\n')

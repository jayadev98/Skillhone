import pdfplumber, sys
p = sys.argv[1]
pdf = pdfplumber.open(p)
print('PAGES', len(pdf.pages))
for i, page in enumerate(pdf.pages):
    print(f'--- PAGE {i+1} ---')
    print(page.extract_text() or '[no extracted text]')

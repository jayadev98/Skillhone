import pdfplumber, sys
pdf = pdfplumber.open(sys.argv[1])
for pi, page in enumerate(pdf.pages):
    print('PAGE', pi+1, 'SIZE', page.width, page.height)
    for img in page.images:
        print({k:img.get(k) for k in ('x0','x1','top','bottom','width','height','name','srcsize','colorspace','bits')})

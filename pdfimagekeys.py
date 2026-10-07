import pdfplumber, sys
with pdfplumber.open(sys.argv[1]) as pdf:
    for i, img in enumerate(pdf.pages[0].images[:10]):
        print(i, list(img.keys()))
        print('srcsize',img.get('srcsize'),'stream',type(img.get('stream')),'obj',type(img.get('object_id')))

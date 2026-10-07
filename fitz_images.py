import fitz, sys
pdf = fitz.open(sys.argv[1])
page = pdf[0]
for item in page.get_images(full=True):
    xref=item[0]
    info=pdf.extract_image(xref)
    rects=page.get_image_rects(xref)
    print(xref, info['width'], info['height'], info['ext'], rects)

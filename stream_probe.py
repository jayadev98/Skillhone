import pdfplumber, sys
with pdfplumber.open(sys.argv[1]) as pdf:
    img=pdf.pages[0].images[3]
    stream=img['stream']
    print('filters',stream.attrs.get('Filter'),'data',len(stream.get_data()),stream.get_data()[:16])

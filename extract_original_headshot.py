import pdfplumber, sys
with pdfplumber.open(sys.argv[1]) as pdf:
    img=next(im for im in pdf.pages[0].images if im['srcsize']==(356,512))
    open(sys.argv[2],'wb').write(img['stream'].get_data())

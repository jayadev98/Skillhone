import pdfplumber, sys
from PIL import Image
src, dest = sys.argv[1], sys.argv[2]
with pdfplumber.open(src) as pdf:
    page = pdf.pages[0]
    page.crop((64, 0, 150, 119)).to_image(resolution=400).save(dest + '.png')
im = Image.open(dest + '.png').convert('RGB')
im.save(dest + '.jpg', 'JPEG', quality=91, optimize=True)

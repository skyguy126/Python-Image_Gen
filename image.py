import Image, ImageEnhance, sys, os

reload(sys)
sys.setdefaultencoding('utf-8')

MAX_SIZE = 44

im = Image.open("" + raw_input("Drag and drop image: "))
width, height = im.size
factor = 0
if width < MAX_SIZE and height < MAX_SIZE:
    pass
else:
    if width > height:
        factor = float(width)/MAX_SIZE
    else:
        factor = float(height)/MAX_SIZE
    im = im.resize((int(float(width)/factor), int(float(height)/factor))).convert("L")

im = ImageEnhance.Contrast(im).enhance(1.2)
pixels = list(im.getdata())
width, height = im.size
pixels = [pixels[i * width:(i + 1) * width] for i in xrange(height)]
try:
    os.remove("output.txt")
except OSError:
    pass
kek = open("output.txt", 'w')
for r in range(0, height):
    for c in range(0, width):
        #if pixels[r][c] > 204:
        #    kek.write("*")
        #    continue
        if pixels[r][c] > 153:
            kek.write(u"\u2591")
            continue
        if pixels[r][c] > 102:
            kek.write(u"\u2592")
            continue
        if pixels[r][c] > 51:
            kek.write(u"\u2593")
            continue
        if pixels[r][c] >= 0:
            kek.write(u"\u2588")
            continue
    kek.write('\n')
kek.close()
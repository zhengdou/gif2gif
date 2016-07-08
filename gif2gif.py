from PIL import Image,ImageEnhance,ImageDraw
from images2gif import writeGif


WIDTH, HEIGHT= 40, 40
char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")


def gif2img(filename):
    im = Image.open(filename)
    mypalette = im.getpalette()
    i = 0
    try:
        imglist=[]
        while 1:
            im.putpalette(mypalette)
            new_im = Image.new("RGBA", im.size)
            new_im.paste(im)
            new_im.save('img'+str(i)+'.png')
            imglist.append('img'+str(i)+'.png')
            i += 1
            im.seek(im.tell() + 1)
    except EOFError:
        pass
    return imglist


def get_char(r,b,g,alpha = 256):
    length = len(char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    unit = (256.0 + 1)/length
    return char[int(gray/unit)]


def write2text(img):
    txt = ''
    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt += get_char(*im.getpixel((j,i)))
        txt += '\n'
    print txt
    name = img.split('.')[0]
    with open(name+'.txt','w') as f:
        f.write(txt)
    return name+'.txt'


def txt2img(filename):
    im = Image.new("RGB",(300,600), (255,255,255))
    draw = ImageDraw.Draw(im)
    f = open(filename)
    text = f.read()
    f.close()
    draw.text((0,0),text, fill=(0,0,0))  
    im.save(filename[:-3]+'jpg')
    return filename[:-3]+'jpg'


def jpg2gif(filename):
    time = 1/len(filename)
    images = [Image.open(fn) for fn in filename]
    outname = 'result.gif'
    if images is None:
    	print 'error'
    else :
    	writeGif(outname, images, duration=time, subRectangles=False)
    	print 'down'



if __name__=='__main__':
    imglist = gif2img('b.gif')
    txtlist=[]
    jpglist=[]
    for img in imglist:
        im = Image.open(img)
        im = im.resize((WIDTH,HEIGHT), Image.NEAREST)
        sharpness = ImageEnhance.Sharpness(im)
        im = sharpness.enhance(9.0)
        im.save(img,'png')
        txtlist.append(write2text(img))
    for text in txtlist:
        jpglist.append(txt2img(text))
    jpg2gif(jpglist)

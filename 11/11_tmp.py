
from PIL import Image, ImageDraw

im = Image.open('cave.jpg')
rgb_im = im.convert('RGB')
r, g, b = rgb_im.getpixel((1, 1))

#print(r, g, b)
#(65, 100, 137)
result_img = Image.new('RGB', (im.size[0], im.size[1]),(255,255,255))
draw  =  ImageDraw.Draw(result_img)
print im.size
starter = 0;
for x in range(0,im.size[0]):
    if (x%2)==1:
        starter = 0
    else:
        starter = 1

        pass
    for y in range(starter,im.size[1],2):
        print str(x)+"/"+str(y)+str(rgb_im.getpixel((x,y)))
        draw.point((x,y),rgb_im.getpixel((x,y)))
        pass

result_img.save("result_img.png")
result_img.show() 
   
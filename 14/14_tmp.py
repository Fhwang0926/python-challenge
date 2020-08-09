from PIL import Image, ImageDraw
import sys,time

im = Image.open('wire.png')
rgb_im = im.convert('RGB')
result_img = Image.new('RGB', (100, 100),(255,255,255))
draw  =  ImageDraw.Draw(result_img)
print im.size

x=0
y=0
x_up = 0
x_down = 0
y_right = 0
y_left = 0
count = 0
while count<10000:
	for x in range(y_left,100-y_right):
		draw.point((x,y),rgb_im.getpixel((count,0)))
		count+=1
		#time.sleep(0.1)
		#print "x : "+str(x)+" y : "+str(y)+" / count : "+str(count)+" / "+str(rgb_im.getpixel((count,0)))
	print "x : "+str(x)+" y : "+str(y)
	
	x_up+=1
	for y in range(x_up,100-x_down):
		draw.point((x,y),rgb_im.getpixel((count,0)))
		#time.sleep(0.1)
		count+=1
	print "x : "+str(x)+" y : "+str(y)
	#print "x : "+str(x)+" y : "+str(y)+" / count : "+str(count)+" / "+str(rgb_im.getpixel((count,0)))	
	y_right+=1
	
	for x in range(100-y_right,y_left,-1):
		draw.point((x,y),rgb_im.getpixel((count,0)))
		#time.sleep(0.1)
		count+=1
	print "x : "+str(x)+" y : "+str(y)
	#print "x : "+str(x)+" y : "+str(y)+" / count : "+str(count)+" / "+str(rgb_im.getpixel((count,0)))	
	
	x_down+=1
	for y in range(100-x_down,x_up,-1):
		draw.point((x,y),rgb_im.getpixel((count,0)))
		count+=1
		#time.sleep(0.1)
		#print "x : "+str(x)+" y : "+str(y)+" / count : "+str(count)+" / "+str(rgb_im.getpixel((count,0)))	
	print "x : "+str(x)+" y : "+str(y)
	
	y_left+=1
	pass
	print "------------"

result_img.save("result_img.png")
result_img.show() 
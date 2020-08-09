from PIL import Image, ImageDraw,ImageChops
import subprocess, os

im = Image.open('mozart.gif')
width, height = im.size
#print im.info

offset_in = '\xc3'

frame = 0
#for y in range(1):
for y in range(height):
    crop_box =  (0 , y, width, y+1) #new make 1 line image
    row = im.crop(crop_box) #crop to image
    #row.show() #can see croped 1 line image
    #print repr(row.tobytes()) #print method change tostrig ==> tobyte
    row_byte = row.tobytes(); #save byte 
    #for i in range(len(row_byte)): # 1 line image proceed
    #    character = row_byte[i] #read 1 byte
    #    if character == row_byte[i+1] and character == row_byte[i+2] and character == row_byte[i+3]:
    #        #if same 3 pixel print byte value
    #        print repr(character)
    offset = row_byte.index(offset_in) - 1 #get index to start index
    row = ImageChops.offset(row, -offset) #offset split
    im.paste(row,crop_box) #using offset to image pink area replace
    im.save('frame'+str(frame).zfill(3)+".png") #file name upcount format
    frame+=1 #file name up count
    #file save

#make animation gif file
#using window
os.chdir(os.path.realpath(os.path.dirname(__file__))) #change dir
os.system('del animation.gif') #if have gif file then del
os.system("ffmpeg -i frame%03d.png animation.gif") #make animation gif file
os.system('del frame*.png') #del file

#using linux
#print subprocess.check_output('convert -delay 1 -loop 0 frame*.png animated.gif'.split()) # make anmation gif file
#im.show() #show file
im.close() #close file
os.system('animation.gif') #open file


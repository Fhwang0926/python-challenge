# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from PIL import Image
import urllib2 as urllib
import io, re
result=""
im = urllib.urlopen("http://www.pythonchallenge.com/pc/def/oxygen.png")
image_data = io.BytesIO(im.read())
using_data = Image.open(image_data)
using_data = using_data.convert("RGB")
print using_data.mode
Temp=0;
o=""
count=0;
for x in range(0,608-1):
    #print using_data.getpixel((x,int(using_data.size[1]/2)))[0]
    
    tmp = using_data.getpixel((x,using_data.size[1]/2))[0]
    o+=chr(tmp)
    if (Temp!=tmp):
        result+=chr(tmp)
        Temp=tmp
        count=0
    else:
        count+=1
        if count==7:
            result+=chr(tmp)
            Temp=tmp
            continue
        
print result
code = ""
for tmp in re.findall("[0-9]{3}",result):
    code+=chr(int(tmp))

print "===>>> "+code
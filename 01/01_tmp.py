#!/usr/bin/python
# -*- coding: utf-8 -*-
import pyperclip



tmp = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.".upper()
result = ""
print(tmp)
print("-------------decoding-----------")

for tmp_char in tmp:
	if (ord(tmp_char) >= 65) & (ord(tmp_char) <=90):
		if (ord(tmp_char)+2) > 90:
			result+=chr(ord(tmp_char)-90+64+2)
			#-26+2
			#-24
		else:
			result+=chr(ord(tmp_char)+2)	
		pass
	else:
		if tmp_char==" ":
			result+=" "
		else:
			result+=tmp_char
	pass
print(result.lower())
pyperclip.copy(result.lower())
print("")
#make table
tmp=""
for x in range(65,90):
	tmp+=chr(x)
	pass
org=tmp
print("org : "+org)

tmp=""
for x in range(65,88):
	tmp+=chr(x+2)
	pass
tmp+="ab".upper()
tran=tmp

print("tra : "+tran)
print("")
output = "map".upper()
print("Real Result : "+output.translate(str.maketrans(org,tran)))
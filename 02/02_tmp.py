#!/usr/bin/python
# -*- coding: utf-8 -*-
f = open("test.txt",'r')
data = f.read()
f.close()
tmp=""
data = data.upper()
for x in data:
	if ((ord(x) > 64) & (ord(x) < 91)):
		tmp+=x
		print(tmp)
print(tmp)
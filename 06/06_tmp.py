import zipfile, re

num = 90052
zipf = zipfile.ZipFile("C:\Temp/channel.zip")
result = "";
try:
	while 1:
		f = open("C:\Temp/channel/"+str(num)+".txt",'r')
		data = f.read()
		f.close()
		result+=zipf.getinfo(str(num)+".txt").comment;
		num=data.split(" ")[3]
		print data

		#print str(num)+".txt"
	pass
except Exception, e:
	f = open("C:\Temp/channel/"+str(num)+".txt",'r')
	data = f.read()
	f.close()
	print data

print result


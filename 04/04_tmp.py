import re,urllib2
nextcode=12345
tmp=0;
data=""
try:

	while 1:
		data=urllib2.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="+str(nextcode))
		data = data.read()

		nextcode="".join(re.findall("[0-9]",data))
		if nextcode=="":
			exit
			pass
		tmp+=1
		print str(tmp)+"http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + str(nextcode)	
except Exception, e:
	print data;
	pass
import re, urllib2

data=urllib2.urlopen("http://www.pythonchallenge.com/pc/def/equality.html")
data = data.read()
print ""
print "".join(re.findall("[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]",data))

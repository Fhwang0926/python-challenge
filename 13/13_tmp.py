import xmlrpclib
url0 = "http://www.pythonchallenge.com/pc/phonebook.php"
url1 = "http://www.xmlrpc.com/discuss/msgReader$128"
proxy = xmlrpclib.ServerProxy(url0)

for x in proxy.system.listMethods():
	print str(x)
	pass
print "-"*20
print "phone : " + proxy.system.methodHelp("phone")
print ""
print "multicall : " +proxy.system.methodHelp("system.multicall")
print ""
print "methodSignature : " +proxy.system.methodHelp("system.methodSignature")
print ""
print "getCapabilities : " +proxy.system.methodHelp("system.getCapabilities")
print ""
print "evil : " + proxy.phone("Bert")
print "call to evil : " + proxy.multicall("Bert")



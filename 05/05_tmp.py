import pickle

f = open("C:\Temp/banner_05.p",'r')
data = pickle.load(f)
tmp=""
for x in data:
	for y in x:
		print y[0]*y[1]
		tmp+=y[0]*y[1]
		pass
	tmp+="\n"
	pass

print tmp
import sys

result = []

start_num = "1"
tmp_char = ""
tmp_str = ""
list_index = 0;
count = 1

while 1:
	print str(count)+" : "+start_num
	for x in range(0,len(start_num)+1):
		if start_num[x:x+1] == tmp_char:
			tmp_str+=tmp_char
		else:
			
			result.append(tmp_str+tmp_char)
			tmp_char = start_num[x:x+1]
			tmp_str = ""
			list_index+=1
			pass
		pass
		#print result
	start_num=""
	for x in range(1,len(result)):
		tmp = result[x]
		start_num+=tmp[:1]+str(len(tmp))
		#print start_num
		pass
	
	result = [] * len(result)
	if count == 30:
		print start_num
		print  "result : "+str(len(start_num))
		break
		pass
	count+=1
pass



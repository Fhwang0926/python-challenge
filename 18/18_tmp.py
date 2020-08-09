import gzip,difflib

with gzip.open('deltas.gz', 'rb') as f:
    file_content = f.read()
data1 = []
data2 = []
for line in file_content.split("\n"):
    # print line
    # print line[:53]
    # print line[56:]
    # print str(len(line[:53]))+" / "+str(len(line[56:]))
    data1.append(str(line[:53].strip()))
    data2.append(str(line[56:].strip()))
comp = list(difflib.Differ().compare(data1,data2))
#print comp
img1 = open('18_1.png','wb')
img2 = open('18_2.png','wb')
img3 = open('18_3.png','wb')

for line in comp:
    byte = [chr(int(b,16)) for b in line[2:].split()]
    print byte
    if line[:1]=='+':
        for tmp in byte:
            img1.write(tmp)    
            pass
    elif line[:1]=='-':
        for tmp in byte:
            img2.write(tmp)    
            pass
    else:
        for tmp in byte:
            img3.write(tmp)    
            pass
img1.close()
img2.close()
img3.close()
        
        
        


file_data = open('evil2.gfx','rb')
file_data1 = open('tmp1.jpg','wb+')
file_data2 = open('tmp2.jpg','wb+')
file_data3 = open('tmp3.jpg','wb+')
file_data4 = open('tmp4.jpg','wb+')
file_data5 = open('tmp5.jpg','wb+')

print file_data
index = 1
while 1:
    s=file_data.read(1)
    if s=="":break
    if index==1:
        file_data1.write(s)
        index+=1
    elif index==2:
        file_data2.write(s)
        index+=1
    elif index==3:
        file_data3.write(s)
        index+=1
    elif index==4:
        file_data4.write(s)
        index+=1
    elif index==5:
        file_data5.write(s)
        index=1
    print str(index) + str(s)
    pass
file_data.close()
file_data5.close()
file_data4.close()
file_data3.close()
file_data2.close()
file_data1.close()
import base64, httplib

login = base64.b64encode("butter:fly")
headers = {"Authorization" : "Basic %s" % (login)}
conn = httplib.HTTPConnection("www.pythonchallenge.com")
data_index = 1152983631#30202



def get_byte(start,end = 0):
    tmp = ""
    if end > 0:
        for data_index in range(start,end,1):
            headers.update({"Range" : "bytes=%s-%s" % (data_index,data_index+1)})# get 1byte
            conn.request("GET","/pc/hex/unreal.jpg","",headers)
            get_data = conn.getresponse().read()

            if get_data:
                tmp += get_data
        return tmp
    else:
        headers.update({"Range" : "bytes=%s-" % (start)})# get 1byte
        conn.request("GET","/pc/hex/unreal.jpg","",headers)
        get_data = conn.getresponse().read()

        f = open("level20.zip", "wb+")
        f.write(get_data)
        f.close()
        print "save file"
    print "end"


get_byte(data_index)

print "GG"


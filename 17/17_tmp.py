import urllib2,re,requests,bz2,urllib,os

def call(who):
    import xmlrpclib

    proxy = xmlrpclib.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")
    print "Leopold :  "+ proxy.phone(who)
    return proxy.phone(who).split("-")

url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing="
code = "12345"
cookies = ""

while 1:
    break
    request = urllib2.Request(url+code)
    html = urllib2.urlopen(request).read()
    r = requests.get((url+code))
    next_num = html.split(" ")[len(html.split(" "))-1]
    try:
        cookies  += r.cookies['info']
        code = next_num
        print html
    except:
        result = urllib.unquote(urllib.unquote("".join(cookies.replace("+"," "))))
        print result
        print bz2.decompress(result)
        call("Leopold")
        break
print "------------------------------------"

cookie = {'info': 'the flowers are on their way'}

r = requests.get('http://www.pythonchallenge.com/pc/stuff/violin.php', cookies=cookie)
print r.text

    
        
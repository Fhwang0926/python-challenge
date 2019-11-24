
import zipfile, os



broken_zip = zipfile.ZipFile('mybroken.zip')
# the zip file has an image inside
print('The content of the zip file is "{0}"'.format(broken_zip.namelist()[0]))
# the zip seems to be broken
print('The file "{0}" is broken (Bad CRC).'.format(broken_zip.testzip()))
# we're going to extract it anyway
gif_zipinfo = broken_zip.getinfo('mybroken.gif')
gif_zipinfo.CRC = None
broken_zip.extract(gif_zipinfo)

try:
    os.system("mybroken.gif")
except IOError:
    print("It's true, the image is broken.")
print("END")




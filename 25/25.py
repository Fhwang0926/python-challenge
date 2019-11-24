from requests import get  # to make GET request
import os

def download(url, file_name):
    # open in binary mode
    with open(file_name, "wb") as file:
        # get request
        response = get(url, auth=("butter", "fly"))
        if(response.status_code != 200): print("rscode : ", response.status_code); raise Exception('WTF response not 200') 
        # write to file
        file.write(response.content)

# start insdex 1 because lake1.jpg
index = 1
while 1:
    if os.path.exists("lake1.wav"): break
    try:
        url = "http://www.pythonchallenge.com/pc/hex/lake{}.wav".format(index)
        name = "lake{}.wav".format(index)
        download(url, name)
        print("[+]", url, name)
        index+=1
        pass
    except Exception as e:
        print("OMG : ", e)
        break
    pass
print("END download")


from PIL import Image
import wave

wavs = [wave.open('lake%d.wav' % i) for i in range(1,26)]
result = Image.new('RGB', (300,300), 0)
num_frames = wavs[0].getnframes()
for i in range(len(wavs)): 
    byte = wavs[i].readframes(num_frames)
    img = Image.frombytes('RGB', (60, 60), byte)
    result.paste(img, (60 * (i % 5), 60 * (i // 5)))
result.save('level25.png')
print("show")
os.system('level25.png')
print("END")
import zlib, bz2, time

with open("package.pack", "rb") as f:
    data = f.read()
    print(data[:10])
    rs = ''
    while True:
        # print("run", data[:10], "~~", data[-10:])
        # time.sleep(1)
        if data.startswith(b'x\x9c'):
            print("startswith : ", data[:5], "~", data[-5:])
            data = zlib.decompress(data)
            rs += '#';
        elif data.startswith(b'BZh'):       
            print("startswith : ", data[:5], "~", data[-5:])
            data = bz2.decompress(data)
            rs += ' ';
        elif data.endswith(b'\x9cx'):
            print("endswith : ", data[:5], "~", data[-5:])
            data = data[::-1]
            rs += '\n';
        else:
            print(data)
            break
    print(data)
    print(rs)


# with open("level20.zip", 'rb') as f:
#     data = f.read()
#     time.sleep(1)
    # print(data[:5], "~~", data[-5:])
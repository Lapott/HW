# https://en.wikipedia.org/wiki/Classful_network
ip = "193.0.0.5"
oct1 = int(ip.split(".")[0])

if oct1 < 128:
    print("Class A")
elif 128 <= oct1 < 192:
    print("Class B")
elif 192 <= oct1 < 224:
    print("Class C")
elif 224 <= oct1 < 240:
    print("Class D")
else:
    print("Class E")
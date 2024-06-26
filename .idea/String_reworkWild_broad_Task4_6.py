def _invert(n):
    return n^255
ip = "192.168.43.54 / 255.255.254.0"
ipmask = ip.split(" / ")
ipad = ipmask[0]
mask = ipmask[1]
ipad_list = ipad.split(".")
mask_list = mask.split(".")
ip1 = int(ipad_list[0])
ip2 = int(ipad_list[1])
ip3 = int(ipad_list[2])
ip4 = int(ipad_list[3])
m1 = int(mask_list[0])
m2 = int(mask_list[1])
m3 = int(mask_list[2])
m4 = int(mask_list[3])
net1 = ip1 & m1
net2 = ip2 & m2
net3 = ip3 & m3
net4 = ip4 & m4
print (f"network = {net1}.{net2}.{net3}.{net4}")
wild1 = _invert(m1)
wild2 = _invert(m2)
wild3 = _invert(m3)
wild4 = _invert(m4)
print (f"wildcard = {wild1}.{wild2}.{wild3}.{wild4}")
broad1 = net1 | wild1
broad2 = net2 | wild2
broad3 = net3 | wild3
broad4 = net4 | wild4
print (f"broadcast =  {broad1}.{broad2}.{broad3}.{broad4}")
hostmin4 = net4 + 1
print (f"hostmin = {net1}.{net2}.{net3}.{hostmin4}")
hostmax4 = broad4 - 1
print (f"maxhost = {broad1}.{broad2}.{broad3}.{hostmax4}")

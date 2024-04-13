def _invert(n):
    return n^255
ip1, ip2, ip3, ip4 = 192, 168, 43, 54
m1, m2, m3, m4 = 255, 255, 255, 240
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
print (f"hostmin =  {broad1}.{broad2}.{broad3}.{broad4}")
hostmin4 = net4 + 1
print (f"hostmax = {net1}.{net2}.{net3}.{hostmin4}")
hostmax4 = broad4 - 1
print (f"broadcast = {broad1}.{broad2}.{broad3}.{hostmax4}")


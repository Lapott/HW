def num_bin(num):
    binary = f"{num:b}"
    binaryfull = f"{binary:0>8}"
    return binaryfull
ip = "10.23.43.234"
ipspl = ip.split(".")
print (ipspl)
ip1 = (int(ipspl[0]))
ip2 = (int(ipspl[1]))
ip3 = (int(ipspl[2]))
ip4 = (int(ipspl[3]))
bin = num_bin(ip1) + num_bin(ip2) + num_bin(ip3) + num_bin(ip4)
print (bin)
#    while n > 0:
#    binar = str(n % 2) + binar
#    n = n // 2
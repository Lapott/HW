import re
mac_list = [
    "50-46-5D-6E-8C-20",
    "50-46-5d-6e-8c-20",
    "50:46:5d:6e:8c:20",
    "5046:5d6e:8c20",
    "50465d6e8c20",
    "50465d:6e8c20",
]
def get_mac_notation(mac):
    if re.match(r"([0-9a-f]{2}-){5}[0-9a-f]{2}", string=mac):
         mac_notation = "lowercase"
    elif re.match(r"([0-9A-F]{2}-){5}[0-9A-F]{2}", string=mac):
        mac_notation = "IEEE EUI-48"
    elif re.match(r"([0-9a-f]{2}:){5}[0-9a-f]{2}", string=mac):
        mac_notation = "UNIX"
    elif re.match(r"([0-9a-f]{4}:){2}[0-9a-f]{4}", string=mac):
        mac_notation =  "Cisco"
    elif re.match(r"([a-f0-9]{12})", string=mac):
        mac_notation =  "Bare"
    else:
        mac_notation = "unknown"
    return mac_notation
for  mac in mac_list:
    notation = get_mac_notation(mac)
    print (mac, notation)

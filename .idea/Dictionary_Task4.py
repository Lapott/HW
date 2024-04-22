import pprint
SCRAPLI_TEMPLATE = {
    "auth_username": "cisco",
    "auth_password": "password",
    "transport": "system",
    "auth_strict_key": False,
    "port": 22,
}
devtemp1 = {
   "hostname": "sw1.abcd.net"
}
devtemp2 = {
    "hostname": "sw1.abcd.net",
    "transport": "telnet",
    "port": 23,
}
device1 = SCRAPLI_TEMPLATE.copy()
device1.update(devtemp1)
device2 = SCRAPLI_TEMPLATE.copy()
device2.update(devtemp2)
devicelist = [device1, device2]
pprint.pp(devicelist)

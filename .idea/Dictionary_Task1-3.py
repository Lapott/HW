import pprint
# Task1
device1 = {
   "hostname" : "r1.abcd.net",
   "ip" : "192.168.1.1",
   "username" : "cisco",
   "password"  : "secret",
   "platform" : "cisco_ios",
   "enable" : "True",}

device2 = {
   "hostname" : "sw1.abcd.net",
   "ip" : "192.168.1.2",
   "username" : "admin",
   "password"  : "secret",
   "platform" : "huawei_vrp",
   "enable"  : "False",}
device3  = {
   "hostname" : "wlc.abcd.net",
   "ip" : "192.168.1.3",
   "username" : "wlc_admin",
   "password"  : "password",
   "enable"  : "False",}
# Task2
devices_list = [device1, device2, device3]
# Task3
devices_dict = {
    devices_list[0]["hostname"]: devices_list[0],
    devices_list[1]["hostname"]: devices_list[1],
    devices_list[2]["hostname"]: devices_list[2],
}
pprint.pp(devices_dict)
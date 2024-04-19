intf_list = ["gi0/0", "gi0/1", "gi0/22", "gi0/23", "gi0/3", "gi0/4"]
intf_list.remove("gi0/22")
intf_list[2] = "gi0/2"
print (intf_list)
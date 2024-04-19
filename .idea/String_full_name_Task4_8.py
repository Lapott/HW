if_name1 = "Eth0/1"
if_name2 = "GE1/0/2"
if_name3 = "Тen4/3"
if_namefull1 = if_name1.replace("Eth", "Ethernet")
if_namefull2 = if_name2.replace("GE", "GigabitEthernet")
if_namefull3 = if_name3.replace("Тen", "TenGigabitEthernet")
print (if_namefull1)
print (if_namefull2)
print (if_namefull3)
output = "switchport trunk allowed vlan 2,101,104"
result = output.split()[-1].split(",")
print(result)
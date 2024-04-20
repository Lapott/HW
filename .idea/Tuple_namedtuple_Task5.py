from collections import namedtuple
InterfaceStatus = namedtuple("InterfaceStatus", ["name", "ip", "status"])
InterfaceStatus1 = InterfaceStatus("GigabitEthernet0/2", "192.168.190.235", "up")
InterfaceStatus2 = InterfaceStatus("GigabitEthernet0/4", "192.168.191.2", "down")
InterfaceStatus3 = InterfaceStatus("TenGigabitEthernet2/1", "unassigned", "up")
InterfaceStatus4 = InterfaceStatus("Te36/45 ", "unassigned", "down")
intf_brief = [InterfaceStatus1, InterfaceStatus2, InterfaceStatus3, InterfaceStatus4]
print(len(intf_brief))
print(isinstance(intf_brief, list))
print(intf_brief[0].status)
print(intf_brief[1].ip)
print(intf_brief[3].name)
interfaces = [
    "Eth0/0",
    "Gig0/4/3",
    "GE4/4",
    "Po3",
    "Ten5/4",
    "XGE4/1",
    "Eth-Trunk4",
]


def interf(interf):
    if interf.find("Eth") == 0:
        interf = interf.replace("Eth", "Ethernet")
    if interf.find("Fa") == 0:
        interf = interf.replace("Fa", "FastEthernet")
    if interf.find("Gig") == 0:
        interf = interf.replace("Gig", "GigabitEthernet")
    if interf.find("GE") == 0:
        interf = interf.replace("GE", "GigabitEthernet")
    if interf.find("Ten") == 0:
        interf = interf.replace("Ten", "TenGigabitEthernet")
    if interf.find("TE") == 0:
        interf = interf.replace("TE", "TenGigabitEthernet")
    if interf.find("XGE") == 0:
        interf = interf.replace("XGE", "TenGigabitEthernet")
    return interf


for i in interfaces:
    print(i, interf(i))

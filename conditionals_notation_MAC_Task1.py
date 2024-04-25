import re
#   IEEE EUI-48 lowercase
# mac = "50-4d-57-66-83-20"
#   IEEE EUI-48
# mac = "50-46-5D-6E-8C-20"
# mac = "50-46-5D-6E-8C-20"
#   unix notation
# mac = "50:46:5d:6e:8c:20"
#   cisco notation
mac = "5046:5d6e:8c20"
#   bare notation
# mac = "50465d66f320"
#   test zero
# mac = "000000000000"

if re.match(r"([0-9a-f]{2}-){5}[0-9a-f]{2}", string=mac):
    print(f"нотация {mac}: IEEE EUI-48 lowercase")
elif re.match(r"([0-9A-F]{2}-){5}[0-9A-F]{2}", string=mac):
    print(f"нотация {mac}: IEEE EUI-48")
elif re.match(r"([0-9a-f]{2}:){5}[0-9a-f]{2}", string=mac):
    print(f"нотация {mac}: UNIX")
elif re.match(r"([0-9a-f]{4}:){2}[0-9a-f]{4}", string=mac):
    print(f"нотация {mac}: Cisco")
elif re.match(r"([a-f0-9]{12})", string=mac):
    print(f"нотация {mac}: Bare")
else:
    print(f"нотация {mac}: unknown")
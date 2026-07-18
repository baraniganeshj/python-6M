devices = ["Router-1", "Switch-1", "Firewall-1", "Server-1"]

for device in devices:
    print("Checking", device)

print()

for device in devices:
    print(f"{device}: UP")

print()

devices.append("Router-2")

for device in devices:
    print(f"{device}: UP")

ISP = ["AT&T", "Verizon", "Lumen", "Comcast"]

print()

for vendor in ISP:
    print(f"Checking vendor: {vendor}")




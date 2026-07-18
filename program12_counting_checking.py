Status_List = ['UP', 'DOWN', 'UP', 'DOWN', 'UP']

print(f"Status List:\n{Status_List}")
print()

down_count = Status_List.count("DOWN")
up_count = Status_List.count("UP")

print(f"Total DOWN Devices: {down_count}")
print(f"Total UP Devices: {up_count}")

devices = ["Router-1", "Switch-1", "Firewall-1", "Server-1"]

print()
print(f"Firewall-1 Exists: {"Firewall-1" in devices}")
print(f"Router-99 Exists: {"Router-99" in devices}")
print()

Incident = ["INC1001", "INC1002", "INC1003", "INC1002", "INC1004"]

print(f"Incident Count for INC1002: {Incident.count('INC1002')}")
print(f"INC1005 Exists: {'INC1005' in Incident}")

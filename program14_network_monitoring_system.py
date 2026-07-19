devices = ["Router-1", "Switch-1", "Firewall-1", "Server-1", "Router-2"]
statuses = ["UP", "DOWN", "UP", "DOWN", "UP"]


print()
print("=" * 50)
print("NETWORK MONITORING REPORT")
print("=" * 50)
print()

for i in range(len(devices)):
    if statuses[i] == "DOWN":
        print(f"{devices[i]} - {statuses[i]} - ALERT")
    else:
        print(f"{devices[i]} - {statuses[i]} - OK")

print()
print("=" * 50)
print("SUMMARY")
print("=" * 50)
print()

print(f"\nTotal Devices = {len(devices)}")
print(f"Total Up Devices = {statuses.count('UP')}")
print(f"Total Down Devices = {statuses.count('DOWN')}")

print()

if "DOWN" in statuses:
    print("Network Attention Required")
else:
    print("Network Healthy")

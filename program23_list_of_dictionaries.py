devices = [{"Name": "Chennai-RTR-1", "IP": "10.10.10.1", "Status": "UP", "CPU": 55, "Memory": 60}, {"Name": "Chennai-SW-1", "IP": "10.10.10.2", "Status": "DOWN", "CPU": 0, "Memory": 0}, {"Name": "Bangalore-FW-1", "IP": "10.10.20.1", "Status": "UP", "CPU": 92, "Memory": 88}]
devices_down_count = sum(1 for device in devices if device['Status'] == "DOWN")

print("=" * 50)
print("DEVICE INVENTORY")
print("=" * 50)
print(f"\nTotal devices down: {devices_down_count}")

for device in devices:
    if device['CPU'] > 90:
        print(f"High CPU Device: {device['Name']}")

for device in devices:
    if device['Status'] == "DOWN":
        print(f"\n{device['Name']}: ALERT")
    else:
        print(f"\n{device['Name']}: OK")
    print(f"IP: {device['IP']}")
    print(f"Status: {device['Status']}")
    print(f"CPU: {device['CPU']}%")
    print(f"Memory: {device['Memory']}%")
    
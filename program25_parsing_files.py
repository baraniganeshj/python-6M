with open("network_log.txt", "r") as file:
    content = file.read()
down_devices = []
for line in content.splitlines():
    parts = line.split()
    date = parts[0]
    device = parts[1]
    status = parts[2]
    print(f"Device: {device}, | Status: {status}")

    if status == "DOWN":
        down_devices.append(device)

down_count = len(down_devices)
print(f"\nDOWN devices: {down_count}")

print("\nDevice Currently Down:")
for device in down_devices:
    print(device)
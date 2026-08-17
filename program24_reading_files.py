print("="*50)
print("NETWORK LOG READER")
print("="*50)
with open("network_log.txt", "r") as file:
    content = file.read()
    print(f"\n{content}")

down_devices = len([line for line in content.splitlines() if "DOWN" in line])
print(f"\nDOWN devices found: {down_devices}")
Devices = ["Router-1", "Switch-1", "Firewall-1", "Server-1"]
Statuses = ["UP", "DOWN", "UP", "DOWN"]

def check_device_status(device_name, status):
    if status == "UP":
        return f"{device_name} : {status} - OK"
    elif status == "DOWN":
        return f"{device_name} : {status} - ALERT"
    else:
        return f"{device_name} : {status} - UNKNOWN"

def count_down_devices(statuses_list):
    down_count = 0
    for status in statuses_list:
        if status == "DOWN":
            down_count += 1
    return down_count

down_count = count_down_devices(Statuses)

def generate_summary(down_counts):
        if down_counts == 0:
            return "NETWORK HEALTHY"
        elif down_counts in [1, 2]:
            return "ATTENTION REQUIRED"
        elif down_counts >= 3:
            return "CRITICAL NETWORK CONDITION"

print("="*50)
print("NETWORKING MONITORING REPORT")
print("="*50)
print()
for i in range(len(Devices)):
    print(check_device_status(Devices[i], Statuses[i]))
print()
print("="*50)
print("SUMMARY")
print("="*50)
print(f"Total Devices: {len(Devices)}")
print(f"Devices Down: {down_count}")
print()
print(generate_summary(down_count))

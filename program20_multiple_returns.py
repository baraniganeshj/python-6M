Devices = ["Router-1", "Switch-1", "Firewall-1", "Server-1", "Router-2"]
Statuses = ["UP", "DOWN", "UP", "DOWN", "UP"]
CPU_usage = [45, 92, 70, 95, 50]

def get_network_statistics(devices, statuses, cpu_usage):
    total_devices = len(devices)
    down_count = 0
    high_cpu_count = 0
    for i in range(len(devices)):
        if statuses[i] == "DOWN":
            down_count += 1
        if cpu_usage[i] > 90:
            high_cpu_count += 1
    return total_devices, down_count, high_cpu_count

total_devices, down_count, high_cpu_count = get_network_statistics(Devices, Statuses, CPU_usage)

print("="*50)
print("NETWORK STATISTICS REPORT")
print("="*50)
print(f"\nTotal Devices: {total_devices}")
print(f"\nDevices Down: {down_count}")
print(f"\nHigh CPU Devices: {high_cpu_count}")

if down_count > 1:
    print("\nATTENTION REQUIRED")
else:
    print("\nNETWORK HEALTHY")
devices = ["Chennai-RTR-1", "Chennai-SW-1", "Chennai-FW-1", "BLR-RTR-1",
          "BLR-SW-1", "BLR-FW-1", "Chennai-AP-1", "BLR-AP-1"]
statuses = ["UP", "DOWN", "UP", "UP", "UP", "UP", "UP", "UP"]
cpu_usage = [55, 0, 94, 78, 0, 0, 91, 62]
memory_usage = [60, 0, 88, 92, 0, 0, 70, 55]

def network_report(devices, statuses, cpu_usage, memory_usage):
    total_devices = len(devices)
    devices_down =  statuses.count("DOWN")
    high_cpu = len([cpu for cpu in cpu_usage if cpu > 90])
    high_memory = len([memory for memory in memory_usage if memory > 85])
    worst_device = devices[cpu_usage.index(max(cpu_usage))]
    return total_devices, devices_down, high_cpu, high_memory, worst_device

total_devices, devices_down, high_cpu, high_memory, worst_device = network_report(devices, statuses, cpu_usage, memory_usage)
print(f"Total Devices: {total_devices}")
print(f"Devices Down: {devices_down}")
print(f"Devices with High CPU Usage: {high_cpu}")
print(f"Devices with High Memory Usage: {high_memory}")
print(f"Worst Device (Highest CPU Usage): {worst_device}")

if devices_down > 2:
    print("CRITICAL: MULTIPLE DEVICES DOWN")
elif high_cpu > 0 and high_memory > 0:
    print("WARNING: RESOURCE PRESSURE ON MULTIPLE FRONTS")
else:
    print("NETWORK STABLE")


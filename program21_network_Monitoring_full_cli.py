devices = ["Chennai-RTR-1", "Chennai-SW-1", "Bangalore-FW-1", "Bangalore-RTR-2", "Chennai-AP-1", "Bangalore-AP-1"]
statuses = ["UP", "DOWN", "UP", "UP", "UP", "DOWN"]
cpu_usage = [45, 0, 92, 78, 55, 0]
memory_usage = [60, 0, 88, 72, 65, 0]
uptime_percentages = [98.5, 0, 95.2, 99.1, 97.8, 0]


def analyze_network(devices, statuses, cpu_usage, memory_usage, uptime_percentages):
    total_devices = len(devices)
    devices_down = 0
    critical_cpu_count = 0
    critical_memory_count = 0
    average_cpu_usage = sum(cpu_usage) / total_devices
    average_memory_usage = sum(memory_usage) / total_devices
    average_uptime = sum(uptime_percentages) / len(uptime_percentages)
    for i in range(len(devices)):
        if statuses[i] == "DOWN":
            devices_down += 1
        if cpu_usage[i] > 90:
            critical_cpu_count += 1
        if memory_usage[i] > 85:
            critical_memory_count += 1
    return total_devices, devices_down, critical_cpu_count, critical_memory_count, average_cpu_usage, average_memory_usage, average_uptime

def generate_alerts(statuses, cpu_usage, memory_usage, devices):
    alerts = []
    for i in range(len(devices)):
        if statuses[i] == "DOWN":
            alerts.append(f"Device {devices[i]} is DOWN")
        if cpu_usage[i] > 90:
            alerts.append(f"Device {devices[i]} has high CPU usage ({cpu_usage[i]}%)")
        if memory_usage[i] > 85:
            alerts.append(f"Device {devices[i]} has high memory usage ({memory_usage[i]}%)")
    return alerts

total_devices, devices_down, critical_cpu_count, critical_memory_count, average_cpu_usage, average_memory_usage, average_uptime = analyze_network(devices, statuses, cpu_usage, memory_usage, uptime_percentages)
alerts = generate_alerts(statuses, cpu_usage, memory_usage, devices)

print("=" * 50)
print("DEVICE STATUS REPORT")
print("=" * 50)

for i in range(len(devices)):
    print(
        f"{devices[i]} | "
        f"{statuses[i]} | "
        f"CPU: {cpu_usage[i]}% | "
        f"Memory: {memory_usage[i]}% | "
        f"Uptime: {uptime_percentages[i]}%"
    )
print("="*50)
print("NETWORK ANALYSIS:")
print(f"Total Devices: {total_devices}")
print(f"Devices Down: {devices_down}")
print(f"Devices with Critical CPU Usage: {critical_cpu_count}")
print(f"Devices with Critical Memory Usage: {critical_memory_count}")
print(f"Average CPU Usage: {average_cpu_usage}%")
print(f"Average Memory Usage: {average_memory_usage}%")
print(f"Average Uptime: {average_uptime:.2f}%")
print("="*50)
print("ALERTS:")

if devices_down > 1:
    print(f"CRITICAL: Multiple Devices down: {devices_down}")

for alert in alerts:
    if alert.startswith("Device") and "CPU" in alert:
        print(f"CRITICAL: {alert}")
    elif alert.startswith("Device") and "memory" in alert:
        print(f"CRITICAL: {alert}")

print()
print("="*50)
if devices_down == 0 and critical_cpu_count == 0 and critical_memory_count == 0:
    print("DECISION: NETWORK STATUS: HEALTHY")
else:
    print("DECISION: ESCALATE TO MANAGER - Multiple critical issues detected")
print("="*50)


# Program 5: Comparisons and Boolean Logic
# Understanding > < == and/or operators

device1_temp = 45
device1_cpu_usage = 92
device2_temp = 65
device2_cpu_usage = 72

print("=" * 50)
print("NETWORK DEVICE STATUS CHECK")
print("=" * 50)

print("\nDevice 1 Status:")
print(f"Temperature: {device1_temp}°C")
print(f"CPU Usage: {device1_cpu_usage}%")

print(f"\nIs temperature too high (>50)? {device1_temp >50} ")
print(f"Is CPU critical (> 85)? {device1_cpu_usage > 85}")
print(f"Is BOTH critical? {device1_temp > 50 and device1_cpu_usage > 85}")
print(f"Is EITHER critical? {device1_temp > 50 or device1_cpu_usage > 85}")

print("\n" + "=" * 50)

print(f"\nDevice 2 Status:")
print(f"Temperature: {device2_temp}°C")
print(f"CPU Usage: {device2_cpu_usage}%")

print(f"\nIs temperature too high (>50)? {device2_temp >50} ")
print(f"Is CPU critical (> 85)? {device2_cpu_usage > 85}")
print(f"Is BOTH critical? {device2_temp > 50 and device2_cpu_usage > 85}")
print(f"Is EITHER critical? {device2_temp > 50 or device2_cpu_usage > 85}")

print("\n" + "=" * 50)
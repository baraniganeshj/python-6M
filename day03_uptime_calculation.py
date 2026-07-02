total_minutes = 720
downtime_minutes = 45
uptime_minutes = total_minutes - downtime_minutes
uptime_percentage = (uptime_minutes / total_minutes) * 100
downtime_percentage = (downtime_minutes / total_minutes) * 100

print("Total Minutes:", total_minutes)
print("Downtime Minutes:", downtime_minutes)
print("Uptime Minutes:", uptime_minutes)
print("Uptime Percentage:", uptime_percentage)
print("Downtime Percentage:", downtime_percentage)
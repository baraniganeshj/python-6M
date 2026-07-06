total_minutes = 10080
downtime_minutes = 300
uptime_minutes = (total_minutes - downtime_minutes)
uptime_percentage = (uptime_minutes/total_minutes * 100)


print("=" * 50)
print("NETWORK UPTIME ALERT SYSTEM")
print("=" * 50)

print(f"\nTotal Minutes: {total_minutes}")
print(f"Downtime Minutes: {downtime_minutes}")
print(f"Uptime Percentage: {uptime_percentage:.2f}%")

if uptime_percentage >= 95:
    print("\nStatus: Healthy")
    print("Action: No escalation needed. System running smoothly.")
    print("\n" + "=" * 50)

else:
    print("\nStatus: Alert")
    print("Action: ESCALATE to manager immediately. Uptime below threshold.")
    print("\n" + "=" * 50)

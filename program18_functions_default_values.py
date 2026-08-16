def generate_alert(device_name, issue=None):
    if issue is None:
        issue = "No Issue Reported"
    return f"ALERT: {device_name} - {issue}"

Call_1 = generate_alert("Router-1", "Interface Down")
Call_2 = generate_alert("Firewall-1", "High CPU")
Call_3 = generate_alert("Switch-1")

print("="*50)
print("ALERT GENERATOR")
print("="*50)
print("")
print(f"\n{Call_1}")
print(f"\n{Call_2}")
print(f"\n{Call_3}")
All_Alerts = ['INFO', 'WARNING', 'CRITICAL', 'INFO', 'CRITICAL', 'WARNING']

print(f"All Alerts: {All_Alerts}")
print()

print(f"Critical Alerts: {[alert for alert in All_Alerts if alert == 'CRITICAL']}")
print()

print(f"Toatal Critical Alerts: {All_Alerts.count}")
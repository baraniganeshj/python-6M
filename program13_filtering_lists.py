All_Alerts = ['INFO', 'WARNING', 'CRITICAL', 'INFO', 'CRITICAL', 'WARNING']
print(f"All Alerts:\n {All_Alerts}")
print()
cirtical_alerts = [alert for alert in All_Alerts if alert == 'CRITICAL']
print(f"Critical Alerts:\n {cirtical_alerts}")
print()
critical_count = cirtical_alerts.count('CRITICAL')
print(f"Total Critical Alerts: {(critical_count)}")

devices = ["Router-1", "Switch-1", "Firewall-1", "Server-1"]
Routers = [device for device in devices if device == 'Router-1']
print()
print(f"Routers:\n {Routers}")


All_Incidents = ['P3', 'P1', 'P4', 'P1', 'P2']
print(f"\nAll Incidents:\n {All_Incidents}")
P1_Incidents = [incident for incident in All_Incidents if incident == 'P1']
print(f"\nP1 Incidents:\n {P1_Incidents}")
P1_count = P1_Incidents.count('P1')
print(f"\nP1 Count: {(P1_count)}")

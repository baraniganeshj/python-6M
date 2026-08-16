Network_Alerts = ["INFO", "HIGH", "CRITICAL", "HIGH", "INFO", "CRITICAL"]
Server_Alerts = ["HIGH", "HIGH", "INFO", "INFO", "WARNING"]
Security_Alerts = ["CRITICAL", "CRITICAL", "HIGH", "CRITICAL", "HIGH"]

def count_high_severity_alerts(alerts_list):
    high_severity_count = 0
    for alert in alerts_list:
        if alert == "HIGH" or alert == "CRITICAL":
            high_severity_count += 1
    return high_severity_count

network_count = count_high_severity_alerts(Network_Alerts)
server_count = count_high_severity_alerts(Server_Alerts)
security_count = count_high_severity_alerts(Security_Alerts)

print(f"Network Alerts: High Severity Alerts: {network_count}")
print(f"Server Alerts: High Severity Alerts: {server_count}")
print(f"Security Alerts: High Severity Alerts: {security_count}")

if network_count in [0, 1, 2]:
    print(f"Network Alerts: {network_count} NORMAL")
elif network_count in [3, 4]:
    print(f"Network Alerts: {network_count} ATTENTION")
elif network_count >= 5:
    print(f"Network Alerts: {network_count} CRITICAL")

if server_count in [0, 1, 2]:
    print(f"Server Alerts: {server_count} NORMAL")
elif server_count in [3, 4]:
    print(f"Server Alerts: {server_count} ATTENTION")
elif server_count >= 5:
    print(f"Server Alerts: {server_count} CRITICAL")

if security_count in [0, 1, 2]:
    print(f"Security Alerts: {security_count} NORMAL")
elif security_count in [3, 4]:
    print(f"Security Alerts: {security_count} ATTENTION")
elif security_count >= 5:
    print(f"Security Alerts: {security_count} CRITICAL")
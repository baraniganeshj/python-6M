print("=" * 50)
print("DEVICE STATUS CHECK")
print("=" * 50)
print()

def check_device_status(device, status):
    if status == "DOWN":
        print(f"{device} : {status} - ALERT")
    else:
        print(f"{device} : {status} - OK")

check_device_status("Router-1", "UP")
check_device_status("Switch-1", "DOWN")
check_device_status("Firewall-1", "UP")

check_device_status("Server-1", "DOWN")

print()

def get_device_message(device):
    return f"Checking {device}"

router_1 = get_device_message("Router-1")
switch_1 = get_device_message("Switch-1")

print(router_1)
print(switch_1)

print()



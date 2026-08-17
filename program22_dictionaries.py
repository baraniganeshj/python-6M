device = {
   "Name" :"Chennai-RTR-1",
    "IP" : "10.10.10.1",
    "Status" : "UP",
    "CPU" : 55,
    "Memory" : 60 
}

print(f"Name: {device['Name']}")
print(f"IP: {device['IP']}")
print(f"Status: {device['Status']}")
print(f"CPU: {device['CPU']}%")
print(f"Memory: {device['Memory']}%")

device["CPU"] = 72
print(f"Updated CPU: {device['CPU']}")

device["Location"] = "Chennai DC"
print(f"Location: {device['Location']}")

print(device)
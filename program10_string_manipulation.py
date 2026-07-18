log1 = ("router-1 interface down")

print(f"Original Log: {log1}")
print()   
print(f"Uppercase Log: \n{log1.upper()}")
print()
print(f"Lowercase Log: \n{log1.lower()}")
print()
print(f"Replaced Log: \n{log1.replace('down', 'up')}")
print()

log2 = ("CRITICAL ROUTER-1 DOWN")

words = log2.split()

for word in words:
    print(word)
print()
log3 = ("Vendor ticket opened for ATT circuit outage")

print(f"Original: \n{log3}")
print()
print(f"Upper: \n{log3.upper()}")
new_log3 = log3.replace("ATT", "AT&T")
print()
print(f"Updated: \n{new_log3}")
print()
texts = new_log3.split()
print("Words:")
for text in texts:
    print(text)




name = input("Enter your Name: ")
hours_worked = int(input("Enter Hours Worked: "))
assigned_tickets = int(input("Enter Assigned Tickets: "))
tickets_closed = int(input("Enter Tickets Closed: "))


average_tickets = tickets_closed / hours_worked
remaining_tickets = assigned_tickets - tickets_closed

print(f"Shift Summary for {name}")
print(f"Hours Worked: {hours_worked}")
print(f"Assigned Tickets: {assigned_tickets}")
print(f"Tickets Closed: {tickets_closed}")
print(f"Remaining Tickets: {remaining_tickets}")
print(f"Average Tickets Per Hour: {average_tickets}")




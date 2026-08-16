def calculate_uptime(Total_Minutes, Downtime_Minutes):
    uptime_percentage = ((Total_Minutes - Downtime_Minutes) / Total_Minutes) * 100
    return uptime_percentage

chennai_DC_Total_Minutes = 10080
chennai_DC_Downtime_Minutes = 300

bangalore_DC_Total_Minutes = 10080
bangalore_DC_Downtime_Minutes = 120

hyderabad_DC_Total_Minutes = 10080
hyderabad_DC_Downtime_Minutes = 45

chennai_uptime = calculate_uptime(chennai_DC_Total_Minutes, chennai_DC_Downtime_Minutes)
bangalore_uptime = calculate_uptime(bangalore_DC_Total_Minutes, bangalore_DC_Downtime_Minutes)
hyderabad_uptime = calculate_uptime(hyderabad_DC_Total_Minutes, hyderabad_DC_Downtime_Minutes)

if chennai_uptime >= 99:
    print(f"Chennai DC Uptime: {chennai_uptime:.2f}% - HEALTHY")
else:
    print(f"Chennai DC Uptime: {chennai_uptime:.2f}% - ATTENTION")

if bangalore_uptime >= 99:
    print(f"Bangalore DC Uptime: {bangalore_uptime:.2f}% - HEALTHY")
else:
    print(f"Bangalore DC Uptime: {bangalore_uptime:.2f}% - ATTENTION")

if hyderabad_uptime >= 99:
    print(f"Hyderabad DC Uptime: {hyderabad_uptime:.2f}% - HEALTHY")
else:
    print(f"Hyderabad DC Uptime: {hyderabad_uptime:.2f}% - ATTENTION")


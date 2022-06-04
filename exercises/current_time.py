import time as t

gmt = int(input("Enter your time zone GMT"))

total_seconds = int(t.time())
current_second = total_seconds % 60
total_minutes = total_seconds // 60
current_minutes = total_minutes % 60
total_hours = total_minutes // 60
current_hour = (total_hours + gmt) % 24

# print(current_hour, ":", current_minutes, ":", current_second)

print(f"{current_hour}:{current_minutes}:{current_second}")
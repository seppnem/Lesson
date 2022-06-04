seconds = int(input("enter number of seconds"))

days = seconds // (60*60*24)
hours = seconds // (60*60)
months = seconds // (24*30*3600)

print(days,":" , hours , ":" , months , ":" , seconds)
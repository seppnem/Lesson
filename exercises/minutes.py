minutes = int(input("enter the number of minutes"))

days = (minutes // (24*60))//365

year = minutes // 365

print(minutes,"is approximately",year,"years and",days,"days")
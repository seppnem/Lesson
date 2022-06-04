water=int(input("enter the amount of water in kilograms "))
temperature=int(input("enter the initial temperature"))
final_temp=int(input("enter the final temperature"))


Q = water * (final_temp - temperature) * 4184

print("the energy is needed is",Q)


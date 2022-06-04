import random as x

lottery_number = x.randrange(100,1000)
lottery = lottery_number
user_number = int(input("enter a 3 digit number"))
user = user_number

print(lottery_number)
l1 = lottery % 10
lottery = lottery // 10

l2 = lottery % 10
lottery = lottery // 10

l3 = lottery % 10

u1 = user % 10
user = user // 10

u2 = user % 10
user = user // 10

u3 = user % 10

if user_number == lottery_number:
    print("you won 10000 dollars")
elif (l1 == u1 or l1 == u2 or l1 == u3) and (l2==u1 or l2==u2 or l2==u3) and (l3==u1 or l3==u2 or l3==u3):
    print("you won 3000 dollars")
elif (l1 == u1 or l1 == u2 or l1 == u3) or (l2==u1 or l2==u2 or l2==u3) or (l3==u1 or l3==u2 or l3==u3):
    print("you won 1000 dollars")

else:
    print("you owe 10000 dollars to me")

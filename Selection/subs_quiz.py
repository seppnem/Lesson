import random as r

MIN_LIMIT = 0
MAX_LIMIT = 100

number1 = r.randint(MIN_LIMIT, MAX_LIMIT)
number2 = r.randint(MIN_LIMIT, MAX_LIMIT)

if number2 < number1:
    """temp = number2
    number2 = number1
    number1 = temp"""
    number2, number1 = number1, number2  # swap

x = int(input(f"{number2}-{number1}="))

if x == number2 - number1:
    print("correct")
else:
    print("wrong")
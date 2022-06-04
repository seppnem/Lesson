import random as r

MIN_LIMIT = 0
MAX_LIMIT = 100
QUESTION_COUNT = 5
i = 0

while i < QUESTION_COUNT:
    number1 = r.randint(MIN_LIMIT, MAX_LIMIT)
    number2 = r.randint(MIN_LIMIT, MAX_LIMIT)

    if number2 < number1:
        """temp = number2
        number2 = number1
        number1 = temp"""
        number2, number1 = number1, number2  # swap

    x = int(input(f"{number2}-{number1}="))

    while x != number2 - number1:
        print("wrong")
        x = int(input(f"{number2}-{number1}="))

    print("correct")


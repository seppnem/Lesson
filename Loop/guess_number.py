import random

magic_number = random.randint(0, 100)

guess_number = int(input("Guess"))

while guess_number != magic_number:
    if guess_number > magic_number:
        print("Too high")
    else:
        print("Too low")
    guess_number = int(input("Guess"))

print("Correct")


number = int(input("Enter a number"))

maximum = -1
while number >= 0:
    if number > maximum:
        maximum = number

    number = int(input("Enter a number"))

print(maximum)
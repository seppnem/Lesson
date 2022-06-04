number = int(input("Enter three digit number"))

d1 = number % 10
number2 = number // 10
d2 = number2 % 10
number3 = number2 // 10
d3 = number3 % 10

print(number, "digits -> ", d1, d2, d3, "Mul -> ", d1 * d2 * d3)



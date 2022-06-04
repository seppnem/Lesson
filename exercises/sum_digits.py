x = int(input("enter a number between 0 and 1000"))

a = x % 10
number1 = x // 10

b = number1 % 10
number2 = number1 // 10

c= number2 % 10

print("The sum of the digits is",a+b+c)





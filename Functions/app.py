#import Functions.calculator

#print(Functions.calculator.add(5, 3))


#import  Functions.calculator as c
#print(c.add(5, 6))

"""
from Functions.calculator import add, sub, div
import Functions.calc as fc
print(fc.add(8, 9))
print(add(5, 9))
"""



from Functions.calculator import add, sub, div, mul

def main():
    while True:
        a = int(input("Number 1"))
        ops = input("Enter ops")
        b = int(input("Number 2"))

        result = 0
        if ops == "+":
            result = add(a, b)
        elif ops == "-":
            result = sub(a, b)
        elif ops == "*":
            result = mul(a, b)
        elif ops == "/":
            result = div(a, b)
        else:
            result = None

        if result == None:
            print("Invalid operator")
        else:
            print(a, ops, b, " = ", result)

        flag = True
        while flag == True:
            is_continue = input("Do you want to cont.[Y - N ]")

            if is_continue == "N":
                flag = False
            elif is_continue == "Y":
                break # while True inner while
            else:
                flag = True

        if flag == False:
            break  # ends while True: outer loop






main()
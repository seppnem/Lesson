import random as r

r.randint(20, 30)

#global scope
x = 10

def func():
    #func scope
    print(x)
    y = 20

#print(y)
func()

x = 30

func()




z = 40
def foo():
    global z
    z = 20

foo()
print(z)









#global scope

def foo():
    #func scope
    x = 10
    print()

class Person:
    def __init__(self, name="Havva", age=2005): #n="Adam", a=1757):
        #attribute
        self.name = name
        self.age = age

    def getAge(self):
        return self.age

    @staticmethod
    def foo():
        pass

p = Person()
p.getAge()
p1 = Person("Onur", 18)
p1.getAge()   # getAge(p1)

Person.foo()

class Circle:
    #class scope
    ###state
    def __init__(self, r):  # Circle(self, 5.7)
        self.radius = r   #attribute, instance variable, data field


    ##behaivour
    def getArea(self):
        return 3.14 * self.radius ** 2

    def getPerimeter(self):
        return 2 * self.radius * 3.14

def displayCircleArea(circle):
    print(circle.getArea())

#global scope
def main():


    c1 = Circle(5.7)
    displayCircleArea(c1)

    print(c1.getArea())
    c1.radius = 10
    print(c1.getArea())
    c1.getPerimeter()

    a = Person()
    onur = Person("onur", 18)

    c2 = Circle(5)
    print(c2.getArea())


main()
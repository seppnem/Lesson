class Animal:
    def __init__(self, age, fc):
        assert isinstance(fc, int)
        assert isinstance(age, int)

        self._age = age   #protected
        self._footCount = fc

    def makeSound(self):
        print("Animal sound")


class Cat(Animal):
    def __init__(self, age, fc, color):
        #super(Cat, self).__init__()
        super().__init__(age, fc)
        self.__color = color
    #override s aniamal makeSound
    def makeSound(self):
        print("miyav")

    def getAge(self):
        return self._age

    # object sınıfının __str__ methodunu override ediyorum
    def __str__(self):
        return "Cat -> " + "my age is " + str(self._age) + "Foot count " + str(self._footCount) + "Color " + self.__color



class Dog(Animal):
    def __init__(self, age, fc):
        super().__init__(age, fc)

    def makeSound(self):
        print("hav hav")

def main():
    a1 = Cat(5, 4, "white")
    a2 = Cat(3, 4, "orange")
    d1 = Dog(7, 4)

    farm = [a1, a2, d1]

    for animal in farm:
        animal.makeSound()

    for animal in farm:
        print(animal)

    #print(isinstance(a1, Cat))
    #print(isinstance(a1, Animal))

if __name__ == '__main__':
    main()
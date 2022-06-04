class Person:
    def __init__(self, name):
        self.__name = name


    def __add__(self, other):
        if not isinstance(other, Person):
            raise TypeError("person must be person instance")
        newName = self.__name + "\n" + other.__name
        newPerson = Person(newName)
        return newPerson

    def __lt__(self, other):
        return self.__name < other.__name

    #override
    def __str__(self):
        return self.__name

    def __repr__(self):
        return self.__name

    def foo(self):
        pass




def main():
    p = Person("Ali")
    p1 = Person("Veli")
    p2 = Person("Zeynep")

    personList = [p2, p, p1]

    print(sorted(personList))

    #p2 = 2 + p
    #p2 = p + 2
    #p2 = p + p1
    #p2 = p.__add__(p1)

    #print(p2)


main()
class Employee :  # TODO: abstract
    count=100
    def __init__(self,name,salary,title):
        #TODO: encapsulate attribute
        self._name=name
        self.salary=salary
        self.title=title
        self.__id = Employee.count
        Employee.count += 1

    def numberofemployees (self):
        print("the total number of employes are :",self.count)

    def setname (self, name):
        self.name=name
    def getname (self):
        return self.name
    def setsalary (self, salary):
        self.salary=salary
    def getsalary (self):
        return self.salary
    def setttitle (self,title):
        self.title=title
    def gettitle (self):
        return self.title

    #TODO: abstract raiseSalary()

class Developer(Employee):
    def __init__(self,name,salary,title,workinghours):
        self.workinghours=workinghours



class Sales:
    pass


class Manager:
    pass


class Company:

    employeeList =[]

    addEmployee()
    removeEmployee()
    raiseSalary


class App:
    company = Company("")


    #menu 1 add Employee
    #menu 2 remove




# Is- A, Has-A, Objects, and Classes

## Animal is-a object

class Animal(object):
    pass

## Dog is-a Animal
class Dog(Animal):

    def __init__(self, name):
        ## Dog has-a name
        self.name = name

## Cat is-a Animal
class Cat(Animal):

    def __init__(self, name):
        ## Cat has-a name
        self.name = name

## Person is-a Object
class Person(object): # in Python 3, you do not need to add object but "Explicit is better than implicit"

    def __init__(self, name):
        ## Person has-a name
        self.name = name

        ## Person has-a pet
        self.per == None

## Employee is-a Person
class Employee(Person):

    def __init__(self, name, salary):
        ## You can run the __init__ method of a parent class reliably.
        super(Employee, self).__init__(name) # In Python 3, super().__init__()
        ## Employee has-a salary
        self.salary = salary

## Fish is-a object
class Fish(object):
    pass

## Salmon is-a Fish
class Salmon():
    pass

## Halibut is-a Fish
class Halibut(Fish):
    pass

## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

## mary has a pet
mary.pet = satan

## frank is-a Employee
frank = Employee("Frank", 120000)

## frank has-a pet
frank.pet = rover

## filpper is-a Fish
filipper = Fish()

## crouse is-a Salmon
crouse = Salmon()

## harry is-a Halibut
harry = Halibut()

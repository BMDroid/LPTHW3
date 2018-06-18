# Using super() with __init__

class Parent(object):

    def __init__(self):
        print("This is the initialization for the Parent class.")

class Child(Parent):

    def __init__(self, stuff):
        self.stuff = stuff
        super(Child, self).__init__()
        print("This is the stuff in the Child: ", self.stuff)

dad = Parent()
son = Child('stuff')

# Inheritance versus composition
# Inheritance is used to indicate that one class will get most or all of its features from a parent classself.
# 1. Actions on the child imply an action on the parent.
# 2. Actions on the child override the action on the parent.
# 3. Actions on the child alter the action on the parent.

# Implicit Inheritance

class Parent(object):

    def implicit(self):
        print("PARENT  implicit()")

class Child(Parent):
    # It will inherit all of its behavior from the Parent.
    pass

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

# Override Explicitly

class Parent_b(object):

    def override(self):
        print("PARENT override()")

class Child_b(Parent_b):

    def override(self):
        print("CHILD override()")

dad = Parent_b()
son =  Child_b()

dad.override()
son.override()

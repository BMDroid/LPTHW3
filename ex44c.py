class Parent_c(object):

    def altered(self):
        print("PARENT altered()")

class Child_c(Parent_c):

    def altered(self):
        print("CHILD, BEFORE PARENT altered()") # This is the override part
        super(Child_c, self). altered() # altered() in the Parent being called
        print("CHILD, AFTER PARENT altered()")

dad = Parent_c()
son = Child_c()

dad.altered()
son.altered()

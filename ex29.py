# What if

people = 20
cats = 30
dogs = 15

if people < cats: # the colon will tell the Python you are going to create a new "block" of code.
    print("Too many cats! The world is doomed!") # And the indent will tell the Python what lines of the code are in the block.

if people > cats:
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")

if people > dogs:
    print("The world is dry!")

dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs:
    print("People are less than or equal to dogs.")

if people == dogs:
    print("People are dogs.")

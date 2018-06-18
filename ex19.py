# The variables in the function are not connected to the variables in the script.
# The variables in the script are seperate and live outside of the functionself.
# They are then passed to the function, and the temporary versions are made just for the function's run.
# When the function exists these temporary variables go away and everything keeps working.

def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of the crackers!")
    print(f"Man that's enough for a party!")
    print("Get a blanket. \n")

print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

print("OR, we can use variables from our script:")
amount_of_cheese =  10 # global variables
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can even do manth inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

print(f"""
These are the variables in the script in the end:
amount_of_cheese: {amount_of_cheese}
amount_of_crackers: {amount_of_crackers}
""")

if amount_of_cheese == 10 and amount_of_crackers == 50:
    print("The variables have not been alterd by the function.\n")
else:
    print("The variables have been alterd by the function.\n")

# Try to use user input in a function

def user_input():
    print("Please input two integers:")
    a = int(input("> ")) # int() parse the integer from the string
    b = int(input("> "))
    print(f"This is the sum of two integers: {a + b}")

user_input()

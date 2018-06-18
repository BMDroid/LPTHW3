# Names, Variables, Code, Functions
# Functions do three things
# 1. name pieces of code the way variables name strings and numbers
# 2. take arguments the way scripts take argv
# 3. let you make you own "mini-scripts" or "tiny commands"

# this one is like scripts with argv
def print_two(*args): # the * put all the args in a list
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}") # we skip the unpacking arguments and just use the name we want right inside ()

# this just takes one argument
def print_one(arg1):
    print(f"arg1: {arg1}")

# this takes no arguments
def print_none():
    print("I got nothing.")

print_two("Jianyuan", "Bo")
print_two_again("Jianyuan", "Bo")
print_one("First!")
print_none()

# this is the checklist for the Functions
# 1. start your definition with def
# 2. function name can only contains characters and underscore and cannot start with the numbers just like the naming of the varaibles
# 3. put the close parenthesis
# 4. put the argumets in the parenthesis
# 5. each argument has an unique name
# 6. put a close parenthesis and a colon after the arguments
# 7. indent all the lines of code in the function four spaces
# 8. end the function by going back to writing with no indent

# this is the checklist for running the function
# 1. call the function name
# 2. put a close parenthesis with the arguments seperated with comma in it

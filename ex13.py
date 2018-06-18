# this exercise woll make the script also accept the arguments
from sys import argv # argv is the "argument variable", this variable holds the arguments you pass to the python
# read the WYSS section for how to run this
script, first, second, third = argv # unpack the arguments

print("The script is called:", script)
print("Your first variable is:", first)
print("Your sencond variable is:", second)
print("Your third variable is:", third)

# the arguments counts from the first argument after the python conmmand
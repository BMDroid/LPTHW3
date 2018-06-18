# Functions Can Return Something

def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b

print("Let's do some math with just functions!")

age = add(20, 6)
height = subtract(180, 2)
weight =  multiply(45, 2)
iq = divide(240, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

# A puzzle for the extra credit
print("Here is a puzzle")

what = add(age, subtract(height, multiply(weight, divide(iq, 2)))) # python can take the return value of the function as parameter of another function

print("That becomes: ", what, "Can you do it by hand?")

if what == 26 + (178 - (90 * (120 / 2))):
    print("Your answer is right! You prove that you can do this by hand.")
else:
    print("Your answer is wrong.")

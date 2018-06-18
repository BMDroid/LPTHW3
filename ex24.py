print("Let's practice everything.")
print('You\'d need to know \'bout escapes with \\ that do:')
print('\n newlines and \t tabs.')

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \nthe needs of lovely
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print("-------------")
print(poem)
print("-------------")

five = 10 - 2 + 3 - 6
print(f"This should be five: {five}")

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates # function can return several values

start_point = 10000
beans, jars, crates = secret_formula(start_point)

# remeber that this is another way to format a strings
print("With a starting poin t of {}". format(start_point)) # .format()

# it's just like with an f"" strings
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point / 10

print("We can also do that this way:")
formula = secret_formula(start_point)
# this is an easy way to apply a list to a format string
print("We'd have {} beans, {} jars, and {} crates.".format(*formula)) # the asterisk is used for unpacking the container

# test the suage of the asterisk
print(formula) # this print the list as (500000.0, 500.0, 5.0)
print(*formula) # this print 500000.0 500.0 5.0

# test the unpacking again
def test_unpacking(a, b, c):
    return a + b + c

test_result = test_unpacking(*formula)
print(test_result) # the unpacking return each elemts in the container as the type they are which is the integer here

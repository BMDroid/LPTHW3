# Loops and Lists
# for-Loops
# lists: start the list with the left bracket [, then you put each item you wnat in the list separated by commas, then end the list with a ] right bracket.

the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quaters' ]

# this first kind of for-loop foes through a lists
for number in the_count: # the variable is defined by the for-loop when it starts, initializing it to the current element of the loop iteration
    print(f"This is count {number}")

# same as above
for fruit in fruits:
    print(f"A fruit of type: {fruit}")

# also we can go through mixed lists too
# notice we have to use {} since we don't know what's in it
for i in change:
    print(f"I got {i}")

# we can also build lists, first start with an empty one
elements = [] # create a empty list

# then use the range function to do 0 to 5 counts
for i in range(0, 6): # range() generates a list of integers not including the last
    print(f"Adding {i} to the list.")
    # append is a function that lists Understand
    elements.append(i) # append the i to the list

# now we can print them out too
for i in elements:
    print(f"Element was: {i}")

# assign the range(0, 6) directly to the lists
elements_assign = [*range(0, 6)] # rang() could be unpack which means it is some kind of list
list_format = "{}, " * 6
list_format = list_format[:-2] # remove the last white space and the comma from the list_format
print("This is the elements from the lists:", list_format.format(*elements_assign))

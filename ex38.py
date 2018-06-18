# Doing things to the lists
# Python change the function call with twop arguments,  list.appenf('a') becoomes append(list, 'a')

ten_things =  "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(' ') # split the string with ' ' and return as a list
more_stuff = ["Days", "Night", "Song", "Firebee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop() # pop() without any argument then remove the last one and return its value
    print("Adding:", next_one)
    stuff.append(next_one) # append the variable to the end of the list
    print(f"There are {len(stuff)} items now.")

print("There we go:", stuff)

print("Let's fo somoe thingd with stuff.")

print(stuff[1]) # print the 2nd elements of the sutff with 0-base index
print(stuff[-1]) # print the last element
print(stuff.pop()) # print the last element and remove it
print(' '.join(stuff)) # print out the list with certain format
print('#'.join(stuff[3:5])) # stuff[a:b] is the sublist of the stuff and it contains the (b-a) elements starting from a

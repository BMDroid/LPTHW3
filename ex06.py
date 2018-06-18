tyes_of_people = 10
x = f"There are {tyes_of_people} types of people." # f-string

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}." # f-string


print(x)
print(y)

print(f"I said: {x}") # f-string
print(f"I also said: '{y}'") # f-string

hilarous = False
joke_evaluation = "Isn't that joke so funny?! {}" # why thers is an empty {} in the string

print(joke_evaluation.format(hilarous)) # usaually use that sometimes when apply a format to an already created string, such as in a loop

w = "This is the left side of..."
e = "a string with a right side."
a = w + e
b = w + f"{3}"

print(w + e)
print(a)
print(b)
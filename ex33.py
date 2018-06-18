# While Loop: keep executing the code block under it as long as a boolean expression is True.

i = 0
numbers = []

while i < 6:
    print(f"At the top i is {i}")
    numbers.append(i)

    i += 1
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i}")

print("The numbers: ")

for num in numbers:
    print(num)

def append_nums(list, nums, step):
    """This function will append 0 to nums with step to the list"""
    if nums * step <= 0 or nums <= 0 or step <= 0:
        print("The parameters should be all be positive integers.")
        return list
    i = 0
    while i < nums:
        list.append(i)
        i += step
    return list

print(f"Please enter a list separated with the white space:")
list_str = input("> ")
list = list_str.split(" ")

print("Please enter the how many numbers you want to add to the list start from O:")
nums = int(input("> "))

print("Please enter the step between each integer: ")
step = int(input("> "))

print(f"This is the list after the operation {append_nums(list, nums, step)}")

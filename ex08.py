formatter = "{} {} {} {}" # this is a string

print(formatter.format(1, 2, 3, 4)) # call a fuction 'format()' which turn variables into a string with the format of the string variable formatter defined at the first line
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))
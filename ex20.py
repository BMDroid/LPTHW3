# Functions and files

from sys import argv

script, input_file = argv

def print_all(f):
    print(f.read())

def rewind(f): # seek() function is dealing with the bytes not lines. seek(0) move the file to the 0 byte(first byte) in the file.
    f.seek(0)# after read the file, the cursor will located at the end of the file. If we now print the file, we will only get an empty line.

def print_a_line(line_count, f):
    print(line_count, f.readline(), end = "") # readline() will read one line from the currnt cursor and then move the cursor to the next line

current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

current_line = 1
print_a_line(current_line, current_file)

current_line += 1;
print_a_line(current_line, current_file)

current_line += 1;
print_a_line(current_line, current_file)

# rewrite the print line by line of the file using for
print("Now let's print all the lines using for loop.\n")
rewind(current_file) # if we do not rewind the file, the for loop will start from the cursor left by the operations above
current_line = 1;
for line in current_file:
    print(f"Line No.{current_line}:  {line}", end = "") # the end = "" avoid double \n to every line
    current_line += 1

# write the function to print every line in the file
def print_lines(f):
    rewind(f)
    current_line = 1
    for line in f:
        print(f"Line No.{current_line}:  {line}", end = "")
        current_line += 1

print("Now, print the file line by line using function.\n")
print_lines(current_file)

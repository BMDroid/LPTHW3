# close - close the files
# read -  read the contents of the files
# readline - reads just one line
# truncate - empties the file
# write('stuff') - writes "stuff" to the file, takes a paranmeter of a string you want to write to the file
# seek(0) - move the read/write location to the beginning of the file

from sys import argv

script, filename =  argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that,hit RETURN.")

input("?")

print("Opening the file...")
#target = open(filename, 'w') # 'w' means going to open the file in 'write' mode, the default mode of the 'open()' function is going to open the file in the 'read' mode
target = open(filename, 'w+') # open the file in read and write mode

print("Truncating the file. Goodbye!")
target.truncate()
print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("Now I'm going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print(f"Let's show what's in the {filename} now.")
target.seek(0) # IMPORNTANT: return to the beginning of the file, or yo will just read an empty string
print(target.read())

print("And finally, we close it.")
target.close()

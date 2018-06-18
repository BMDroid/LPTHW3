# this ex is to write a script to copy one file to another

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

# we could do these two on one line, how?
in_file = open(from_file)
indata = in_file.read()

# indata = open(from_file).read() # this could work

print(f"The input file is {len(indata)} bytes long")

print(f"Does the output file exist? {exists(to_file)}") # the 'exists()' will return True if the file exists, based on its name in a string as an argument
print("Ready, hit RETURN to continue, CRTL-C to abort.")
input("> ")

out_file = open(to_file, 'w+')
out_file.write(indata)

print("Alright, all done.")

print(f"Let's show the {to_file}: \n ")
out_file.seek(0) # this is move to the beginning of the file
print(out_file.read())

out_file.close() # a close file cannot be written anymore
in_file.close()

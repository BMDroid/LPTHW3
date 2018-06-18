# avoid the hard coding and learn to read files
from sys import argv

script, fileName = argv

txt = open(fileName) # txt is the file object, it does not return the file content

print(f"Here's your file {fileName}:")
print(txt.read()) # the read() keeps the format of the file comtent
txt.close() # close the file when youn are done with it

print("Type the filename again:")
file_again =  input("> ")

txt_again = open(file_again)

print(txt_again.read())
txt_again.close()

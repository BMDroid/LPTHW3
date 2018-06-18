# String, Bytes and Character Encodings
# 1. How modern computers store human languages for display and processing and how Python 3 call this strings
# 2. How you must encode and decode Python's strings into a typed called Bytes
# 3. How to handle errors in your string and byte handling
# 4. How to read code and find out that it means even if you have never seen it before

import sys
script, input_encoding, error = sys.argv

def main(language_file, encoding, errors):
    line = language_file.readline() # read one line fron the file it is given

    if line: # check EOF
        print_line(line, encoding, errors)
        return main(languafe_file, encoding, errors) # a function that call itself

def print_line(line, encoding, errors):
    # string.strip(chars), return a copy of string with the leading and trailing Character chars removed. If the char is none or omitted, the white space in the string will be removed.
    # If given and not None, chars must be a string; the characters in the string will be stripped from the both ends of the string this method is called on.
    next_lang = line.strip() # trailing the \n on the line string
    raw_bytes = next_lang.encode(encoding, errors=errors)# encoding is the codec in Python
    cooked_string =  raw_bytes.decode(encoding, errors=errors)

    print(raw_bytes, "<===>", cooked_string)

languages = open("languages.txt", encoding = 'utf-8')

main(languages, input_encoding, error)

# This is the test for the (if line:) in the print_line()
test_file = open("test.txt")
line_number = 0
current_line = test_file.readline()
while current_line: # even if the current line is white space, the only false will occur when current_line == ""
    line_number += 1
    current_line = test_file.readline()
if_line = line_number

test_file.seek(0)
line_number = 0
for line in test_file:
    line_number += 1
for_line = line_number

print(f"if_line = {if_line}, for_line = {for_line}")
if if_line == for_line:
    print(if_line == for_line)
    print("The \'if line:\' will check the existability of the current line.")

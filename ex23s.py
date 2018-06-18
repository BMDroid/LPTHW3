import io

test_str = '''1st line
2nd line
3rd line
'''
print(f"The following are the content of the test string: \n{test_str}")

def print_line(line_number, buf):
    print(f"You want to print the No. {line_number} line.")
    num = 0
    line = ""
    while num < line_number:
        line = buf.readline() # this read the line of the test_str
        num += 1
    if line == "":
        print("The line you wanted does not exit.")
    else:
        print(line)

buf = io.StringIO(test_str)
line_number = int(input("Which line of the test string do you want to print?\nPlease enter the line number: "))
print_line(line_number, buf)

buf = open("test.txt")
line_number = int(input("Which line of the test file do you want to print?\nPlease enter the line number: "))
print_line(line_number, buf)

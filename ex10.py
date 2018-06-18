tabby_cat ="\tI'm tabbed." # tabbed the line
persian_cat = "I'm split\non a line." # create a new line
blacklash_cat = "I'm \\ a \\ cat." # \ can be used to escape certain characters 
x = "I \"understand\" joe." # escape the double-quote insede string
y = "\"I Love you\""
z = f"I said to my baby: {y} everyday."

fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''# \ will only escape the first character, and the triple double-quotes works the same as the triple single-quote

print(tabby_cat)
print(persian_cat)
print(blacklash_cat)
print(fat_cat)
#print(x)
print(z)

escape_sequence = """
\\\ \t\tBlacklash(\\)
\\' \t\tSingle-quote(\')
\\" \t\tDouble-quotes(\")
\\a \t\tASCII bel(BEL)
\\b \t\tASCII backspace(BS)
\\f \t\tASCII formfeed(FF)
\\n \t\tASCII linefeed(LF)
\\N{name} \tCharacter named name in the Unicode database(Unicod only)
\\r \t\tCarriage Return(CR)
\\t \t\tHorrizontal Tab(TAB)
\\uxxxx \t\tCharacter with 16-bit hex value xxxx
\\Uxxxxxxxx \tCharacter with 32-bit hex value xxxxxxxx
\\v \t\tASCII vertical tab (VT)
\\ooo \t\tCharacter with octal value ooo
\\xhh \t\tChatacter with hex value hh
"""
print("Escape Sequence:\n" + escape_sequence)

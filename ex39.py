# Dictionaries
# Just like a database for storing and organizing database

def list_ex():
    """List can only use number to access the data"""
    things = ['a', 'b', 'c', 'd']
    print(things)
    print(f"This is the 2nd element of the list: {things[1]}")

def dict_ex():
    stuff = {'name':'Jianyuan', 'age':26, 'height':178}
    print(f"This is the dictionary: {stuff}")
    print(stuff['name'])
    print(stuff['age'])

    stuff['city'] = "HF"
    print(stuff['city'])

    stuff[1] = "Wow" # number could also be used as keys
    stuff[2] = "Nice"
    print(stuff)

    del stuff['city'] # can also delete the element in the dictionary
    del stuff[1]

list_ex()
dict_ex()

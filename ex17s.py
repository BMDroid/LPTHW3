# this is for the stusy drills to make the ex17.py as short as possible

from sys import argv

open(argv[2], 'w+').write((open(argv[1]).read()))

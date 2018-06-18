from random import randint
from sys import exit
from room import Room

class Death(Room):

    quips = [
        "You died. You kinda suck at this.",
        "Your Mom would be proud...if she were smarter.",
        "Such a luser.",
        "I have a small puppy that's better at this.",
        "You're worse than your Dad's jokes."
        ]

    def __init__(self):
        self.info = {'current_room': '', 'next_room': 'None'}
        super().__init__('death')

    def enter_room(self):
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)

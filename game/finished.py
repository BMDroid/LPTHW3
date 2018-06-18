from textwrap import dedent
from random import randint
from room import Room

class Finished(Room):

    def __init__(self):
        self.info = {'current_room': '', 'next_room': 'None'}
        super().__init__('finished')

    def enter_room(self):
        print(dedent("""
            This is the last part of this game. Here you stand in front of a huge door.
            The foor is red, super RED!
            You walk closer and you smell the blood. Besides, you can see the light behind the door
            through the lock. It is a huge lock. If you want to get out, you need to decode the lock first.
            The only thing you know is that: you need to enter a 3 digits number to open the lock. The pin is unique.
            And you only have 5 chances to decode it.
            Let's begin.
            """))

        pin_str = f"{randint(0, 9)}{randint(0, 9)}{randint(0, 9)}"
        chances = 5

        while chances >= 1 :
            if chances <= 2:
                print(f"You have only {chances} chances left.")
                self.hint_switch(pin_str)

            depin = input("> ")

            if depin != pin_str:
                print("You are wrong!")
                chances -= 1
            else:
                print(dedent("""
                You are very smart. You open the lock!
                You win!
                """))
                exit(1)

        self.info['next_room'] = 'death'

    def hint_switch(self, pin_str):
        print(f"Do you want some hint?")
        hint_switch = input("yes or no? > ")
        if hint_switch == 'yes':
            random_location = randint(0, 2)
            print(f"The pin contain number {pin_str[random_location: random_location + 1]}.")
        else:
            print("Seems you are a little bit stubborn.\nThen good luck!")

from textwrap import dedent
from room import Room

class Start(Room):

    def __init__(self):
        self.actions = ['yes', 'no', 'hint']
        self.info = {'current_room': '', 'next_room': 'None'}
        super().__init__('start')

    def enter_room(self):
        print(dedent("""
        You enter the forest and this is the start of this game.
        The forest is full of black trees, no any other color could be seen.
        You hear the voice of a little girl. You cannot see her. But her voice
        is whisperd into your ears: "Please help me. Please!"
        Do you want to enter the forest?
        """))

        again = True

        while again == True:
            action = input("> ")

            if action == self.actions[0]:
                print(dedent("""
                You are a brave young man. You have the heart of a chevalier.
                But you are too brave to play this game. Sorry. XD
                """))
                self.info['next_room'] = 'death'
                again = False

            elif action == self.actions[1]:
                print(dedent("""
                Haha, you are tricked. This room has another name: The No Room!
                You are the perfect one for this interesting game!
                A tornado suddenly appears right on your face. You are carried by the tornado
                and officially enter the forest!
                """))
                self.info['next_room'] = 'finished'
                again = False

            elif action == self.actions[2]:
                print(f"Here si the hints for you.\nYou can choose between \'{self.actions[0]}\' and \'{self.actions[1]}\'.\nBe carful for what you choose!")

            else:
                print("Your answer cannnot handled by the game!\nStart Over!!!")


# test = Start()
# test.enter()
# next_room = test.exit()
# print(next_room)

# Branches and Functions

from sys import exit

def gold_room():
    print("This room is full of gold. How much do you take?")

    numbers = "0123456789"
    choice = input("> ")

    if all(i in numbers for i in choice): # any() and all() take iterables and return True if any and all of the elements are True.
    #if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print("Nice, you are not greedy, you win!")
        exit(0) # 0 is exit code and exit(0) means clean exit without errors
    else:
        dead("You greedy bastard!")

def bear_room():
    print("There is a bear here.\nThe bear has a bunch of honey.\nThe fat bear is in front of another door.\nHow are you going to move the bear?")
    bear_moved = False

    while True:
        choice =  input("> ")

        if choice == "take honey":
            dead("The bear looks at you then slaps you face off.")
        elif choice == "taunt bear" and not bear_moved:
            print("The bear has moved from the door.")
            print("You go through it now.")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("the bear gets pissed off and chews your legs off.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means.")

def  cthulhu_room():
    print("Here you see the great evil Cthulu.\nHe, it, whatever stare at you and you go insane.\nDo you flee for your life of eat your head?")
    choice =  input("> ")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty!")
    else:
        cthulhu_room()

def dead(why):
    print(why, "Good job!")
    exit(0)

def start():
    print("You are in a dark room.\nThere is a door to your right and left.\nWhich one do you take?")
    choice = input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")

start()

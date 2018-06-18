# The code for "Gothons from Planet Percal #25"

from sys import exit
from random import randint
from textwrap import dedent

class Scene(object):
    """This is a just demonstration of simple class"""

    def enter(self):
        print("This scene is not yet configured.")
        print("Subclass it and implement enter()")
        exit(1)


class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        """This function will keep the game playing unless the next_scene_name == \'finished\'"""
        current_scene = self.scene_map.openning_scene() # return the specific scene object
        last_scene = self.scene_map.next_scene('finished') # return Finished()

        while current_scene != last_scene:
            next_scene_name = current_scene.enter() # it is the next_scene_name which returned by the enter() of current_scene
            current_scene =self.scene_map.next_scene(next_scene_name)

        # be sure to print out the last scene
        current_scene.enter()


class Death(Scene):
    quips = ["You died. You kinda suck at this.",
        "Your Mom would be proud... if she were smarter.",
        "Such a loser.",
        "I have a small puppu that's better at this.",
        "You're worse than his cat's joke."]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips) - 1)]) # Death.quips ? self.quips
        exit(1)


class CentralCorridor(Scene):

    # dedent() can be used to make triple-quoted strings line up with the left edge of the display,
    # while still presenting them in the source code in indented form.
    def enter(self):
        print(dedent("""
        The Gothons of Planet Percal #25 have invaded your ship destroyed your entire crew.
        You are the last surviving member and your last mission is to get the neutron destruct
        bomb from the Weapons Armory, put it in the bridge, and blow the ship up after getting
        into on escape pod.

        You're running down the central corridor to the Weapons Arnory when a Gothon jumps out,
        red dcaly skin , dark grimy teeth and evil clown costume flowing around his hate filled body.
        He's blocking the door to the Armoary and about to pull a weapon to blast you.
        """))

        action = input("> ")

        if action == 'shoot!':
            print(dedent("""
            Quick onn the draw you yank out your blaster and fire it at the Gothonself.
            His clown costume is flowing and moving around his body, which throws off your aim.
            Your laser hists his cosrume but misses him entirely. This completely ruins his brand
            new costume his mother bought him, which makes him fly int an insane rage and blast you
            repeatedly in the face until you are dead. Then he eats you.
            """))
            return 'death'

        elif action == 'dodge!':
            print(dedent("""
            Like a world class boxer you dodge, weave, slip and slide right as the Gothon's blaster cranks
            a laser past your head. In the middle of your artful dodge your foot slips and you bang your head
            on the metal wall and pass out. You wake up shortly after only to die as the Gothon stomps on your
            head and eats you.
            """))
            return 'death'

        elif action == 'tell a joke':
            print(dedent("""
            Lucky for you they made you learn Gothon insults in the academy. You tell the one Gothon joke you know:
            Lbhe zbgure cf fb sng, jura fur fcgf nebhaq gur ubhfr, fur fvgf nebhaq gur ubhfr. The Gothons, tries not to laugh,
            then busts out laughing and can't move. While he's laughing you run up and shoot him square in the head putting him
            down, then jump through the Weapon Armory door.
            """))
            return 'laser_weapon_armory'

        else:
            print("DOES NOT COMPUTE!")
            return 'central_corridor' # if the action cannot be recognized then start the secent agaain

class LaserWeaponArmory(Scene):

    def enter(self):
        print(dedent("""
        You do a dive roll into the Weapon Armory, crouch and scan the room for more Gothons that might be hidding. It's dead quiet,
        too quiet. You stand up and run to the far side of the toom and find the nertron bomb in its container. There's a keypad lock
        on the box and you need the code to get the bomb out. If you get the code wrong 10 times then the lock closes forever and you
        can't get the bomb. The code is 3 digits.
        """))

        code = f"{randint(1, 9)}{randint(1, 9)}{randint(1, 9)}"
        print(code)
        guess = input("[keypad]> ")
        guessed = 1 # this is used to count the total numbers of guessing

        while guess != code and guessed < 10:
            print("BZZZZEDDD")
            guessed += 1
            guess = input("[keypad]> ")

        if guess == code:
            print(dedent("""
            The container clicks open and the seal breaks, letting gas out. You grab the neutron bomb and run as fast as you can to the
            bridge where you must place it in the right spot.
            """))
            return 'the_bridge'
        else:
            print(dedent("""
            The lock buzzes one last time and then you hear a sickening melting sound as the mechanism is fused together. You decide to
            sit there, and finally the Gothons blow up the ship from their ship and you die.
            """))
            return 'death'

class TheBridge(Scene):

    def enter(self):
        print(dedent("""
        Your burst onto the Bridge with the netron destruct bomb under your arm and surprise 5 Gothons who are trying to take control of
        the ship. Each of them has an even uglier clown costume than the last. They haven't pulled their weapons out yet, as they ess the
        active bomb under your arm and don't want to set it off.
        """))

        action = input("> ")

        if action == "throw the bomb":
            print(dedent("""
            In a panic you throw the bomb at the group of Gothons and make a leap for the door. Right as you drop it a Gothon shoots you right'
            in the back killing you. As you die you see another Gothon frantically try to disarm the bomb. You die knowing they will probably
            blow up when it goes off.
            """))
            return 'death'

        elif action == "slowly place the bomb":
            print(dedent("""
            You point your blaster at the bomb under your arm and Gothons put their hands up and start to sweat. You  inch backward to the door,
            open it, and then carefully place the bomb on the floor, pointing your blaster at it. You then jump back through the door, punch the
            close button and blast the lock so the Gothons can't get out. Now that the bomb is placed you run to the escape pod to get off this tin
            can.
            """))
            return 'escape_pod'
        else:
            print("DOED NOT COMPUTE")
            return 'the_bridge'

class EscapePod(Scene):

    def enter(self):
        print(dedent("""
        You rush through the ship desperately tring to make it to the escape pod before the whole ship explodes. It seems like hardly any Gothons are
        on the ship, so your run is clear of interference. You get to the chamber with the escape pods, and now need to pick one to take. Some of them could
        be damaged but you don't hace time to look. There's 5 pods, which one do you take?
        """))

        good_pod = randint(1, 5)
        print(good_pod)
        guess = input("[pod #]> ")

        if int(guess) != good_pod:
            print(dedent("""
            You jump into pod {guess} and hit the eject button. The pod escape out into the void of space, then implodes as the hull ruptures, crushing your body into
            the jam jelly.
            """))
            return 'death'
        else:
            prnit(dedent("""
            You jump into the pod {guess} and hit the eject button. The pod easily slides out into space heading to the planet below. As it flies to the planet, you look
            back and see your ship implode then explode like a bright star, taking out the Gothohn ship at the same time. You won!
            """))
            return 'finished'

class Finished(Scene):

    def enter(self):
        print("You won! Good job!")
        return 'finished'

class Map(object):

    scenes = {
    'central_corridor': CentralCorridor(),
    'laser_weapon_armory': LaserWeaponArmory(),
    'the_bridge': TheBridge(),
    'escape_pod': EscapePod(),
    'death': Death(),
    'finished': Finished()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        """This function will return the scene class matches the entered scene_name."""
        val = Map.scenes.get(scene_name)
        return val # return the correct Scene Class

    def openning_scene(self):
        return self.next_scene(self.start_scene) # return the scene object


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()

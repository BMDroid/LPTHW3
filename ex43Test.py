`# This is my version of the ex43

class Scene(object):

    def enter(self):
        pass

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map
        pass

    def play(self):
        self.scene_map.start_scene.enter()
        pass

class Death(Scene):

    def enter(self):
        pass

class CentralCorridor(Scene):

    def enter(self):
        print("Yes")
        pass

class Map(object):

    def __init__(self, start_scene):
        scenes = {'death': Death(), 'central_corridor': CentralCorridor()} # Wow, this is exactly what the Zed did in the book
        self.start_scene = scenes.get(start_scene)
        pass

    def next_scene(self, scene_name):
        pass

    def openning_scene(self):
        pass



a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()

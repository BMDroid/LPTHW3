from room import Room
from start import Start
from death import Death
from finished import Finished

class Engine(object):

    Rooms = {
        'start': Start(),
        'death': Death(),
        'finished': Finished()
        }

    def __init__(self, current_room_name):
        self.current_room = self.Rooms.get(current_room_name)

    def play_game(self):

        next_room_name = 'None'

        while next_room_name == 'None':
            self.current_room.enter_room()
            next_room_name = self.current_room.exit_room()
            self.current_room = self.Rooms.get(next_room_name)
            next_room_name = self.current_room.info.get('next_room')


engine = Engine('start')
engine.play_game()

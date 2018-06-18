class Room(object):
    info = {}
    actions = []

    def __init__(self, current_room):
        self.info = {'current_room': '', 'next_room': 'None'}
        self.info['current_room'] = current_room

    def enter_room(self):
        pass

    def exit_room(self):
        return self.info.get('next_room')

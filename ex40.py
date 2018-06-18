# A first class example

class Song(object):

    def __init__(self, name, lyrics):
        self.name = name
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song("Happy birthday to You", ["Happy birthday to you.",
    "I don't want to get sued",
    "So I'll stop right there"]) # happy_bday is a object from class Song

bulls_on_parade = Song("Bulls on Parade",["They rally around tha family", "With pockets full of shells"])

happy_bday.sing_me_a_song()

print(bulls_on_parade.name)

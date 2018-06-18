from ex48 import lexicon

class Sentence(object):

    def __init__(self, verb, obj):
        self.subject = 'Player'
        self.verb = verb
        self.object = obj

def parser(input):
    words = lexicon.scan(input)
    return words

def peek(words):
    verb =''
    obj = ''
    if words:
        for w in words:
            if w[0] == 'verb':
                verb = w[1]
            elif w[0] == 'noun' or w[0] == 'direction':
                obj = w[1]
    sentence = Sentence(verb, obj)
    return sentence
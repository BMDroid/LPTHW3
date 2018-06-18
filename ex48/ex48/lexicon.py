lexicon = {
    'north': 'direction',
    'south': 'direction',
    'east': 'direction',
    'west': 'direction',
    'down': 'direction',
    'up': 'direction',
    'left': 'direction',
    'right': 'direction',
    'back': 'direction',
    'go': 'verb',
    'stop': 'verb',
    'kill': 'verb',
    'eat': 'verb',
    'the': 'stop',
    'in': 'stop',
    'of': 'stop',
    'from': 'stop',
    'at': 'stop',
    'it': 'stop',
    'door': 'noun',
    'bear': 'noun',
    'princess': 'noun',
    'cabinet': 'noun',
    '0123456789': 'number'
    }

def scan(input):
    words = input.split(" ")
    for i in range(0, len(words)):
        word_is_int = is_int(words[i])

        if word_is_int:
            type = 'number'
            words[i] = convert_number(words[i])
        else:
            type = lexicon.get(words[i].lower()) # case-insensitive
        
        if type == None:
            words[i] = ('error', words[i])
        else:
            words[i] = (type, words[i])

    return words

def is_digit(str):
    if str.isdigit():
        return True
    return False

def is_int(str):
    nums = "0123456789"

    if all((i in nums) for i in str):
        return True
    return False

def is_number(str):
    nums = "0123456789."
    dot_count = 0 # count the '.' in the num_str
    for i in str:
        if dot_count >1 or i not in nums:
            return False
        elif i == '.':
            dot_count += 1
    return True

def convert_number(num_str):
    try:
        return int(num_str)
    except ValueError:
        return None

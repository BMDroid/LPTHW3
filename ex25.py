def break_words(stuff):
    """This function will break up words for us.""" # this will be showed when help(ex25) being called
    words =  stuff.split(' ')
    # str.split(sep=None, maxsplit=-1), Return a list of the words in the string, using sep as the delimiter string.
    # If maxsplit is given, at most maxsplit splits are done (thus, the list will have at most maxsplit+1 elements).
    # If maxsplit is not specified or -1, then there is no limit on the number of splits (all possible splits are made).
    # If sep is given, consecutive delimiters are not grouped together and are deemed to delimit empty strings
    # (for example, '1,,2'.split(',') returns ['1', '', '2']).
    # The sep argument may consist of multiple characters
    # (for example, '1<>2<>3'.split('<>') returns ['1', '2', '3']).
    # Splitting an empty string with a specified separator returns ['']."""
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words) # sort the elements of given iretable in a specific order

def print_first_word(words):
    """Print the first word after popping it off."""
    # Remove the item at the given position in the list, and return it.
    # If no index is specified, a.pop() removes and returns the last item in the list.
    word = words.pop(0) # remove the first element and returen it
    print(word)

def print_last_word(words):
    """Print the last word after popping it off."""
    word = words.pop(-1) # this could be word = words.pop()
    print(word)

def sort_sentence(sentence):
    """Take in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)


def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)

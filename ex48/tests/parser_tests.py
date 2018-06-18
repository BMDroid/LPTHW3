from nose.tools import *
from ex48.parser import *

def test_exception():
    words_list = [('stop', 'the')]
    assert_raises(ParserError, parse_verb, words_list) # assert_raise(exception, callable, parameters)
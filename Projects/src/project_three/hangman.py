import random


class Hangman(object):
    def __init__(self):
        pass

    def get_word(self):
        words = ['yellow', 'bird', 'house']
        word = words[random.randint(0, len(words) - 1)]

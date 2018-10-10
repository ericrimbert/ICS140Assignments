import random


class Hangman(object):
    def __init__(self):
        self.attempts = 10
        self.word = None
        self.output_dict = {}

    def get_word(self):
        words = ['yellow', 'bird', 'house']
        word = words[random.randint(0, len(words) - 1)]

        self.word = word
        return word

    def generate_word_output(self, word):
        count = len(word)
        i = 1
        while i <= count:
            self.output_dict[i] = "_"
            i += 1

        return self.output_dict

    # takes a guessed letter, checks if it is in word
    def check_guessed_letter(self, letter):
        # sets i to count index and count to count correct amount of letters
        i = 1
        count = 0
        for char in self.word:
            if letter == char:
                self.output_dict[i] = char
                count += 1
            i += 1

        # returns count
        return count


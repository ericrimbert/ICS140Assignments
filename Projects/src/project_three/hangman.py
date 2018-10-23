import random


class Hangman(object):
    # constructs initial variables upon the call of the class
    def __init__(self):
        self.attempts = 10
        self.letter_counter = 0
        self.word_details = self.get_word()
        self.word = self.word_details[0]
        self.word_length = self.word_details[1]
        self.alphabet = self.initialize_alphabet()
        self.output_dict = {}

    # gets a word from a dictionary at random
    @staticmethod
    def get_word():
        words = ['yellow', 'bird', 'house', 'mouse', 'doctor', 'dog', 'keystone', 'is', 'bad', 'television', 'bag']
        word = words[random.randint(0, len(words) - 1)]
        word_length = len(word)
        return word, word_length

    # sets the dictionary in the constructor to contain values of the word
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

    # returns the dictionary in a formatted output
    def formatted_output(self):
        output_string = ""
        for key, char in self.output_dict.items():
            output_string += char + " "

        return output_string.strip()

    # initializes a dictionary of the alphabet
    @staticmethod
    def initialize_alphabet():
        # initializes a dictionary and sets num to 97, 97 is lowercase a
        alphabet = {}
        num = 97

        # while that number is less-than or equal to 122(lowercase z)
        while num <= 122:
            # set ascii char to false in dict, iterate 1
            alphabet[chr(num)] = False
            num += 1

        # return dictionary
        return alphabet

    # checks if the letter is a letter and if it has been guessed already
    def validate_letter(self, letter):
        if letter in self.alphabet:
            if self.alphabet[letter]:
                return False
            # if letter wasn't guessed already, sets it to be guessed
            self.alphabet[letter] = True
            return True

        return False

    # ui health for the user to see
    def user_health(self):
        health = 10 * self.attempts
        return f"HEALTH: {health}%"

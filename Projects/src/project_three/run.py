from Projects.src.project_three.hangman import Hangman
hangman = Hangman()


def main():
    word = hangman.get_word()
    hangman.generate_word_output(word)
    letter = input()
    print(hangman.check_guessed_letter(letter))
    print(hangman.output_dict)


main()

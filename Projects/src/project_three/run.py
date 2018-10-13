from Projects.src.project_three.hangman import Hangman
hangman = Hangman()


def main():
    hangman.generate_word_output(hangman.word)

    print(f"Your word has {hangman.word_length} letters, good luck! ---> {hangman.formatted_output()}")
    while hangman.attempts >= 0:
        if hangman.attempts == 0:
            print("You have no more attempts left! You Lose!")
            break

        guessed_letter = input("Enter in a letter: ").lower()
        if hangman.validate_letter(guessed_letter):
            round_count = hangman.check_guessed_letter(guessed_letter)
            if round_count:
                print(f"You got {round_count} letter(s) correct! ---> {hangman.formatted_output()}")
                hangman.letter_counter += round_count
                if hangman.letter_counter == hangman.word_length:
                    print("You Win!")
                    break
            else:
                print(f"You did not get any letters! ---> {hangman.formatted_output()}")
                hangman.attempts -= 1

        else:
            print("Not a valid letter or letter was already guessed.")


main()

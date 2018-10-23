from Projects.src.project_three.hangman import Hangman
hangman = Hangman()


# main function that runs the program
def main():
    # gets word and word length
    hangman.generate_word_output(hangman.word)

    # prints initial statement and sets a while loop, attempts are set to 10 for now
    print(f"Your word has {hangman.word_length} letters, good luck! ---> {hangman.formatted_output()}")
    while hangman.attempts >= 0:

        # if attempts are 0, end and print a loss
        print(hangman.user_health())  # health
        if hangman.attempts == 0:
            print(f"You have no more attempts left! You Lose!\nYour word was {hangman.word}")
            break

        # sets guessed letter and validates it
        guessed_letter = input("Enter in a letter: ").lower()
        if hangman.validate_letter(guessed_letter):
            round_count = hangman.check_guessed_letter(guessed_letter)

            # checks if there is a round_count, if there is not then the letter was not right
            if round_count:
                print(f"\nYou got {round_count} letter(s) correct! ---> {hangman.formatted_output()}")
                hangman.letter_counter += round_count

                # win if letter counter is the same as the word length
                if hangman.letter_counter == hangman.word_length:
                    print("You Win!")
                    break

            # outputs if the letter is incorrect
            else:
                print(f"\nYou did not get any letters! ---> {hangman.formatted_output()}")
                hangman.attempts -= 1

        # outputs if letter was guessed already or is something not in the alphabet
        else:
            print("\nNot a valid letter or letter was already guessed.")


main()

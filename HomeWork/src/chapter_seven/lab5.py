# lab 5


# returns true or false if the string is the same backwards
def palindrom(string):
    string = string.lower()
    if string == string[::-1]:
        return True
    else:
        return False


# returns string that has the first letter upper cased
def capitalize(string):
    # lowers all letters
    string = string.lower()
    # gets the first word in string
    first_word = string.split()[0]
    # splits the rest of the words into a list
    string = string.split()
    string = string[1::]
    # capitalizes first letter in first_word
    capital = first_word[0].upper()
    # splits first word by the first letter then joins the new string and capitalizes letter
    first_word = first_word.split(first_word[0])
    first_word = capital.join(first_word)
    # inserts first_word into first index of list
    string.insert(0, first_word)
    # joins list together with spaces
    return ' '.join(string)


# main function that gets input for word and phrase, does the needful
def main():
    string = input("Enter in a word: ")
    if palindrom(string):
        print("Your word is a palindrom!")
    else:
        print("Your word is not a palindrom.")

    phrase = input("Enter in a phrase, or multiple words: ")
    phrase = capitalize(phrase)
    print(phrase)


main()

# capitalize () is a function that accepts a string as an argument.
# Convert the first character of each word to an upper-case letter
# and the remaining letters to lower-case letters. Return the resulting string.
# Use the string functions split and join.


def palindrom(string):
    string = string.lower()
    if string == string[::-1]:
        return True
    else:
        return False


# did not care for the split function and join.
def capitalize(string):
    string = string.lower()
    string_first = string[0].upper()
    string = string.replace(string_first.lower(), string_first)
    print(string)


def main():
    print(palindrom("civic"))
    capitalize("horse")


main()

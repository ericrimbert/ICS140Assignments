# 1.3.4 - Read user input numbers and perform a calculation

# Try-Except statement to verify the user entered in a correct number
try:
    # Variables that prompt the user to input numbers
    first_number = int(input("Enter in a number: "))
    second_number = int(input("Enter in a second number: "))

    # Prints users two numbers added together
    print(f'Sum of your numbers = {first_number + second_number}')

except ValueError as Error:
    print('Uh oh! You entered an invalid number!')

import random


class ProjectFour(object):
    def __init__(self):
        pass

    # Function 1: stats(). This function takes as its argument a list of numbers.
    # It returns a tuple consisting of the minimum, maximum and average value.
    def stats(self, num_list):
        try:
            # validates the incoming value is a list, raise type error if not
            if type(num_list) != list:
                raise TypeError

            # set blank value for totaling then averaging
            total = 0
            for num in num_list:
                total += num

            # sets final values for min, max, and avg - then returns a tuple of them
            max_num = max(num_list)
            min_num = min(num_list)
            avg_num = total / len(num_list)
            num_values = (min_num, max_num, avg_num)

            return num_values

        except TypeError:
            print("You did not provide a list!")

            return None

        except ValueError:
            print("You did not provide a correct numbers in your list!")

            return None

    # Function 2: reverse(). This function takes a string as its argument.
    # It reverses the characters in the string and returns the resultant string.
    def reverse(self, string):
        try:
            # auto sets the string to type string just in case
            string = str(string)

            # returns backwards string
            return string[::-1]

        except TypeError:
            print("Invalid type, please enter in a string!")

    # Function 3: triangle(). This function takes an integer as its argument.
    # The function prints out a right triangle with the base and height as the input argument.
    # For example, if the base is 5, the triangle would be printed as:
    def triangle(self, base, triangle):
        try:
            # disallows a base of 2
            if base <= 2:
                print("Base is too small!")
                return None

            # prints if triangle type is specified
            if triangle:
                # triangle type 1
                if triangle == 1:
                    # sets index and other main variables
                    index = 1
                    start = "*"
                    second = "**"
                    base_str = "*"*base

                    # prints parts that all triangles will have
                    print(start)
                    if base > 2:
                        print(second)
                    # loop that will print center section of the triangle
                    while index <= base-3:
                        print(start + " "*index + start)
                        index += 1
                    print(base_str)

                    return True

                else:
                    # do an isosc triangle
                    base_str = "*"*((base*2)-1)
                    # sets triangle settings that all sizes will have
                    index = 1
                    start = " "*(base-1)+"*"
                    print(start)
                    # while loop with incrementing index
                    while index <= base-2:
                        # line that gets printed, separated for readability
                        line1 = " "*(base-index-1) + "*"
                        line2 = " "*(index*2-1)+"*"
                        # prints then increments index
                        print(line1 + line2)
                        index += 1

                    # prints the base
                    print(base_str)

        except TypeError:
            print("Invalid number, please enter in an integer larger than 1!")

            return None

        except ValueError:
            print("Please enter in a valid value!")

            return None


project = ProjectFour()

# Main Program:
#
#
# Create a list of 10 or more random numbers between 0 and 100.
#
# Call the function stats with this list as its argument.
#
# Print out the numbers in the list
#
# Print the results of calling stats as:
#
# Minimum = XX, Maximum = YY, Average = ZZ.
#
#
# Ask the user to enter a string to be reversed.
#
# Call the function reverse with this string as its argument.
#
# Print out the reversed string.
#
#
# Ask the user to enter the size of the triangle to print.
#
# Call the function triangle with this number as its argument.


def main():
    # part one
    # creates a list
    print("")
    random_nums = list()
    index = 1
    # fills list depending on a random size with random numbers
    while index < random.randint(10, 100):
        random_nums.append(random.randint(0, 100))
        index += 1
    # checks if stats returned and prints the numbers, then the min, max, and avg
    stats = project.stats(random_nums)
    if stats:
        string = "Numbers in list:"
        for num in random_nums:
            string += " " + str(num)
        print(string)
        print(f"Minimum = {stats[0]}, Maximum = {stats[1]}, Average = {stats[2]}\n")

    # gets a string to be reversed
    string = input("Enter in a string to be reversed: ")
    reversed_string = project.reverse(string)
    # prints reversed string
    if reversed_string:
        print(reversed_string + "\n")

    # Gets a triangle size and type, then prints it
    try:
        tri_size = int(input("Please enter in the size you want your triangle to be: "))
        tri_type = int(input("What type of triangle do you want?\nEnter in '1' for a right triangle and '2' for an icosceles: "))
        if tri_type != 1:
            tri_type = 2

        project.triangle(tri_size, tri_type)

    except ValueError:
        print("Invalid number entered!")


main()

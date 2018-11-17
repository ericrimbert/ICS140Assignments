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
            num_values = (max_num, min_num, avg_num)

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
    def triangle(self, base, triangle=1):
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

                if triangle == 2:
                    # do an isosc
                    base_str = "*"*((base*2)-1)
                    index = 1
                    start = " "*(base-1)+"*"
                    print(start)
                    while index <= base-2:
                        line1 = " "*(base-index-1) + "*"
                        line2 = " "*index+"*"
                        print(line1 + line2)
                        index += 1
                    print(base_str)

        except TypeError:
            print("Invalid number, please enter in an integer larger than 1!")

            return None

        except ValueError:
            print("Please enter in a valid value!")

            return None


project = ProjectFour()

print(project.triangle(4, 2))

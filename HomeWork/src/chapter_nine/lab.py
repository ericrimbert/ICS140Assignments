# redo lab
from math import pi, sqrt


# class for math functions
class MathFunctions(object):
    def __init__(self):
        pass

    # quadratic formula
    def quadratic_formula(self, A, B, C):
        root1 = (- B + (sqrt(B*B) - sqrt(4*A*C)))/2*A
        root2 = (- B - (sqrt(B*B) - sqrt(4*A*C)))/2*A

        # if the roots are negative zeros, return zeros
        if root1 == -0.0:
            root1 = 0

        if root2 == -0.0:
            root2 = 0

        # if the roots are the same, return one of them
        if root1 == root2:
            root2 = None
            return root1, root2

        return root1, root2

    # area formula
    def area(self, r):
        try:
            area = pi * (r * r)

            return area

        except Exception:
            return "Cannot compute Area!"

# calling the class and setting it


functions = MathFunctions()


# main program
def main():
    # sets a bool value for looping
    arg = True
    while arg:
        # try running quadratic formula
        try:
            a = float(input("Please enter in Value for 'A': "))
            b = float(input("Please enter in Value for 'B': "))
            c = float(input("Please enter in Value for 'C': "))

            try:
                root1, root2 = functions.quadratic_formula(a, b, c)
                print(f'Root 1: {root1}')
                if root2:
                    print(f'Root 2: {root2}')

                arg = False

            except Exception:
                print('Error, cannot compute roots!\n')
                arg = False

        except ValueError:
            print("Please enter in a valid number!")

    arg = True
    while arg:
        # try running the area
        try:
            radius = float(input("Please enter in a radius: "))
            if radius <= 0:
                raise ValueError

            print(functions.area(radius))

            arg = False

        except ValueError:
            print('Error, please enter in a valid number!')


# call main function
main()

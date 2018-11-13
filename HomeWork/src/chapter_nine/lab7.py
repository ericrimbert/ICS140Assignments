# lab 7
from math import sqrt


class MathFunctions(object):
    def __init__(self):
        pass

    def quadratic_formula(self):
        try:
            A = float(input("Please enter in Value for 'A': "))
            B = float(input("Please enter in Value for 'B': "))
            C = float(input("Please enter in Value for 'C': "))

            root1 = (- B + (sqrt(B*B) - sqrt(4*A*C)))/2*A
            root2 = (- B - (sqrt(B*B) - sqrt(4*A*C)))/2*A

            # if the roots are negative zeros, return zeros
            if root1 == -0.0:
                root1 = 0

            if root2 == -0.0:
                root2 = 0

            # if the roots are the same, return one of them
            if root1 == root2:
                print(f'Root is {root1}')

            else:
                print(f'Root 1: {root1}')
                print(f'Root 2: {root2}')

        except ValueError as e:
            print("Invalid number. Please enter in a valid number.")
            print(str(e) + '\n')
            con = input("Would you like to continue? [Y]es or [N]o - ")
            if str(con.lower()) == "y" or str(con.lower()) == "yes":
                self.quadratic_formula()
            else:
                return

        except:
            print("No roots!")

    def area(self):
        pass


maf = MathFunctions()
maf.quadratic_formula()

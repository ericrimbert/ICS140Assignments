# Project 1
# Given User input for a circles radius - Find the circumference and area


class CircleMath(object):
    def __init__(self):
        self.radius = float(input("Please enter the radius of the Circle: "))

    def equate_circumference(self):
        try:
            diameter = 2 * self.radius
            print(diameter)

        except ValueError:
            print('Error, incorrect value')

    def equate_area(self):
        pass


domath = CircleMath()
domath.equate_area()
domath.equate_circumference()

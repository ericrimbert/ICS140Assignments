# Project 1
# Given User input for a circles radius - Find the circumference and area
from math import pi


class CircleMath(object):
    def __init__(self):
        self.radius = input("Please enter the radius of the Circle: ")

    # gets the circumference of the circle given radius
    def equate_circumference(self):
        try:
            radius = float(self.radius)
            circumference = 2 * pi * radius

            print(f'The circumference of a circle given the radius {radius} is {circumference}.')

        except ValueError:
            print('Error, incorrect value')

    # gets the area of the circle given radius
    def equate_area(self):
        try:
            radius = float(self.radius)
            area = 2 * (radius * radius)

            print(f'The circumference of a circle given the radius {radius} is {area}.')

        except ValueError:
            print('Error, incorrect value')


circle_math = CircleMath()
circle_math.equate_circumference()
circle_math.equate_area()

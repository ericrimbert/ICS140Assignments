# add stuff


class Calculator(object):
    def __init__(self):
        pass

    def addition(self, num_one, num_two):
        try:
            return num_one + num_two
        except ValueError:
            return "Error!", True

    def subtraction(self, num_one, num_two):
        try:
            return num_one - num_two
        except ValueError:
            return "Error!", True

    def multiplication(self, num_one, num_two):
        try:
            return num_one * num_two
        except ValueError:
            return "Error!", True

    def division(self, num_one, num_two):
        try:
            return num_one / num_two
        except ValueError:
            return "Error!", True

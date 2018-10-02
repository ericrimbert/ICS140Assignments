from Projects.src.project_two.calculator import Calculator
calc = Calculator()


class UserInterface(object):
    def __init__(self):
        self.operations = ['+', '-', '/', '*', 'x', '%']

    def get_input(self):
        try:
            return input("Input: ")
        except KeyboardInterrupt:
            return "Error!", False

    def operations_parser(self, user_input):
        user_input = user_input.replace(' ', '')
        user_numbers = []
        user_operations = []

        for char in user_input:
            if char in self.operations:
                user_operations.append(char)
                num_one, num_two = user_input.split(char)
                user_numbers.append(num_one)
                user_numbers.append(num_two)

        return user_numbers, user_operations

    def operation_decision(self, operation, user_numbers):
        try:
            operation = operation[0]

            try:
                num_one = int(user_numbers[0])
                num_two = int(user_numbers[1])

            except ValueError:
                num_one = float(user_numbers[0])
                num_two = float(user_numbers[1])

            if operation == '+':
                return calc.addition(num_one, num_two), True

            elif operation == '-':
                return calc.subtraction(num_one, num_two), True

            elif operation == '/' or operation == '%':
                return calc.division(num_one, num_two), True

            elif operation == '*' or operation == 'x':
                return calc.multiplication(num_one, num_two), True

            else:
                return "Error! No operation found.", True

        except IndexError:
            return "Error! Index not found.", True

        except ValueError:
            return "Error! Incorrect value entered.", True

        except ZeroDivisionError:
            return "Error! Cannot divide by Zero.", True

# lab 6

# 1. Write a function that prints the name and grade percentage of the student.

# 2. Write a function that finds the average score of each assignment.
#      That is the average of the first assignment, the average of the second assignment, etc.


class StudentStatistics(object):
    def __init__(self):
        self.dictionary = self.initialize_dictionary()

    @staticmethod
    def initialize_dictionary():
        student_grades = {
            'Andrew': [56, 79, 90, 22, 50],
            'Nisreen': [88, 62, 68, 75, 78],
            'Alan': [95, 88, 92, 85, 85],
            'Chang': [76, 88, 85, 82, 90],
            'Tricia': [99, 92, 95, 89, 99]
        }

        return student_grades

    # returns a dictionary of their score in percent
    def get_grades(self):
        student_percentages = {}
        for name, scores in self.dictionary.items():
            max_grade = len(scores) * 100
            total = 0
            for score in scores:
                total += score
            student_percentages[name] = (total / max_grade) * 100

        return student_percentages

    def avg_test_grade(self):
        average_test = {}
        index = 0
        while index < len(self.dictionary):
            total_test = 0
            for scores in self.dictionary.values():
                total_test += scores[index]
            average_test[index+1] = (total_test / (100 * len(self.dictionary))) * 100
            index += 1

        return average_test


def main():
    SchoolGrades = StudentStatistics()

    # prints out each students grade
    for name, grade in SchoolGrades.get_grades().items():
        print(f'{name} - {grade}%')

    print()

    # prints average test score for each test
    for test, average in SchoolGrades.avg_test_grade().items():
        print(f'Test {test} - {average}%')


main()

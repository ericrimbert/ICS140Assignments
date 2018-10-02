from Projects.src.project_two.ui import UserInterface
ui = UserInterface()


# runs code and adds a little message at the top
# include while loop to loop until the user is done
def main():
    answer = True
    print("\t\t----------Simple Calculator----------")
    print("\t\t-----This is a Simple Calculator-----")
    print("You can use addition, subtraction, multiplication, and division")
    print('\t\tIf you would like to quit, type "quit"\n')
    while answer:
        user_input = ui.get_input()
        if user_input.strip().lower() == 'quit':
            answer = False
            return answer

        items = ui.operations_parser(user_input)
        numbers = items[0]
        operations = items[1]

        answer = ui.operation_decision(operations, numbers)
        print(answer[0])
        print('')
        answer = answer[1]


main()

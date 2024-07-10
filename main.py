# from functions import get_todos, write_todos
from modules import functions
import time
while True:
    user_action = input("Type add or show or edit or complete or exit : ")

    if user_action.startswith('add'):
        todo = user_action[4:]
        todos = functions.get_todos()
        todos.append(todo + "\n")
        functions.write_todos(todos)
    elif user_action.startswith('show'):
        todos = functions.get_todos()
        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            print('Current value is ' + todos[number - 1].strip('\n'))
            new_todo = input('Enter the new todo: ')
            todos = functions.get_todos()
            todos[number - 1] = new_todo + "\n"
            functions.write_todos(todos)
        except ValueError:
            print("Your command is invalid")
            continue
    elif user_action.startswith('complete'):
        number = int(user_action[8:])
        todos = functions.get_todos()
        todos.pop(number - 1)
        functions.write_todos(todos)
    elif user_action.startswith('exit'):
        break
    else:
        print('Not a valid command')
print("Bye!")

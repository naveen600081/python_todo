FILEPATH = 'todos.txt'


def get_todos(filePath=FILEPATH):
    with open(filePath, 'r') as file:
        todos = file.readlines()
    return todos


def write_todos(todos_args, filePath=FILEPATH):
    with open(filePath, 'w') as file:
        file.writelines(todos_args)


if __name__ == "__main__":
    print("Hello")

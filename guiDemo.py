import functions
import FreeSimpleGUI as sg

label = sg.Text("Type todo ")
addTodoTask = sg.InputText(tooltip="Enter a todos", key="todo")
add_button = sg.Button("Add")
show_list = sg.Listbox(values=functions.get_todos(), key="todos",
                       enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
window = sg.Window("My Todo App", layout=[[label], [addTodoTask, add_button], [show_list, edit_button],[complete_button]],
                   font=('Arial', 20))
while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            todos.append(values['todo'] + "\n")
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            todo_edit = values["todos"][0]
            new_todo = values['todo']
            todos = functions.get_todos()
            index = todos.index(todo_edit)
            todos[index] = new_todo + "\n"
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Complete":
            todo_complete = values["todos"][0]
            todos = functions.get_todos()
            index = todos.index(todo_complete)
            todos.pop(index)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            break
print("Bye!")
window.close()

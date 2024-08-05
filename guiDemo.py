import functions
import PySimpleGUI as sg
import time
sg.theme("Black")
clock = sg.Text("",key="clock")
label = sg.Text("Type todo ")
addTodoTask = sg.InputText(tooltip="Enter a todos", key="todo")
add_button = sg.Button("Add")
show_list = sg.Listbox(values=functions.get_todos(), key="todos",
                       enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")
window = sg.Window("My Todo App", layout=[[clock], [label], [addTodoTask, add_button], [show_list, edit_button, complete_button], [exit_button]],
                   font=('Arial', 20))
while True:
    event, values = window.read(timeout=500)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    match event:
        case "Add":
            todos = functions.get_todos()
            todos.append(values['todo'] + "\n")
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            try:
                todo_edit = values["todos"][0]
                new_todo = values['todo']
                todos = functions.get_todos()
                index = todos.index(todo_edit)
                todos[index] = new_todo + "\n"
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first", font=("Helvetica",20))
        case "Complete":
            try:
                todo_complete = values["todos"][0]
                todos = functions.get_todos()
                index = todos.index(todo_complete)
                todos.pop(index)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first", font=("Helvetica", 20))
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case 'Exit':
            window.close()
            break
        case sg.WIN_CLOSED:
            break
print("Bye!")
window.close()

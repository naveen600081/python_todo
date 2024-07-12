import functions
import FreeSimpleGUI as sg

label = sg.Text("Type todo ")
addTodoTask = sg.InputText(tooltip="Enter a todo")
add_button = sg.Button("Add")
window = sg.Window("My Todo App", layout=[[label], [addTodoTask, add_button]])
window.read()
window.close()

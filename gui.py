import function
import PySimpleGUI as sg

#  Define window content
label = sg.Text("Type in a To-Do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=function.read_todo(), key='todos',
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")

# Define the window content
layout = [[label], [input_box, add_button], [list_box, edit_button]]

# Create the window
window = sg.Window("My To-Do App", layout=layout, font=('Helvetica', 15))

# Display the window
while True:
    event, value = window.read()
    print(event)
    print(value)
    print(value['todos'])
    match event:
        case "Add":
            todos = function.read_todo()
            new_todo = value['todo'] + "\n"
            print(new_todo)
            todos.append(new_todo)
            function.write_todo(todos)
            window['todos'].update(values=todos)
        case "Edit":
            todo_to_edit = value['todos'][0]
            new_todo = value['todo']

            todos = function.read_todo()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            function.write_todo(todos)
            window['todos'].update(values=todos)
        case 'todos':
            window['todo'].update(value=value['todos'][0])
        case sg.WINDOW_CLOSED:
            break

# Finish up by removing from the screen
window.close()

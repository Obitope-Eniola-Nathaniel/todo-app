import function
import PySimpleGUI as sg

# Define the window content
layout = [[sg.Text("Type in a To-Do")],
          [sg.InputText(tooltip="Enter todo", key="todo"), sg.Button("Add")]]

# Create the window
window = sg.Window("My To-Do App", layout, font=('Helvetica', 15))

# event, value = window.read()
# print(event)
# print(value)
# Display the window
while True:
    event, value = window.read()
    print(event)
    print(value)
    match event:
        case "Add":
            todos = function.read_todo()
            new_todo = value['todo'] + "\n"
            print(new_todo)
            todos.append(new_todo)
            function.write_todo(todos)
        case sg.WINDOW_CLOSED:
            break

# Finish up by removing from the screen
window.close()

# # Another way in doing it
# label = sg.Text("Type in a To-Do")
# input_box = sg.InputText(tooltip="Enter todo")
# add_button = sg.Button("Add")
# window = sg.Window("My To-Do App", layout=[[lable, add_button], [input_box]])

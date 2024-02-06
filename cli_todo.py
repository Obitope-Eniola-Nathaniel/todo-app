# import function
from function import read_todo, write_todo
import time


time = time.strftime("%d %b, %Y %H:%M:%S")
print("It is", time)

while True:
    user_input = input("Type add, show, edit, complete or exit: ").strip()

    if user_input.startswith("add"):
        todo = user_input[4:] + "\n"

        # Read_todo list file
        todos = read_todo()

        todos.append(todo)

        # Write_todo to list
        write_todo(todos)

    elif user_input.startswith("show"):
        # Read_todo list file
        todos = read_todo()

        # todos = [item.strip for item in todos]
        # print(todos)
        for index, item in enumerate(todos):
            item = item.strip()
            print(f"{index + 1}-{item}")

    elif user_input.startswith("edit"):
        # Read_todo list file
        todos = read_todo()
        try:
            number = int(user_input[5:])
            number = number - 1
            new_todo = input("Enter new todo: ") + "\n"
            todos[number] = new_todo

            print(todos)

            # Write to_do to list
            write_todo(todos)
        except ValueError:
            print("Invalid input")
            pass

    elif user_input.startswith("complete"):
        try:
            number = int(user_input[9:])

            # Read_todo list file
            todos = read_todo()

            index = number - 1
            todo_to_remove = todos[index].strip()
            todos.pop(index)

            # Write_todo to list
            write_todo(todos)

            message = f" Todo {todo_to_remove} was removed from the list"
            print(message)
        except ValueError:
            print("Invalid input")
            pass

    elif "exit" in user_input:
        break
    else:
        print("Invalid command")

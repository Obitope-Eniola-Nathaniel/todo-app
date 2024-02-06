FILEPATH = "todos.txt"


def read_todo(filepath=FILEPATH):
    """ Read a text and return the list of
    to-do items.
    """
    with open(filepath, "r") as read_file:
        return read_file.readlines()


def write_todo(todos_agr, filepath=FILEPATH):
    """ Write the to_do items list in the test file. """
    with open(filepath, "w") as write_file:
        write_file.writelines(todos_agr)

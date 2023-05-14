# from functions import read_file, write_file
import functions
import time

now = time.strftime("%b %d, %Y  %H:%M:%S")
print(now)

while True:
    prompt = input("Add, Show, Edit or exit: ")
    prompt = prompt.strip()
    prompt = prompt.lower()
    # match prompt:
    if prompt.startswith("add"): # or add" in prompt - case if 'add' in prompt => produce error since case can not expect match expression solution is if/else
        task = prompt[4:] + '\n'
        # file = open('files/todo.txt', 'r')
        # todo = file.readlines()
        # file.close()
        todo = functions.read_file('todo.txt')
        todo.append(task)
        functions.write_file(filename="todo.txt", data=todo)
    elif prompt.startswith("show") or prompt.startswith("disp"): # case "show" | "Display"
        todo = functions.read_file('todo.txt')
        # todo_new = [do.strip("\n") for do in todo]
        for index, item in enumerate(todo): # Can be used either for getting characters of a word. enumurate also works for str
            item = item.strip("\n")
            item = item.title()
            row = f"{index+1}- {item}"
            # item.capitalize()
            print(row)
    elif prompt.startswith("edit"):
        try:
            number = int(prompt[5:])
            new_task = input("Write the new task: ") + '\n'
            todo = functions.read_file('todo.txt')
            todo[number-1] = new_task # todo.__setitem__(1,'test'), __getitem__
            functions.write_file("todo.txt", todo)
        except ValueError:
            print("Wrong input after input")
            continue
    elif prompt.startswith("complete"):
        try:
            number = int(prompt[9:])
            todo = functions.read_file('todo.txt')
            todo_to_removed = todo[number-1]
            todo_to_removed = todo_to_removed.strip("\n")
            todo.pop(number - 1)
            functions.write_file("todo.txt", todo)
            print(f"todo {todo_to_removed} has been removed.")
        except IndexError:
            print("Input number is out of range!")
            continue
    elif prompt.startswith("exit"):
        break
    else:
        print("Unknown inputs")
       #  case _:
       #     print("Please write Add, Show, Display or exit")
print('Bye')
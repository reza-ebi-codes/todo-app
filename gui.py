import functions
import PySimpleGUI as sg

label = sg.Text("Add to To-Do list")
input_box = sg.InputText(tooltip="Your To-Do", key="todo", enable_events=True)
add_button = sg.Button("Add")
view = sg.Listbox(values=functions.read_file("todo.txt"), key="todos", enable_events=True, size=(45, 10))
edit_button = sg.Button("Edit")


windows = sg.Window("App To-Do List",
                    layout=[[label], [input_box, add_button], [view, edit_button]],
                    font=('helvetica', 20))
while True:
    event, values = windows.read()
    print(values)
    match event:
        case "Add":
            todo_list = functions.read_file("todo.txt")
            new_todo = values["todo"] + "\n"
            todo_list.append(new_todo)
            functions.write_file("todo.txt", todo_list)
            windows["todos"].update(values=todo_list)
        case "Edit":
            todo_list = functions.read_file("todo.txt")
            print(todo_list)
            index = todo_list.index(values["todos"][0])
            todo_list[index] = values["todo"] + "\n"
            functions.write_file("todo.txt", todo_list)
            windows["todos"].update(values=todo_list)
        case "todos":
            windows["todo"].update(value=values["todos"][0].strip("\n"))
        case sg.WIN_CLOSED:
            break

windows.close()


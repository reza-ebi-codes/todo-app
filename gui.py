import functions
import PySimpleGUI as sg # Becare of upper case in the name of module

label = sg.Text("Add to To-Do list")
input_box = sg.InputText(tooltip="Your To-Do", key="todo")
add_button = sg.Button("Add")

windows = sg.Window("App To-Do List",
                    layout=[[label], [input_box], [add_button]],
                    font=('helvetica', 20))
while True:
    event, values = windows.read()
    match event:
        case "Add":
            todos = functions.read_file("todo.txt")
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            functions.write_file("todo.txt", todos)
        case sg.WIN_CLOSED:
            break

windows.close()


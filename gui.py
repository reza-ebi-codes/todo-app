import functions
import PySimpleGUI as sg # Becare of upper case in the name of module

label = sg.Text("Add to To-Do list")
input_box = sg.InputText(tooltip="Your To-Do")
add_button = sg.Button("Add")

windows = sg.Window("App To-Do List",layout=[[label],[input_box],[add_button]])
windows.read()
windows.close()


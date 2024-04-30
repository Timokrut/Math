import PySimpleGUI as sg
import os


sg.theme('DarkGrey9')

layout = [
    [sg.Text('Название фигуры'), sg.InputText()], 
    [sg.Button('Сгенерировать текст для Desmos')],
    [sg.Button('Создать GGB файл (Geogebra)')],
    [sg.Button('Создать OBJ файл (Blender, ...)')],
    [sg.Output(size=(70, 15))]
]

window = sg.Window("Desmos&Geogebra helper by Timokrut", layout)


while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    
window.close
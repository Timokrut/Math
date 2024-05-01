import PySimpleGUI as sg
from bs4 import BeautifulSoup as bs

import        os
import      json
import    shutil
import  requests
import pyperclip

from createobj   import write_obj_file,  remake_vertices
from collectdata import remake_array,    collect_data,    generate_desmos_code
from createggb   import create_template, create_ggb_file, read_obj_file,       add_point, create_polygon

sg.theme('DarkGrey9')

config_file = "config.json"
settings_file = "settings.json"

def save_settings(settings):
    with open(settings_file, "w") as file:
        json.dump(settings, file, indent=4)

def load_settings():
    try:
        with open(settings_file, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {
    "Polygon": {
      "color": {"r": 21, "g": 101, "b": 192},
      "alpha": 1,
      "label": False
    },

    "Segment": {
      "color": {"r": 21, "g": 101, "b": 192},
      "alpha": 0,
      "thickness": 0,
      "show_object": True,
      "label": False
    },

    "Point": {
      "color": {"r": 0, "g": 0, "b": 0},
      "alpha": 0,
      "pointSize": 5,
      "label": False
    }
}               

def save_folder_path(folder_path):
    config = {"folder_path" : folder_path}
    with open(config_file, "w") as file:
        json.dump(config, file)

def get_default_folder_path():
    if os.path.exists(config_file):
        with open(config_file, "r") as file:
            config = json.load(file)
            return config.get("folder_path", "")
    return ""

def create_obj(path) -> None:
    url = f'http://dmccooey.com/polyhedra/{values[0]}.txt'
    page = requests.get(url)
    data = page.text.replace('  ', ' ')
    vertices, faces, Constants = collect_data(data)
    faces = remake_array(faces)
    vertices = remake_vertices(vertices, Constants)

    write_obj_file(vertices, faces, path)

default_folder = get_default_folder_path()
settings = load_settings()

layout = [
    [sg.Text('Название фигуры'), sg.InputText()], 
    [sg.Button('Сгенерировать текст для Desmos')],
    [sg.Button('Создать GGB файл (Geogebra)'), sg.Button('Настройки')],
    [sg.Button('Создать OBJ файл (Blender, etc)')],
    [sg.Text('Выберите папку для сохранения файлов:'), sg.InputText(default_text=default_folder, key='folder_path'), sg.FolderBrowse()],
    [sg.Output(size=(70, 15))]
]

def settings_window():
    settings_layout = [
        [sg.Text('Настройки')],
        [sg.Text('Polygon:')],
        [sg.Text('Color: R'), sg.InputText(settings['Polygon']['color']['r'], size=(5, 1)), sg.Text('G'), sg.InputText(settings['Polygon']['color']['g'], size=(5, 1)), sg.Text('B'), sg.InputText(settings['Polygon']['color']['b'], size=(5, 1))],
        [sg.Text('Alpha:'), sg.InputText(settings['Polygon']['alpha'], size=(5, 1))],
        [sg.Text('Label (true/false):'), sg.InputText(settings['Polygon']['label'], size=(5, 1))],
        [sg.Text('\nSegment:')],
        [sg.Text('Color: R'), sg.InputText(settings['Segment']['color']['r'], size=(5, 1)), sg.Text('G'), sg.InputText(settings['Segment']['color']['g'], size=(5, 1)), sg.Text('B'), sg.InputText(settings['Segment']['color']['b'], size=(5, 1))],
        [sg.Text('Alpha:'), sg.InputText(settings['Segment']['alpha'], size=(5, 1))],
        [sg.Text('Thickness:'), sg.InputText(settings['Segment']['thickness'], size=(5, 1))],
        [sg.Text('Show object (true/false):'), sg.InputText(settings['Segment']['show_object'], size=(5, 1))],
        [sg.Text('Label (true/false):'), sg.InputText(settings['Segment']['label'], size=(5, 1))],
        [sg.Text('\nPoint:')],
        [sg.Text('Color: R'), sg.InputText(settings['Point']['color']['r'], size=(5, 1)), sg.Text('G'), sg.InputText(settings['Point']['color']['g'], size=(5, 1)), sg.Text('B'), sg.InputText(settings['Point']['color']['b'], size=(5, 1))],
        [sg.Text('Alpha:'), sg.InputText(settings['Point']['alpha'], size=(5, 1))],
        [sg.Text('PointSize:'), sg.InputText(settings['Point']['pointSize'], size=(5, 1))],
        [sg.Text('Label (true/false):'), sg.InputText(settings['Point']['label'], size=(5, 1))],
        [sg.Button('Save'), sg.Button('Restore Defaults')]
    ]
    settings_window = sg.Window('Settings', settings_layout)
    while True:
        event, values = settings_window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == 'Save':
            settings['Polygon']['color']['r'] = int(values[0])
            settings['Polygon']['color']['g'] = int(values[1])
            settings['Polygon']['color']['b'] = int(values[2])
            settings['Polygon']['alpha'] = float(values[3])
            settings['Polygon']['label'] = bool(int(values[4]))
            
            settings['Segment']['color']['r'] = int(values[5])
            settings['Segment']['color']['g'] = int(values[6])
            settings['Segment']['color']['b'] = int(values[7])
            settings['Segment']['alpha'] = float(values[8])
            settings['Segment']['thickness'] = int(values[9])
            settings['Segment']['show_object'] = bool(int(values[10]))
            settings['Segment']['label'] = bool(int(values[11]))
            
            settings['Point']['color']['r'] = int(values[12])
            settings['Point']['color']['g'] = int(values[13])
            settings['Point']['color']['b'] = int(values[14])
            settings['Point']['alpha'] = float(values[15])
            settings['Point']['pointSize'] = int(values[16])
            settings['Point']['label'] = bool(int(values[17]))
            
            save_settings(settings)
            sg.popup("Settings saved!")

        if event == 'Restore Defaults':
            settings['Polygon']['color']['r'] = 21
            settings['Polygon']['color']['g'] = 101
            settings['Polygon']['color']['b'] = 192
            settings['Polygon']['alpha'] = 1.0
            settings['Polygon']['label'] = False
            
            settings['Segment']['color']['r'] = 21
            settings['Segment']['color']['g'] = 101
            settings['Segment']['color']['b'] = 192
            settings['Segment']['alpha'] = 0.0
            settings['Segment']['thickness'] = 0
            settings['Segment']['show_object'] = True
            settings['Segment']['label'] = False
            
            settings['Point']['color']['r'] = 0
            settings['Point']['color']['g'] = 0
            settings['Point']['color']['b'] = 0
            settings['Point']['alpha'] = 0.0
            settings['Point']['pointSize'] = 5
            settings['Point']['label'] = False
            sg.popup("Settings restored!")

    settings_window.close()

window = sg.Window("Desmos&Geogebra helper by Timokrut", layout)


while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    
    folder_path = values['folder_path']

    if event == 'Настройки':
        settings_window()

    if len(values[0]) > 0:
        if len(folder_path) > 0:
            save_folder_path(folder_path)
            if event == 'Создать GGB файл (Geogebra)':
                try:
                    create_template(os.path.join(folder_path, f'{values[0]}_ggb_template'))

                    try:
                        verticies, faces = read_obj_file(os.path.join(folder_path, f'{values[0]}.obj'))
                    except:
                        create_obj(os.path.join(folder_path, f"{values[0]}.obj"))
                        verticies, faces = read_obj_file(os.path.join(folder_path, f'{values[0]}.obj'))

                    for number, point in enumerate(verticies):
                        name = f'V{number}'
                        add_point(name, point, os.path.join(folder_path, f'{values[0]}_ggb_template/ggb_template/geogebra.xml'))

                    for face in faces:
                        create_polygon(face, os.path.join(folder_path, f'{values[0]}_ggb_template/ggb_template/geogebra.xml'))

                    endfile = '''</construction>
                    </geogebra>'''
            
                    with open (os.path.join(folder_path, f'{values[0]}_ggb_template/ggb_template/geogebra.xml'), 'a') as file:
                        file.write(endfile)

                    source_folder = os.path.join(folder_path, f'{values[0]}_ggb_template/ggb_template')
                    target_rar = os.path.join(folder_path, f'{values[0]}.ggb')

                    if os.path.exists(os.path.join(folder_path, f"{values[0]}.ggb")):
                        os.remove(os.path.join(folder_path, f"{values[0]}.ggb"))
                    
                    create_ggb_file(source_folder, target_rar)
                    
                    os.remove(os.path.join(folder_path, f"{values[0]}.obj"))
                    shutil.rmtree(os.path.join(folder_path, f'{values[0]}_ggb_template'))

                    print('Файл GGB успешно создан')

                except Exception as e:
                    print(e)    

            if event == 'Сгенерировать текст для Desmos':
                try:
                    url = f'http://dmccooey.com/polyhedra/{values[0]}.txt'
                    page = requests.get(url)
                    soup = bs(page.text, 'html.parser')
                    data = page.text.replace('  ', ' ')
                    vertices, faces, Constants = collect_data(data)
                    new_edges = remake_array(faces)
                    desmos_code = generate_desmos_code(vertices, new_edges, Constants)
                    pyperclip.copy(desmos_code)
                    print(f"Координаты {values[0]} скопированы в буфер обмена. Зайдите в Desmos и нажмите CTRL + V")
                except Exception as e:
                    print(e)    

            if event == 'Создать OBJ файл (Blender, etc)':
                try:
                    try:
                        os.makedirs(os.path.join(folder_path, 'obj'))
                    except:
                        pass

                    create_obj(os.path.join(folder_path, f"obj/{values[0]}.obj"))
                    print(f"Object файл для {values[0]} создан")

                except Exception as e:
                    print(e)    
        else:
            print('Укажите путь')            
    else:
        print('Сначала напишите название фигуры')           

window.close
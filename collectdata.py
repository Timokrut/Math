import re
import requests
from bs4 import BeautifulSoup as bs
import pyperclip
import os

from typing import Dict

def extract_numbers(string: str) -> list[float]:
    return [int(num) for num in re.findall(r'-?\d+\.?\d*', string)]

def remake_array(arr: list[list[int]]) -> list[list[int]]:
    new_arr = []
    for subarr in arr:
        if len(subarr) <= 3:
            new_arr.append(subarr)
        else:
            new_subarr = []
            for i in range(len(subarr) - 2):
                new_subarr.append([subarr[0], subarr[i+1], subarr[i+2]])
            new_arr.extend(new_subarr)
    return new_arr

def convert_text(input_text: str) -> str:
    changed = ['C_{']
    for i in range(0, len(input_text)):
        flag = True
        if input_text[i] == '-' and flag == True:
            changed.insert(0, '-')
            flag = False

        if input_text[i] == 'C' or input_text[i] == '-':
            continue
        changed.append(input_text[i])
    changed.append('}')
    return "".join(changed)

def collect_data(data: str):
    i = 0
    Constants = dict()
    while (True):
        patternC = rf'C{i} = ([\d\.]+)'
        value = re.search(patternC, data)

        if value:
            Constants["C_{" + str(i) + "}"] = float(value.group(1))
            i += 1
        else:
            break

    j = 0
    vertices = []
    while (True):
        patternV = rf"V{j} = \(([-\d\.]+), ([-\d\.]+), ([-\d\.]+)\)"
        value = re.search(patternV, data)   
        if value:
            vertices.append([(value.group(1)), (value.group(2)), (value.group(3))])
            j += 1
        else:
            break

    faces = []
    for line in data.split('\n'):
        if line.startswith('V'):
            vertices.append([float(x.strip()) if x.isnumeric() else x.strip() for x in (line.split('=')[1].strip()[1:-1].split(', '))])  
        elif line.startswith('{'):
            faces.append(extract_numbers(line))
    
    for points in vertices:
        for i in range(len(points)):
            try: 
                float(points[i])
            except:
                points[i] = convert_text(points[i])

    return vertices, faces, Constants

def generate_desmos_code(vertices: list[list[str]], edges: list[list[int]], constants: Dict[str:float]) -> str:
    constants_code = "\n".join([f"{c} = {constants[c]}" for c in constants])

    vertices_code = ", ".join([f'({vertex[0]}, {vertex[1]}, {vertex[2]})' for vertex in vertices])
    
    edges_code = ", ".join([f"({(edge[0] + 1)}, {str(edge[1] + 1)}, {edge[2] + 1})" for edge in edges])

    desmos_code = f"{constants_code}\nP = [{vertices_code}]\nF = [{edges_code}]\n\operatorname{{triangle}}(P[F.x],P[F.y],P[F.z])"
    return desmos_code

if __name__ == "__main__":
    while True:
        name = input('Напишите название фигуры(как нас сайте): ')
        url = f'http://dmccooey.com/polyhedra/{name}.txt'
        page = requests.get(url)
        soup = bs(page.text, 'html.parser')

        data = page.text.replace('  ', ' ')

        vertices, faces, Constants = collect_data(data)

        new_edges = remake_array(faces)

        desmos_code = generate_desmos_code(vertices, new_edges, Constants)
        pyperclip.copy(desmos_code)
        print("Координаты скопированы в буфер обмена. Зайдите в Desmos и нажмите CTRL + V")

        print("Хотите ввести еще одно название(Нажмите Enter)?(Если нет - напишите n)")
        reply = input()        
        if reply.lower() == 'n':
            break
        os.system("cls")

import re
import requests # type: ignore
from bs4 import BeautifulSoup as bs # type: ignore
import numpy as np
import pyperclip
# HexagonalDipyramid


name = input('Напишите название фигуры(как нас сайте): ')
url = f'http://dmccooey.com/polyhedra/{name}.txt'
page = requests.get(url)
soup = bs(page.text, 'html.parser')

data = page.text

def extract_numbers(string):
    return [int(num) for num in re.findall(r'-?\d+\.?\d*', string)]

def collect_data(data):
    i = 0
    Constants = dict()
    while (True):
        patternC = rf'C{i} = ([\d\.]+)'
        value = re.search(patternC, data)
        if value:
            Constants[f"C_{i}"] = float(value.group(1))
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
    return vertices, faces, Constants

vertices, faces, Constants = collect_data(data)

def generate_desmos_code(vertices, edges, constants):
    constants_code = "\n".join([f"{c} = {constants[c]}" for c in constants])

    vertices_code = ", ".join([f'({vertex[0].replace("C", "C_")}, {vertex[1].replace("C", "C_")}, {vertex[2].replace("C", "C_")})' for vertex in vertices])
    
    edges_code = ", ".join([f"({', '.join(str(edge[i] + 1) for i in range(j, j + 3))})" for edge in edges for j in range(len(edge) - 2)])


    desmos_code = f"{constants_code}\nP = [{vertices_code}]\nF = [{edges_code}]\ntriangle (P[F.x], P[F.y], P[F.z])"
    return desmos_code

desmos_code = generate_desmos_code(vertices, faces, Constants)
pyperclip.copy(desmos_code)
print("Координаты скопированы в буфер обмена. Зайдите в Desmos и нажмите CTRL + V")

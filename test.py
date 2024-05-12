import requests
from bs4 import BeautifulSoup as bs
import re
from collectdata import remake_array, extract_numbers, convert_text
from shape_scan import distance, count_solution

def collect_data(data: str):
    i = 0
    Constants = dict()
    while (True):
        patternC = rf'C{i} = ([\d\.]+)'
        value = re.search(patternC, data)

        if value:
            Constants["C_{" + str(i) + "}"] = float(value.group(1))
            Constants["-C_{" + str(i) + "}"] = float(value.group(1)) * -1
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
                points[i] = Constants[convert_text(points[i])]

    return vertices, faces, Constants


name = input('Напишите название фигуры(как нас сайте): ')
url = f'http://dmccooey.com/polyhedra/{name}.txt'
page = requests.get(url)
soup = bs(page.text, 'html.parser')

data = page.text.replace('  ', ' ')

vertices, faces, Constants = collect_data(data)

first_face = faces[0]

new_edges = remake_array(faces)



amount_of_verticies = {}
print(vertices)

for i in vertices:
    amount_of_verticies[i] = 0

print(amount_of_verticies)    


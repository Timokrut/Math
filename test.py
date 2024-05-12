import requests
from bs4 import BeautifulSoup as bs
import re
from collectdata import remake_array, extract_numbers, convert_text
from shape_scan import count_solution, distance, find_sim, point_max_comp, find_number

EPSILON = 10e-8

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


# name = input('Напишите название фигуры(как нас сайте): ')
name = 'TrigonalTrapezohedron'
url = f'http://dmccooey.com/polyhedra/{name}.txt'
page = requests.get(url)
soup = bs(page.text, 'html.parser')

data = page.text.replace('  ', ' ')

vertices, faces, Constants = collect_data(data)

first_face = faces[0]

new_edges = remake_array(faces)
amount_of_verticies = {}

for i in vertices:
    amount_of_verticies[vertices.index(i)] = 0

from typing import Dict

def check_solution(solution: list[float], I: list[float], amount_of_verticies: Dict[int,int], number_of_vertice: int, compare_numb_to_I: list[int]) -> int:
    if len(solution) == 0:
        return -1
    if len(solution) == 1: 
        if solution[0] in I:
            return -1
        else:
            if amount_of_verticies[number_of_vertice] >= 1:
                idx = compare_numb_to_I.find(number_of_vertice)
                d1 = distance(I[idx], [0, 0, 0])
                d2 = distance(solution[0], [0, 0, 0])
                if d1 == d2:
                    I.append(solution[0])
                    amount_of_verticies[number_of_vertice] += 1
                else:
                    return -1     
            else:
                I.append(solution[0]) 
                amount_of_verticies[number_of_vertice] += 1

    if len(solution) == 2:
        flag = 0
        for i in solution:
            if i in I:
                flag += 1
                continue
        
            if amount_of_verticies[number_of_vertice] >= 1:
                idx = compare_numb_to_I.index(number_of_vertice)
                d1 = distance(I[idx], [0, 0, 0])
                d2 = distance(i, [0, 0, 0])
                if d1 == d2:
                    I.append(i)
                    amount_of_verticies[number_of_vertice] += 1
                else:
                    flag += 1
                    continue   
            else:
                I.append(i)
                amount_of_verticies[number_of_vertice] += 1
                return 0
        else:
            return -1 if flag == 2 else 0
            
    
if __name__ == '__main__':
    I = [[0, 0, 0]]
    compare_numb_to_I = [i for i in new_edges[0]]
    I.append([0, distance(vertices[0], vertices[compare_numb_to_I[1]]), 0])
    check_solution(count_solution(vertices[0], vertices[compare_numb_to_I[1]], vertices[compare_numb_to_I[2]], I[0], I[1]), I, amount_of_verticies, 5, compare_numb_to_I)

    for counter in range(len(new_edges)):
        verts, good_verticies = point_max_comp(new_edges, counter)
        for count, good_point in enumerate(good_verticies):
            idx_0 = []
            # if amount_of_verticies[good_point[0]] > 1:
            for i in range(len(compare_numb_to_I)):
                if compare_numb_to_I[i] == good_point[0]:
                    idx_0.append(i)
            
            idx_1 = []                    
            # if amount_of_verticies[good_point[1]] > 1:
            for i in range(len(compare_numb_to_I)):
                if compare_numb_to_I[i] == good_point[1]:
                    idx_1.append(i)

            flag = True
            for i in idx_0:
                if flag == False:
                    break
                for j in idx_1:
                    if flag and check_solution(count_solution(vertices[good_point[0]], vertices[good_point[1]], vertices[verts[count]], I[i], I[j]), I, amount_of_verticies, verts[count], compare_numb_to_I) == 0:
                        flag = False
                        break
    print(I)


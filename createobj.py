from collectdata import collect_data, remake_array
import os
import requests
from bs4 import BeautifulSoup as bs

from typing import Dict


def write_obj_file(points: list[list[str]], faces: list[list[int]], file_path: str) -> None:
    with open(file_path, 'w') as obj_file:
        for point in points:
            obj_file.write(f"v {point[0]} {point[1]} {point[2]}\n")

        for face in faces:
            obj_file.write(f"f {face[0]+1} {face[1]+1} {face[2]+1}\n")

def remake_vertices(vertices: list[list[str]], const: Dict[str,float]) -> list[list[str]]:
    remade_vertices = []
    
    for vertex in vertices:
        remade_vertex = []
        for element in vertex:
            if element.startswith('-C_{'):
                remade_vertex.append(str(-const[element[1:]]))
            elif element.startswith('C_{'):
                remade_vertex.append(str(const[element]))
            else:
                remade_vertex.append(element)
        remade_vertices.append(remade_vertex)
    
    return remade_vertices

if __name__ == "__main__":
    while True:
        name = input('Напишите название фигуры(как нас сайте): ')
        url = f'http://dmccooey.com/polyhedra/{name}.txt'
        page = requests.get(url)
        soup = bs(page.text, 'html.parser')

        data = page.text.replace('  ', ' ')

        vertices, faces, Constants = collect_data(data)
        faces = remake_array(faces)
        vertices = remake_vertices(vertices, Constants)

        write_obj_file(vertices, faces, "model.obj")

        print("Object файл создан")

        print("Хотите ввести еще одно название(Нажмите Enter)?(Если нет - напишите n)")
        reply = input()        
        if reply.lower() == 'n':
            break
        os.system("cls")

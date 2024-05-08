from sympy import symbols, Eq, solve

C0 = 0.7071067811865475244008443621048

Verticies = [[0.0, 0.0,  C0], [0.0, 0.0, -C0], [ C0, 0.0, 0.0], [-C0, 0.0, 0.0], [0.0,  C0, 0.0], [0.0, -C0, 0.0]]

F = [[0, 2, 4],[0, 4, 3],[0, 3, 5],[0, 5, 2],[1, 2, 5],[1, 5, 3],[1, 3, 4],[1, 4, 2]]

def distance(point_A: list[float], point_B: list[float]) -> float:
    return ((point_A[0] - point_B[0])**2 + (point_A[1] - point_B[1])**2 + (point_A[2] - point_B[2])**2)**0.5

#                  A - V0                B - V2                V - 4                 I[len(I) - 2]         I[len(I) - 1]
def count_solution(point_A: list[float], point_B: list[float], point_C: list[float], point_D: list[float], point_E: list[float], I : list[float]) -> None:
    x, y = symbols('x y')
    eq1 = Eq((x - point_D[0])**2 + (y - point_D[1])**2, distance(point_A, point_C)**2)
    eq2 = Eq((x - point_E[0])**2 + (y - point_E[1])**2, distance(point_B, point_C)**2)
    sol_dict = solve((eq1,eq2), (x, y))
    # print(f' (x - {point_D[0]})^2 + (y - {point_D[1]})^2 = distance ({point_A}, {point_C})^2 // {distance(point_A, point_C)}^2 ')
    # print(f' (x - {point_E[0]})^2 + (y - {point_E[1]})^2 = distance ({point_B}, {point_C})^2 // {distance(point_B, point_C)}^2 ')

    # print()
    
    solution = sol_dict[1] if sol_dict[1][0] > sol_dict[0][0] else sol_dict[0]

    # print(f'solution 1 - {sol_dict[0]}')
    # print(f'solution 2 - {sol_dict[1]}')
    # print(f'pick - {list(solution) if solution in I else list(sol_dict[0] if sol_dict[0] in I else sol_dict[1])}')
    # print()
        


    return list(solution) if solution in I else list(sol_dict[0] if sol_dict[0] in I else sol_dict[1])


def find_sim(face_A: list[int], face_B: list[int]):
    counter = 0
    for i in face_A:
        for j in face_B:
            if i == j:
                counter += 1
    return counter                

def point_max_comp(faces, counter):
    i = faces[counter]
    solutions = []
    good_vericies = []
    for j in faces[faces.index(i):]:
        if i != j:
            if find_sim(i, j) == 2:
                tmp_i = sorted(i)
                tmp_j = sorted(j)
                flag = True
                for k in range(3):
                    if  tmp_i[k] != tmp_j[k]:
                        solutions.append(tmp_j[k])
                    else:
                        if flag == True:
                            a = tmp_j[k]
                            flag = False
                        else:
                            b = tmp_j[k]
                            good_vericies.append([a, b])

    return solutions, good_vericies


def find_number(aid, goodP):
    for i in aid.keys():
        if i == goodP:
            return aid[i]


# INIT
if __name__ == '__main__':
    I = [[0, 0], [0, distance(Verticies[0], Verticies[2])]]
    I.append(count_solution(Verticies[0], Verticies[2], Verticies[4], [0, 0], [0, distance(Verticies[0], Verticies[2])], I))

    medical_aid = {
    0 : I[0],
    2 : I[1], 
    4 : I[2]
}

    for counter in range(len(F)):
        vericies, good_verticies = point_max_comp(F, counter)
        for count, good_point in enumerate(good_verticies):
            # print(f'good point - {good_point}')
            # print(f'find_num_0 - {find_number(medical_aid, good_point[0])}')
            # print(f'find_num_1 - {find_number(medical_aid, good_point[1])}')

            I.append(count_solution(Verticies[good_point[0]], Verticies[good_point[1]], Verticies[vericies[count]], find_number(medical_aid, good_point[0]), find_number(medical_aid, good_point[1]), I))
            
            medical_aid[vericies[count]] = I[-1]
            
            # print(I)
            # print(f'verticies - {vericies}')
            
            # print(f'medical aid - {medical_aid}')

            # print()
            # print()
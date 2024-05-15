from sympy import symbols, Eq, solve

def distance(point_A: list[float], point_B: list[float]) -> float:
    try:
        return round(((float(point_A[0]) - float(point_B[0]))**2 + (float(point_A[1]) - float(point_B[1]))**2 + (float(point_A[2]) - float(point_B[2]))**2)**0.5, 4)
    except:
        return 0

#                  A - V0                B - V2                V - 4                 I[len(I) - 2]         I[len(I) - 1]
def count_solution(point_A: list[float], point_B: list[float], point_C: list[float], point_D: list[float], point_E: list[float]) -> None:
    x, y = symbols('x y')
    eq1 = Eq((x**2 - 2 * x * point_D[0] + point_D[0]**2) + (y**2  - 2 * y * point_D[1] + point_D[1]**2), distance(point_A, point_C)**2)
    eq2 = Eq((x**2 - 2 * x * point_E[0] + point_E[0]**2) + (y**2  - 2 * y * point_E[1] + point_E[1]**2), distance(point_B, point_C)**2)
    sol_dict = solve((eq1,eq2), (x, y))

    answ = []
    for i in sol_dict:
        answ.append([round(i[0], 4), round(i[1], 4), 0])
    
    return answ

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

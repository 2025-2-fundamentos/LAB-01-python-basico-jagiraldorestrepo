"""
Genere una lista de tuplas, donde el primer elemento de cada tupla
contiene  el valor de la segunda columna; la segunda parte de la tupla
es una lista con las letras (ordenadas y sin repetir letra) de la
primera  columna que aparecen asociadas a dicho valor de la segunda
columna.

Rta/
[(0, ['C']),
    (1, ['B', 'E']),
    (2, ['A', 'E']),
    (3, ['A', 'B', 'D', 'E']),
    (4, ['B', 'E']),
    (5, ['B', 'C', 'D', 'E']),
    (6, ['A', 'B', 'C', 'E']),
    (7, ['A', 'C', 'D', 'E']),
    (8, ['A', 'B', 'D', 'E']),
    (9, ['A', 'B', 'C', 'E'])]

"""

import csv
def pregunta_08():
    diccionario = {}
    with open("files/input/data.csv", "r") as f:
        reader = csv.reader(f, delimiter="\t")
        for row in reader:
            clave = int(row[1])
            valor = row[0]

            if clave in diccionario:
                diccionario[clave].append(valor)

            else:
                diccionario[clave] = [valor]

    resultado = [(clave, sorted(list(set(valor)))) for clave, valor in diccionario.items() ]
    resultado.sort()
    return resultado


pregunta_08()
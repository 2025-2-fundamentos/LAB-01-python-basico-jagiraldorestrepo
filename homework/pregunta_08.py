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
from collections import defaultdict
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


def pregunta_08_mejorada():
    letras_por_valor = defaultdict(set)  #ahorra la logica de decir si existe se agrega, sino se crea
    with open("files/input/data.csv", "r") as f:
        reader = csv.reader(f, delimiter="\t")
        for row in reader:
            letra = row[0]          # columna 1 (A, B, C, ...)
            valor = int(row[1])     # columna 2 (0..9)
            letras_por_valor[valor].add(letra)

    resultado = [(valor, sorted(letras)) for valor, letras in sorted(letras_por_valor.items())]
    print(resultado)

pregunta_08_mejorada()



pregunta_08()
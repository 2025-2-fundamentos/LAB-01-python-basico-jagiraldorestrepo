"""
Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla
contiene un valor posible de la columna 2 y una lista con todas las letras
asociadas (columna 1) a dicho valor de la columna 2.

Rta/
[(0, ['C']),
(1, ['E', 'B', 'E']),
(2, ['A', 'E']),
(3, ['A', 'B', 'D', 'E', 'E', 'D']),
(4, ['E', 'B']),
(5, ['B', 'C', 'D', 'D', 'E', 'E', 'E']),
(6, ['C', 'E', 'A', 'B']),
(7, ['A', 'C', 'E', 'D']),
(8, ['E', 'D', 'E', 'A', 'B']),
(9, ['A', 'B', 'E', 'A', 'A', 'C'])]

    """
import csv

def pregunta_07():
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

    resultado = [(clave, valor) for clave, valor in diccionario.items() ]
    resultado.sort()
    return resultado


pregunta_07()
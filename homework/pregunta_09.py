"""
Retorne un diccionario que contenga la cantidad de registros en que
aparece cada clave de la columna 5.

Rta/
{'aaa': 13,
    'bbb': 16,
    'ccc': 23,
    'ddd': 23,
    'eee': 15,
    'fff': 20,
    'ggg': 13,
    'hhh': 16,
    'iii': 18,
    'jjj': 18}}

"""
import csv
from collections import Counter
def pregunta_09():
    lista_claves = []
    with open("files/input/data.csv", "r") as f:
        reader = csv.reader(f, delimiter= "\t")

        for *_, claves in reader:
            
            claves = [x.split(':')[0]  for x in claves.split(",")]
            lista_claves += claves

    conteo = Counter(lista_claves)

    return dict(sorted(conteo.items()))
pregunta_09()

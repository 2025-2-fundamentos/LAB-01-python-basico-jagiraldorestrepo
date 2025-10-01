"""
Genere un diccionario que contengan como clave la columna 1 y como valor
la suma de los valores de la columna 5 sobre todo el archivo.

Rta/
{'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

E	1	1999-02-28	b,g,f	jjj:12,bbb:3,ddd:9,ggg:8,hhh:2
"""

import csv
from collections import defaultdict, Counter


def pregunta_12():
    diccionario_sumas = defaultdict(int)

    with open("files/input/data.csv", 'r') as f:
        reader = csv.reader(f, delimiter="\t")

        for letra, *_, col5 in reader:
            suma = sum((int(x.split(':')[-1])  for x in col5.split(',')))
            diccionario_sumas[letra] += suma

    return dict(sorted(diccionario_sumas.items()))  

print(pregunta_12())      




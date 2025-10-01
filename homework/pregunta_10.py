"""
Retorne una lista de tuplas contengan por cada tupla, la letra de la
columna 1 y la cantidad de elementos de las columnas 4 y 5.

Rta/
[('E', 3, 5),
    ('A', 3, 4),
    ...
    ('E', 2, 3),
    ('E', 3, 3)]

E	1	1999-02-28	b,g,f	jjj:12,bbb:3,ddd:9,ggg:8,hhh:2
"""
import csv

def pregunta_10():
    resultado = []
    with open("files/input/data.csv", 'r') as f:
        reader = csv.reader(f, delimiter="\t")
        for letra, *_, datos1, datos2 in reader:
            datos1 = len(datos1.split(','))
            datos2 = len(datos2.split(','))
            resultado.append((letra, datos1,datos2 ))
        
    return resultado

pregunta_10()




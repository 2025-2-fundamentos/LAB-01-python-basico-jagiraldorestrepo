"""
Retorne un diccionario que contengan la suma de la columna 2 para cada
letra de la columna 4, ordenadas alfabeticamente.

Rta/
{'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}

E	1	1999-02-28	b,g,f	jjj:12,bbb:3,ddd:9,ggg:8,hhh:2
"""
import csv
from collections import defaultdict

def pregunta_11():
    suma = defaultdict(int)
    with open("files/input/data.csv", "r") as f:
        reader = csv.reader(f, delimiter="\t")

        for _, numero, _,  letras, _ in reader:
            numero = int(numero)
            
            for letra in letras.split(','):
                suma[letra] += numero

    return dict(sorted(suma.items()))
print(pregunta_11())
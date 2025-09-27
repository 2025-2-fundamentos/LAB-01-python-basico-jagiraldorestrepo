"""
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """

import csv

def pregunta_03():

    with open("files/input/data.csv", "r") as f:
        abc = {}
        reader = csv.reader(f, delimiter= "\t" )
        
    
        for row in reader:
            letra = row[0]
            valor = int(row[1])

            if letra in abc:
                abc[letra] += valor
            else:
                abc[letra] = valor

        return sorted(abc.items())

pregunta_03()

    

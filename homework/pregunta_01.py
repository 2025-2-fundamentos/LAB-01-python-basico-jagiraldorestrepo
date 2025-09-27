"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import csv


# reader como que guarda un objeto iterable del csv, 
# cada iteracion me da una lista de la fila




def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    with open("files/input/data.csv", "r") as f:
        reader = csv.reader(f, delimiter="\t") 
        total = 0
        for row in reader:
            total += int(row[1])
        
        return total



pregunta_01()




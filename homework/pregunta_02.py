import csv


"""
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """

def pregunta_02():
    with open("files/input/data.csv", "r") as f:
        abc = {}
        reader = csv.reader(f, delimiter = "\t")

        for row in reader:
            letra = row[0]
            if letra in abc:
                abc[letra] += 1
            else:
                abc[letra] = 1
        
        return sorted(abc.items())


from collections import Counter
def pregunta_02_mejor():
    with open("files/input/data.csv", "r") as f:
        
        reader = csv.reader(f, delimiter = "\t")
        letras = [row[0] for row in reader]
        conteo = Counter(letras)
    
    print(sorted(conteo.items()))



pregunta_02()









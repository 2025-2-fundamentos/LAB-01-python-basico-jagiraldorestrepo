"""
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """


import csv
def pregunta_05():
    conter = {}
    with open("files/input/data.csv", "r") as f:
        reader = csv.reader(f, delimiter="\t")

        for row in reader:
            letra = row[0]
            num = int(row[1])

            if letra in conter:
                mx,mn = conter[letra]
                if num > mx:
                    mx = num
                if num < mn:
                    mn = num
                conter[letra] = (mx,mn)

            else:
                conter[letra] = (num, num) #max,min
    resultado = [(letra, mx, mn) for letra, (mx,mn) in conter.items()]
    resultado.sort(key=lambda t: t[0])
    return resultado


print(pregunta_05())


    

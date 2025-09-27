"""
La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la
cantidad de registros por cada mes, tal como se muestra a continuación.

    Rta/
    [('01', 3),
    ('02', 4),
    ('03', 2),
    ('04', 4),
    ('05', 3),
    ('06', 3),
    ('07', 5),
    ('08', 6),
    ('09', 3),
    ('10', 2),
    ('11', 2),
    ('12', 3)]

"""
import csv
from collections import Counter
def pregunta_04():

    with open("files/input/data.csv", "r") as f:
        reader = csv.reader(f, delimiter="\t")

        meses = [row[2].split("-")[1] for row in reader]
        conteo = Counter(meses)
        
        return sorted(conteo.items())

    


pregunta_04()
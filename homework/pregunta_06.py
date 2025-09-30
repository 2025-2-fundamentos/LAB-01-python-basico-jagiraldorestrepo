"""
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """
import csv
def pregunta_06():
    conteo={}
    with open("files/input/data.csv","r") as f:
        reader = csv.reader(f, delimiter='\t')
        for row in reader:
            fila = row[4].split(',')
            for par in fila:
                clave = par.split(':')[0]
                valor = int(par.split(':')[1])
                if clave not in conteo:
                    conteo[clave] =(valor, valor) #min, max

                else:
                    mn,mx = conteo[clave]
                    if valor > mx:
                        mx = valor
                    if valor < mn:
                        mn = valor
                    
                    conteo[clave] = (mn,mx)

        
        resultado = [(clave, minimo, maximo) for clave, (minimo,maximo) in conteo.items()]
        resultado.sort()
        
        return resultado    
    
pregunta_06()


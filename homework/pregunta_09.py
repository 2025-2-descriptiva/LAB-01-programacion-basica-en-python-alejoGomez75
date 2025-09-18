"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_09():
    """
    Retorne un diccionario con la cantidad de registros
    en que aparece cada clave de la columna 5.
    """
    conteo = {}

    with open("files/input/data.csv", "r", encoding="utf-8") as file:
        for line in file:
            columnas = line.strip().split("\t")
            col5 = columnas[4]         
            pares = col5.split(",")     

            for par in pares:
                clave = par.split(":")[0]   
                if clave in conteo:
                    conteo[clave] += 1
                else:
                    conteo[clave] = 1

    return dict(sorted(conteo.items()))  


if __name__ == "__main__":
    print(pregunta_09())

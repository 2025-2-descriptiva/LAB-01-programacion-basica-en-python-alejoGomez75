"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_10():
    """
    Retorne una lista de tuplas donde cada tupla contiene:
    - Letra de la columna 1
    - Cantidad de elementos en la columna 4
    - Cantidad de elementos en la columna 5
    """
    resultado = []

    with open("files/input/data.csv", "r", encoding="utf-8") as file:
        for line in file:
            columnas = line.strip().split("\t")
            letra = columnas[0]             
            col4 = columnas[3].split(",")     
            col5 = columnas[4].split(",")   

            resultado.append((letra, len(col4), len(col5)))

    return resultado


if __name__ == "__main__":
    print(pregunta_10())

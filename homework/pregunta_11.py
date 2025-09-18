"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():
    """
    Retorne un diccionario que contenga la suma de la columna 2
    para cada letra de la columna 4, ordenadas alfabéticamente.
    """
    suma_por_letra = {}

    with open("files/input/data.csv", "r", encoding="utf-8") as file:
        for line in file:
            columnas = line.strip().split("\t")
            numero = int(columnas[1])      
            letras = columnas[3].split(",")  

            for letra in letras:
                if letra in suma_por_letra:
                    suma_por_letra[letra] += numero
                else:
                    suma_por_letra[letra] = numero

    return dict(sorted(suma_por_letra.items()))


if __name__ == "__main__":
    print(pregunta_11())


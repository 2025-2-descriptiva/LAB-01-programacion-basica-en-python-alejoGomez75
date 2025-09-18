"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contenga como clave la columna 1 (letra)
    y como valor la suma de los valores de la columna 5 en todo el archivo.
    """
    suma_por_letra = {}

    with open("files/input/data.csv", "r", encoding="utf-8") as file:
        for line in file:
            columnas = line.strip().split("\t")
            letra = columnas[0]            
            col5 = columnas[4].split(",")  

            total_valores = 0
            for par in col5:
                clave, valor = par.split(":")
                total_valores += int(valor)

            if letra in suma_por_letra:
                suma_por_letra[letra] += total_valores
            else:
                suma_por_letra[letra] = total_valores

    return dict(sorted(suma_por_letra.items()))


if __name__ == "__main__":
    print(pregunta_12())


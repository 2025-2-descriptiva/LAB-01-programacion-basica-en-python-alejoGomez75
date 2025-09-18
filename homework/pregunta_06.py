"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    """
    La columna 5 codifica un diccionario con pares clave:valor.
    Retorne para cada clave el valor mínimo y máximo encontrados en todo el archivo.
    """
    min_max_por_clave = {}

    with open("files/input/data.csv", "r", encoding="utf-8") as file:
        for line in file:
            columnas = line.strip().split("\t")
            col5 = columnas[4]  
            pares = col5.split(",")  

            for par in pares:
                clave, valor = par.split(":")
                valor = int(valor)

                if clave not in min_max_por_clave:
                    min_max_por_clave[clave] = [valor, valor]  
                else:
                    if valor < min_max_por_clave[clave][0]:
                        min_max_por_clave[clave][0] = valor
                    if valor > min_max_por_clave[clave][1]:
                        min_max_por_clave[clave][1] = valor

    resultado = sorted([(clave, vals[0], vals[1]) for clave, vals in min_max_por_clave.items()])

    return resultado


if __name__ == "__main__":
    print(pregunta_06())


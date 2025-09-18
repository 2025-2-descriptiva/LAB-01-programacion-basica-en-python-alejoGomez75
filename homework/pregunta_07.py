"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 2 y 1.
    Cada tupla contiene un valor de la columna 2 y una lista
    con todas las letras asociadas a ese valor.
    """
    asociaciones = {}

    with open("files/input/data.csv", "r", encoding="utf-8") as file:
        for line in file:
            columnas = line.strip().split("\t")
            letra = columnas[0]          
            numero = int(columnas[1])  

            if numero not in asociaciones:
                asociaciones[numero] = [letra]
            else:
                asociaciones[numero].append(letra)

    resultado = sorted(asociaciones.items())

    return resultado


if __name__ == "__main__":
    print(pregunta_07())

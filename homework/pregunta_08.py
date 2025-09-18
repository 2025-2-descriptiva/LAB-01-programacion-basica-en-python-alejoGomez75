"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_08():
    """
    Genere una lista de tuplas:
    - El primer elemento de cada tupla es el valor de la segunda columna (número).
    - El segundo elemento es una lista ORDENADA y SIN REPETIDOS
      de las letras de la primera columna asociadas a ese número.
    """
    asociaciones = {}

    with open("files/input/data.csv", "r", encoding="utf-8") as file:
        for line in file:
            columnas = line.strip().split("\t")
            letra = columnas[0]          
            numero = int(columnas[1])    

            if numero not in asociaciones:
                asociaciones[numero] = set()   
            asociaciones[numero].add(letra)    

    resultado = []
    for numero, letras in asociaciones.items():
        resultado.append((numero, sorted(list(letras))))

    resultado = sorted(resultado)

    return resultado


if __name__ == "__main__":
    print(pregunta_08())


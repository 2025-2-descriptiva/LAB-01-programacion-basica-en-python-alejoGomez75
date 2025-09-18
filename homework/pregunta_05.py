"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor máximo y mínimo de la columna 2
    por cada letra de la columna 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]
    """
    valores = {}

    with open("files/input/data.csv", "r", encoding="utf-8") as file:
        for line in file:
            columnas = line.strip().split("\t")
            letra = columnas[0]        
            numero = int(columnas[1])  

            if letra not in valores:
                valores[letra] = [numero, numero]  
            else:
               
                if numero > valores[letra][0]:
                    valores[letra][0] = numero
                if numero < valores[letra][1]:
                    valores[letra][1] = numero

    resultado = sorted([(letra, maximo, minimo) for letra, (maximo, minimo) in valores.items()])

    return resultado


if __name__ == "__main__":
    print(pregunta_05())

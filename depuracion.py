# Tipos de Errores

# Errores de Sintaxis
# print("Hola Mundo)

# Errores Tiempo de Ejecución
# num = 0
# print(1 / num)

# Errores Lógicos


# def suma(a, b):
#    return a - b


# print(suma(5, 3))


# Uso del print para depurar
"""
def calcular_promedio(notas):
    print("Notas", notas)
    total = 0
    for nota in notas:
        total += nota
    print("Total", total)
    promedio = total / len(notas)
    print("Promedio", promedio)
    return promedio


notas = [8, 9, 7, 6]
promedio = calcular_promedio(notas)

"""

# Uso del módulo pdb para depurar (Python Debugger)


# import pdb
# pdb.set_trace()


# n: para avanzar a la siguiente línea
# c: para continuar la ejecución
# q: para salir


def calcular_promedio(notas):
    import pdb

    pdb.set_trace()

    total = 0
    for nota in notas:
        total += nota
    promedio = total / len(notas)
    return promedio


notas = [8, 9, 7, 6]
promedio = calcular_promedio(notas)

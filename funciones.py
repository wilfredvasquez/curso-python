# DRY - Don't repeat yourself - No te repitas

"""
def nombre_funcion():
    pass
"""

"""
# Definirla
def saludar():
    print("Hola a todos")


# Llamarla
saludar()
"""

"""
# Definirla
def saludar(name):
    print(f"Hola {name}")


# Llamarla
nombre = "Pepe"
saludar(nombre)

saludar("Trueno")
"""

"""
def suma(num1, num2):
    return num1 + num2


resultado = suma(5, 8)
print(f"Resultado {resultado}")
print(suma(10, 5))
"""
"""
y = 11


def ejemplo():
    x = 10
    print(x)
    print(y)


ejemplo()
# print(x)
print(y)
"""

suma = lambda num1, num2: num1 + num2
multiplicacion = lambda num1, num2: num1 * num2

resultado = suma(5, 6)
print(resultado)

print(multiplicacion(10, 5))

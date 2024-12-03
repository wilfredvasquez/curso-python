"""try:
    numero = int(input("Ingrese un número: "))
    print(10 / numero)
except ZeroDivisionError:
    print("Error! no se puede dividir entre cero")
except ValueError:
    print("Error! debe ingresar un número válido")
finally:
    print("Gracias por usar nuestro programa")
"""

"""
try:
    numero = int(input("Ingrese un número: "))
    print(10 / numero)
except Exception as error:
    print(f"Lo siento, ha ocurrido un error: {error}")
"""


class NoNegative(Exception):
    pass


def check_number(num):
    if num < 0:
        raise NoNegative("El número no puede ser negativo")
    return num


try:
    numero = int(input("Ingrese un número: "))
    numero = check_number(numero)
    print(10 / numero)
except NoNegative:
    print("Error! El número ingresado es negativo")

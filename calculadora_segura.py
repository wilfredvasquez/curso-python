def calculadora(a, b, operacion):
    try:
        if operacion == "+":
            return a + b
        elif operacion == "-":
            return a - b
        elif operacion == "*":
            return a * b
        elif operacion == "/":
            return a / b
        else:
            return "Operación no válida"
    except ZeroDivisionError:
        return "No se puede dividir entre cero"
    except TypeError:
        return "Debe ingresar sólo números"


print(calculadora(5, 3, "+"))
print(calculadora(5, 3, "-"))
print(calculadora(5, 3, "*"))
print(calculadora(5, 3, "/"))
print(calculadora(5, 3, "p"))
print(calculadora(5, 0, "/"))
print(calculadora(5, "k", "/"))

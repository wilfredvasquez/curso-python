def calculadora(a, b, operacion):
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


print(calculadora(5, 3, "+"))
print(calculadora(5, 3, "-"))
print(calculadora(5, 3, "*"))
print(calculadora(5, 3, "/"))
print(calculadora(5, 3, "p"))

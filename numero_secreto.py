secret_number = 7

print("Bienvenido al juego de adivinanza")
print("Tienes que adivinar un número entre el 1 y 10")

attemp = None

while attemp != secret_number:
    attemp = int(input("Adivina el número: "))

    if attemp < secret_number:
        print("El número es más alto")
    elif attemp > secret_number:
        print("El número es más bajo")

print("Felicitaciones, Adivinaste")

frase = input("Ingresa una frase: ")

# Convertir a minúscula
print(f"En minúscula: {frase.lower()}")

# Contar palabras
palabras = frase.split(" ")
print(f"Número de palabras: {len(palabras)}")

# Reemplazar vocales
vocales = "aeiouAEIUO"
for vocal in vocales:
    frase = frase.replace(vocal, "*")

print(f"Frase con vocales reemplazadas: {frase}")

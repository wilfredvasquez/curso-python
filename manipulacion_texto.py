"""# Concatenación
saludo = "Hola"
nombre = "Pepe"
mensaje = saludo + ", " + nombre
print(mensaje)

# print("Hola" + 5)

# Repetición
eco = "Hola! " * 3
print(eco)

# Índice y slices
texto = "Python"
primera = texto[0]
print(primera)
ultima = texto[5]
print(ultima)
ultimo = texto[-1]
print(ultimo)
penultimo = texto[-2]
print(penultimo)

print(texto[1] + texto[2] + texto[3] + texto[4])
print(texto[1:5])
"""

"""
# Mayúscula o minúscula
texto = "Hola Mundo"

print(texto.upper())
print(texto.lower())

# Eliminar espacios
lenguaje = "   Python   "
print(lenguaje)
print(lenguaje.strip())

# Reemplazar texto
texto = "Me gusta Python"
print(texto)
print(texto.replace("Python", "programar"))

# Dividir y unirlas
saludo = "Hola como estas?"
palabras = saludo.split(" ")
print(palabras)
email = "pepetrueno@example.com"
print(email.split("@"))
print(email.split("@")[0])

union = "-".join(palabras)
print(union)
"""

# Formateo
nombre = "Pepe"
edad = 25

# format
mensaje = "Me llamo {} y tengo {} años".format(nombre, edad)
print(mensaje)

# f-string
mensaje2 = f"Me llamo {nombre} y tengo {edad} años"
print(mensaje2)

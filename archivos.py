# Modos de apertura
"""
'r' -> Leer un archivo
'w' -> Escribir en un archivo (Sobreescribe el contenido)
'a' -> Agregar un contenido al final del archivo
'r+' -> Leer y escribir el archivo.
"""

"""
# Apertura de archivo
archivo = open("mi_archivo.txt", "r")
# Manipulación del archivo
archivo.close()
"""

"""
# Leer archivo
archivo = open("mi_archivo.txt", "r")
# contenido = archivo.read()
# print(contenido)

# for line in archivo:
#    print(line.strip())

# print(archivo.readline())
# print(archivo.readline())

lista = archivo.readlines()
for line in lista:
    print(line)
print(lista)

archivo.close()
"""

"""
# Escribir archivo
archivo = open("mi_archivo.txt", "w")
archivo.write("\nBienvenidos")
archivo.write("\nCódigo que Transforma")
archivo.close()
"""

"""
# Actualizar
# Escribir archivo
archivo = open("mi_archivo.txt", "a")
archivo.write("\nBienvenidos")
archivo.write("\nCódigo que Transforma")
archivo.close()
"""

"""
# Actualizar
# Escribir archivo
archivo = open("mi_archivo.txt", "r+")
contenido = archivo.read()
print(contenido)
archivo.write("\nBienvenidos")
archivo.write("\nCódigo que Transforma")
archivo.close()
"""

"""
# Context Managers
with open("mi_archivo.txt", "r+") as archivo:
    contenido = archivo.read()
    print(contenido)

print("Finalizar")
"""

try:
    with open("mi_archivo_new.txt", "w") as archivo:
        archivo.write("Información importante")
except FileNotFoundError:
    print("El archivo no existe.")

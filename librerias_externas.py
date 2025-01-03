# Algunas librerías externas
# ---------------------------------------------------------

# numpy: para operaciones matemáticas y manejo de arreglos.
# matplotlib: para crear gráficos.
# pandas: para análisis de datos.
# requests: para realizar solicitudes HTTP.

# Creación de entorno virtual
# ---------------------------------------------------------


# virtualenv mi_entorno


# Para linux y Mac
# source mi_entorno/bin/activate


# Para Windows
# mi_entorno\Scripts\activate


# pip para gestionar paquetes de Python
# ---------------------------------------------------------


# Instalación de librerías
# pip install nombre_paquete


# Ver librerías instaladas
# pip freeze
# pip list


# Actualizar librería
# pip install --upgrade nombre_paquete


# Desinstalar librería
# pip uninstall nombre_paquete

# Usar la librerías
# ---------------------------------------------------------

"""
import numpy as np

# Crear un arreglo
arreglo = np.array([1, 2, 3, 4, 5])

# Operaciones básicas
print("Arreglo original:", arreglo)
print("Suma:", np.sum(arreglo))
print("Promedio:", np.mean(arreglo))
print("Raiz Cuadrada:", np.sqrt(arreglo))
"""

import matplotlib.pyplot as plt


# Datos
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]


# Crear el gráfico
plt.plot(x, y, marker="o", color="blue", label="Línea de ejemplo")


# Personalizar
plt.title("Gráfico de ejemplo")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.legend()


# Mostrar el gráfico
plt.show()

"""
import math

print(math.sqrt(16))
print(math.pi)
"""

"""
from math import sqrt, pi

pi = 3.1416

print(sqrt(16))
print(pi)
"""

"""
import math as m

print(m.sqrt(16))
print(m.pi)
"""

import mi_modulo as mm

# from mi_paquete import calculadora as cal, cortesia as cor
from mi_paquete.calculadora import restar
from mi_paquete.cortesia import presentarse

# print(mm.suma(4, 5))
# print(mm.saludo("Juan"))

print(restar(10, 2))
print(presentarse("Juan"))

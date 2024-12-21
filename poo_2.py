class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        print(f"Hola soy {self.nombre} y tengo {self.edad} años.")

    def caminar(self, distancia):
        print(f"Voy a caminar {distancia} metros.")

    def caminar_educado(self, distancia):
        self.presentarse()
        self.caminar(distancia)


class Estudiante(Persona):
    def __init__(self, nombre, edad, nro_carnet):
        super().__init__(nombre, edad)
        self.nro_carnet = nro_carnet
        self.__calificaciones = []

    def estudiando(self):
        print(f"Estoy estudiando.")

    def presentarse(self):
        print(f"Soy el estudiante {self.nombre} y tengo {self.edad} años.")

    def caminar(self, distancia):
        super().caminar(distancia)
        print("Hasta luego")

    def agregar_calificacion(self, calificacion):
        if type(calificacion) in [int, float]:
            self.__calificaciones.append(calificacion)
        else:
            print("La calificación debe ser un número.")
        return None

    def mostrar_calificaciones(self):
        print(self.__calificaciones)

    def promedio(self):
        return sum(self.__calificaciones) / len(self.__calificaciones)


pepe = Persona("Pepe", 50)
jose = Estudiante("José", 20, "E123456")

pepe.presentarse()
jose.presentarse()

jose.estudiando()
# pepe.estudiando()
jose.caminar(10)

jose.nombre = "José Luis"
print(jose.nombre)

# jose.__calificaciones.append(20)
# jose.__calificaciones.append("A")
# print(jose.__calificaciones)

jose.agregar_calificacion(20)
jose.agregar_calificacion(18)
jose.agregar_calificacion("A")

jose.mostrar_calificaciones()

print("El promedio es:", jose.promedio())

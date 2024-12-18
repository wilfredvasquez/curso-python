nombre = "Pepe"


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


jose = Persona("José", 20)
print(jose.nombre)
jose.nombre = "José Perez"
print(jose.nombre)

jose.presentarse()
jose.caminar(100)
jose.caminar_educado(1000)

pepe = Persona("Pepe", 50)
pepe.presentarse()

miguel = Persona("Miguel", 30)
miguel.caminar(500)

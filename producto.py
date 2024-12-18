class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def aplicar_descuento(self, porcentaje):
        descuento = self.precio * porcentaje / 100
        return self.precio - descuento


laptop = Producto("Laptop", 1000)
precio_final = laptop.aplicar_descuento(10)  # Descuento del 10%
print(f"El precio final del producto {laptop.nombre} es {precio_final}")

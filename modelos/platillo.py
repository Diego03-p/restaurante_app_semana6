from modelos.producto import Producto

# Clase hija que representa un platillo del restaurante
class Platillo(Producto):
    def __init__(self, nombre, precio, disponible, calorias):
        super().__init__(nombre, precio, disponible)
        self.calorias = calorias

    # Sobrescribe el método de la clase padre
    def mostrar_informacion(self):
        disponibilidad = "Sí" if self.disponible else "No"

        return (
            "===== PLATILLO =====\n"
            f"Nombre: {self.nombre}\n"
            f"Precio: ${self.obtener_precio():.2f}\n"
            f"Disponible: {disponibilidad}\n"
            f"Calorías: {self.calorias}"
        )
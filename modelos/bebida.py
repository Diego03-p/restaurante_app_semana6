from modelos.producto import Producto

# Clase hija que representa una bebida del restaurante
class Bebida(Producto):
    def __init__(self, nombre, precio, disponible, volumen):
        super().__init__(nombre, precio, disponible)
        self.volumen = volumen

    # Sobrescribe el método de la clase padre
    def mostrar_informacion(self):
        disponibilidad = "Sí" if self.disponible else "No"

        return (
            "===== BEBIDA =====\n"
            f"Nombre: {self.nombre}\n"
            f"Precio: ${self.obtener_precio():.2f}\n"
            f"Disponible: {disponibilidad}\n"
            f"Volumen: {self.volumen} ml"
        )
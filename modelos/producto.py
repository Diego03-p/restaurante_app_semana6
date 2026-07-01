# Clase padre que representa un producto del restaurante

class Producto:
    def __init__(self, nombre, precio, disponible):
        self.nombre = nombre
        self.__precio = precio
        self.disponible = disponible

    # Método para obtener el precio
    def obtener_precio(self):
        return self.__precio

    # Método para cambiar el precio con validación
    def cambiar_precio(self, nuevo_precio):
        if nuevo_precio > 0:
            self.__precio = nuevo_precio
        else:
            print("El precio debe ser mayor que cero.")

    # Método que será sobrescrito por las clases hijas
    def mostrar_informacion(self):
        disponibilidad = "Sí" if self.disponible else "No"
        return (
            f"Nombre: {self.nombre}\n"
            f"Precio: ${self.__precio:.2f}\n"
            f"Disponible: {disponibilidad}"
        )
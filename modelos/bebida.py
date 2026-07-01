from modelos.producto import Producto

class Bebida(Producto):
    def __init__(self, nombre: str, precio: float, tamaño: str) -> None:
        super().__init__(nombre, precio)
        self.tamaño: str = tamaño

    def mostrar_informacion(self) -> str:
        return f"Bebida: {self.nombre} - Tamaño: {self.tamaño} - Precio: {self.obtener_precio()}"
from modelos.producto import Producto

class Platillo(Producto):
    def __init__(self, nombre: str, precio: float, tipo: str) -> None:
        super().__init__(nombre, precio)
        self.tipo: str = tipo

    def mostrar_informacion(self) -> str:
        return f"Platillo: {self.nombre} - Tipo: {self.tipo} - Precio: {self.obtener_precio()}"
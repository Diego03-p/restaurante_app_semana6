from typing import Any

class Producto:
    def __init__(self, nombre: str, precio: float) -> None:
        self.nombre: str = nombre
        self.__precio: float = precio

    def obtener_precio(self) -> float:
        return self.__precio

    def cambiar_precio(self, nuevo_precio: float) -> None:
        if nuevo_precio > 0:
            self.__precio = nuevo_precio

    def mostrar_informacion(self) -> str:
        return f"Producto: {self.nombre} - Precio: {self.__precio}"
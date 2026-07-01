from typing import List
from modelos.producto import Producto

class Restaurante:
    def __init__(self) -> None:
        self.productos: List[Producto] = []

    def agregar_producto(self, producto: Producto) -> None:
        self.productos.append(producto)

    def mostrar_menu(self) -> None:
        for producto in self.productos:
            print(producto.mostrar_informacion())
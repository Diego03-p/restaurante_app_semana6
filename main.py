from servicios.restaurante import Restaurante
from modelos.platillo import Platillo
from modelos.bebida import Bebida

restaurante = Restaurante()

p1 = Platillo("Pizza", 8.5, "Italiana")
p2 = Platillo("Hamburguesa", 6.0, "Rápida")

b1 = Bebida("Coca Cola", 1.5, "Grande")
b2 = Bebida("Jugo Natural", 2.0, "Mediano")

restaurante.agregar_producto(p1)
restaurante.agregar_producto(p2)
restaurante.agregar_producto(b1)
restaurante.agregar_producto(b2)

restaurante.mostrar_menu()
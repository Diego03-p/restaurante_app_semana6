from modelos.platillo import Platillo
from modelos.bebida import Bebida
from servicios.restaurante import Restaurante

# Crear el restaurante
restaurante = Restaurante()

# Crear dos platillos
platillo1 = Platillo("Arroz con Pollo", 6.50, True, 750)
platillo2 = Platillo("Encebollado", 5.75, True, 680)

# Crear dos bebidas
bebida1 = Bebida("Jugo de Naranja", 2.50, True, 500)
bebida2 = Bebida("Gaseosa", 1.75, False, 355)

# Agregar los productos al restaurante
restaurante.agregar_producto(platillo1)
restaurante.agregar_producto(platillo2)
restaurante.agregar_producto(bebida1)
restaurante.agregar_producto(bebida2)

# Cambiar el precio de un producto
platillo1.cambiar_precio(7.00)

# Mostrar todos los productos
restaurante.mostrar_productos()
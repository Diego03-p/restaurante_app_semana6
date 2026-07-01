# Restaurante App - Semana 6

## Nombre del estudiante

Diego Pluas

## Descripción del sistema

Este proyecto corresponde a la tarea de la Semana 6 de Programación Orientada a Objetos. Se desarrolló un sistema de restaurante utilizando Python, aplicando los principios de herencia, encapsulación y polimorfismo mediante una estructura modular.

## Estructura del proyecto

```
restaurante_app_semana6
│
├── modelos
│   ├── producto.py
│   ├── platillo.py
│   └── bebida.py
│
├── servicios
│   └── restaurante.py
│
└── main.py
```

## Herencia

La clase `Producto` es la clase padre. Las clases `Platillo` y `Bebida` heredan de `Producto` utilizando `super()` para reutilizar los atributos comunes.

## Encapsulación

El atributo `__precio` fue encapsulado para proteger su acceso. Se utilizan los métodos `obtener_precio()` y `cambiar_precio()` para consultar y modificar el precio, validando que siempre sea mayor que cero.

## Polimorfismo

Las clases `Platillo` y `Bebida` sobrescriben el método `mostrar_informacion()`. La clase `Restaurante` recorre una lista de productos y ejecuta ese método, mostrando información diferente según el tipo de objeto.

## Reflexión

La programación orientada a objetos facilita la organización del código, mejora la reutilización mediante la herencia, protege la información con encapsulación y permite implementar comportamientos diferentes mediante polimorfismo.
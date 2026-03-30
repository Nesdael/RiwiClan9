# 11 - Programación Orientada a Objetos (POO)

## Concepto
La POO permite organizar el código en "objetos" que tienen propiedades y comportamientos.

## Analogía sencilla
Imagina un auto: tiene atributos (color, marca) y métodos (arrancar, frenar).

## Estructura básica
- Clase: plantilla para crear objetos
- Atributos: características
- Métodos: acciones
- Encapsulación: ocultar detalles internos

## Ejemplo explicado
```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre  # atributo
        self.edad = edad      # atributo
    def saludar(self):       # método
        print(f"Hola, soy {self.nombre}")

ana = Persona("Ana", 25)
ana.saludar()
```

## Errores comunes
- Olvidar el self
- No usar __init__
- Acceder a atributos inexistentes

## Buenas prácticas
- Nombres claros para clases y métodos
- Documentar clases
- Usar encapsulación básica

## Ejercicios prácticos
1. Crea una clase Auto con atributos marca y modelo, y un método mostrar_info.
2. Haz una clase Estudiante con método estudiar.

## Mini reto
Haz una clase CuentaBancaria con métodos para depositar y retirar dinero.
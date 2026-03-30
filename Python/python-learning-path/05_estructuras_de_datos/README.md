# 05 - Estructuras de Datos en Python

## Concepto
Las estructuras de datos permiten organizar y almacenar información de diferentes formas.

## Analogía sencilla
Imagina una caja de herramientas: cada compartimento es una estructura diferente para guardar cosas.

## Tipos principales
- Listas: colecciones ordenadas y modificables
- Tuplas: colecciones ordenadas e inmutables
- Diccionarios: pares clave-valor
- Sets: colecciones únicas y desordenadas

## Ejemplo explicado
```python
# Lista
frutas = ["manzana", "pera", "uva"]
print(frutas[0])  # manzana

# Tupla
coordenadas = (10, 20)
print(coordenadas[1])  # 20

# Diccionario
persona = {"nombre": "Ana", "edad": 25}
print(persona["nombre"])

# Set
numeros = {1, 2, 3, 3}
print(numeros)  # {1, 2, 3}
```

## Errores comunes
- Acceder a índices inexistentes
- Modificar tuplas (no se puede)
- Duplicar elementos en sets

## Buenas prácticas
- Usar la estructura adecuada según el caso
- Nombres descriptivos

## Ejercicios prácticos
1. Crea una lista de tus comidas favoritas.
2. Crea un diccionario con tu nombre y edad.

## Mini reto
Haz un set con los números del 1 al 5 y agrega el número 3 dos veces. ¿Qué sucede?
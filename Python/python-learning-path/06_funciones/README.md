# 06 - Funciones en Python

## Concepto
Una función es un bloque de código que realiza una tarea específica y puede ser reutilizado.

## Analogía sencilla
Piensa en una receta: sigues pasos definidos para obtener un resultado. Una función es una receta en el código.

## Estructura básica
- Definición: `def nombre_funcion(parámetros):`
- Retorno: `return valor`
- Docstring: descripción de la función

## Ejemplo explicado
```python
def saludar(nombre):
    """Imprime un saludo personalizado"""
    print(f"Hola, {nombre}!")

saludar("Ana")

# Función con retorno
def suma(a, b):
    """Devuelve la suma de dos números"""
    return a + b

resultado = suma(3, 5)
print("Resultado:", resultado)
```

## Errores comunes
- Olvidar el return
- No pasar todos los parámetros
- No usar docstrings

## Buenas prácticas
- Nombres descriptivos
- Documentar funciones
- Evitar funciones demasiado largas

## Ejercicios prácticos
1. Crea una función que reciba tu edad y devuelva si eres mayor de edad.
2. Escribe una función que calcule el área de un círculo.

## Mini reto
Haz una función que reciba una lista de nombres y salude a cada uno.
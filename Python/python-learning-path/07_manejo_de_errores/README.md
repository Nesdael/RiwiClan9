# 07 - Manejo de Errores en Python

## Concepto
El manejo de errores permite controlar situaciones inesperadas en el código.

## Analogía sencilla
Imagina un paracaídas: si algo falla, te ayuda a aterrizar sin problemas. Así funciona el manejo de errores.

## Estructura básica
- `try`: intenta ejecutar el código
- `except`: captura el error
- `finally`: ejecuta siempre, haya error o no

## Ejemplo explicado
```python
try:
    numero = int(input("Ingresa un número: "))
    print("Número ingresado:", numero)
except ValueError:
    print("Eso no es un número válido.")
finally:
    print("Fin del programa.")
```

## Errores comunes
- No especificar el tipo de error
- Olvidar el finally
- Capturar todos los errores sin control

## Buenas prácticas
- Capturar solo los errores necesarios
- Mostrar mensajes claros
- Usar finally para limpiar recursos

## Ejercicios prácticos
1. Haz un programa que pida un número y maneje el error si el usuario ingresa texto.
2. Usa try-except para abrir un archivo que no existe.

## Mini reto
Crea una función que divida dos números y maneje el error si el divisor es cero.
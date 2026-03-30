# 09 - Librerías Estándar en Python

## Concepto
Las librerías estándar son módulos incluidos en Python para realizar tareas comunes.

## Analogía sencilla
Imagina una caja de herramientas con funciones listas para usar: no necesitas construirlas desde cero.

## Librerías principales
- `random`: números aleatorios
- `datetime`: fechas y horas
- `math`: operaciones matemáticas
- `requests`: (instalar) para hacer peticiones web

## Ejemplo explicado
```python
import random
print(random.randint(1, 10))  # Número aleatorio entre 1 y 10

import datetime
print(datetime.datetime.now())  # Fecha y hora actual

import math
print(math.sqrt(16))  # Raíz cuadrada

# requests requiere instalación
# import requests
# r = requests.get('https://api.github.com')
# print(r.status_code)
```

## Errores comunes
- Olvidar instalar librerías externas
- Escribir mal el nombre del módulo
- No leer la documentación

## Buenas prácticas
- Importar solo lo necesario
- Leer la documentación oficial

## Ejercicios prácticos
1. Usa random para simular el lanzamiento de un dado.
2. Muestra la fecha actual con datetime.

## Mini reto
Haz un programa que calcule la raíz cuadrada de un número ingresado por el usuario.
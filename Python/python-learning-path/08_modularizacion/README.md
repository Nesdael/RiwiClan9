# 08 - Modularización en Python

## Concepto
La modularización consiste en dividir el código en archivos y funciones reutilizables.

## Analogía sencilla
Piensa en un rompecabezas: cada pieza es un módulo que se une para formar el programa completo.

## Estructura básica
- Importar módulos: `import nombre_modulo`
- Crear archivos reutilizables: funciones en archivos separados
- Organización de proyectos: carpetas y archivos

## Ejemplo explicado
Supón que tienes un archivo `utils.py`:
```python
def saludar():
    print("Hola desde utils!")
```
Y un archivo `main.py`:
```python
import utils
utils.saludar()
```

## Errores comunes
- Olvidar el archivo `__init__.py` en proyectos grandes
- Escribir mal el nombre del módulo
- No usar rutas relativas

## Buenas prácticas
- Separar funciones por archivo
- Usar nombres claros para módulos
- Documentar cada módulo

## Ejercicios prácticos
1. Crea un archivo `utils.py` con una función que sume dos números.
2. Importa y usa esa función desde `main.py`.

## Mini reto
Haz un módulo que tenga una función para saludar y otra para despedir. Úsalas desde otro archivo.
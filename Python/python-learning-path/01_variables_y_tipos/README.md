# 01 - Variables y Tipos de Datos

## Concepto
Una variable es un espacio en memoria donde guardamos información. Los tipos de datos indican qué clase de información almacena.

## Analogía sencilla
Piensa en una variable como una caja etiquetada: puede contener números, palabras o valores de sí/no.

## Tipos básicos en Python
- `int`: números enteros (ej. 5)
- `float`: números decimales (ej. 3.14)
- `str`: cadenas de texto (ej. "hola")
- `bool`: valores lógicos (True/False)

## Ejemplo explicado
```python
# Definición de variables
edad = 25         # int
altura = 1.75     # float
nombre = "Ana"    # str
es_estudiante = True  # bool

# Mostrar tipos
print(type(edad))         # <class 'int'>
print(type(altura))       # <class 'float'>
print(type(nombre))       # <class 'str'>
print(type(es_estudiante))# <class 'bool'>
```

## Errores comunes
- Usar comillas incorrectas en strings
- Confundir True/False con "true"/"false"
- Olvidar el signo igual para asignar

## Buenas prácticas
- Nombres descriptivos para variables
- Usar minúsculas y guiones bajos

## Ejercicios prácticos
1. Crea variables para tu nombre, edad y si eres estudiante.
2. Imprime el tipo de cada variable usando `type()`.

## Mini reto
Crea una variable que almacene tu peso y otra que indique si tienes mascota. Imprime ambas y sus tipos.
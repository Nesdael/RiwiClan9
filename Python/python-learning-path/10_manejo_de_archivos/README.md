# 10 - Manejo de Archivos en Python

## Concepto
El manejo de archivos permite leer y escribir información en archivos externos.

## Analogía sencilla
Piensa en un cuaderno: puedes escribir notas (guardar datos) y leerlas después.

## Tipos de operaciones
- Lectura: `open('archivo.txt', 'r')`
- Escritura: `open('archivo.txt', 'w')`
- CSV: archivos de datos separados por comas

## Ejemplo explicado
```python
# Escritura
with open('datos.txt', 'w') as f:
    f.write('Hola, archivo!\n')

# Lectura
with open('datos.txt', 'r') as f:
    contenido = f.read()
    print(contenido)

# CSV
import csv
with open('datos.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['nombre', 'edad'])
    writer.writerow(['Ana', 25])

with open('datos.csv', 'r') as f:
    reader = csv.reader(f)
    for fila in reader:
        print(fila)
```

## Errores comunes
- Olvidar cerrar el archivo
- Escribir en modo lectura
- No manejar errores de archivo

## Buenas prácticas
- Usar `with` para abrir archivos
- Manejar excepciones

## Ejercicios prácticos
1. Escribe tu nombre en un archivo y léelo.
2. Crea un archivo CSV con tus datos.

## Mini reto
Haz un programa que lea un archivo y cuente cuántas líneas tiene.
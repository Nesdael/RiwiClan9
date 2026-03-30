# Ejemplos de manejo de archivos

# Escritura en archivo
with open('saludo.txt', 'w') as f:
    f.write('¡Hola, mundo!\n')

# Lectura de archivo
with open('saludo.txt', 'r') as f:
    texto = f.read()
    print("Contenido:", texto)

# Manejo de CSV
import csv
with open('personas.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['nombre', 'edad'])
    writer.writerow(['Juan', 30])

with open('personas.csv', 'r') as f:
    reader = csv.reader(f)
    for fila in reader:
        print("Fila:", fila)

# Ejercicio: cuenta líneas de un archivo
# ...
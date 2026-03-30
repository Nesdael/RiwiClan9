# Ejemplos de manejo de errores

# Manejo de error al convertir texto a número
try:
    valor = int("abc")
except ValueError:
    print("Error: no es un número.")

# Manejo de error al abrir archivo
try:
    f = open("no_existe.txt")
except FileNotFoundError:
    print("Archivo no encontrado.")
finally:
    print("Intento de apertura finalizado.")

# Mini reto: división segura

def dividir(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("No se puede dividir por cero.")
        return None

print(dividir(10, 0))

# Ejercicio: maneja tus propios errores
# ...
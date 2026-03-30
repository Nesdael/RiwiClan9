# Ejemplos de funciones

def es_mayor_de_edad(edad):
    """Devuelve True si la edad es mayor o igual a 18"""
    return edad >= 18

print(es_mayor_de_edad(20))

# Función con docstring y retorno
def area_circulo(radio):
    """Calcula el área de un círculo dado su radio"""
    pi = 3.1416
    return pi * radio ** 2

print("Área círculo:", area_circulo(5))

# Mini reto: saludar a varios

def saludar_nombres(lista):
    """Saluda a cada nombre en la lista"""
    for nombre in lista:
        print(f"Hola, {nombre}!")

saludar_nombres(["Ana", "Luis", "Pedro"])

# Ejercicio: crea tus propias funciones
# ...
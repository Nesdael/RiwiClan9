# 04 - Ciclos en Python

## Concepto
Los ciclos permiten repetir acciones varias veces.

## Analogía sencilla
Piensa en un reloj: sus manecillas giran una y otra vez, igual que un ciclo repite instrucciones.

## Tipos de ciclos
- `for`: recorre una secuencia
- `while`: repite mientras se cumpla una condición
- `break`: termina el ciclo
- `continue`: salta a la siguiente iteración

## Ejemplo explicado
```python
# Ciclo for
for i in range(5):
    print("Iteración:", i)

# Ciclo while
contador = 0
while contador < 3:
    print("Contador:", contador)
    contador += 1

# Uso de break y continue
for num in range(5):
    if num == 3:
        break  # Termina el ciclo
    if num == 1:
        continue  # Salta esta iteración
    print(num)
```

## Errores comunes
- Ciclos infinitos por olvidar actualizar la condición
- Olvidar la indentación
- Usar mal break/continue

## Buenas prácticas
- Usar variables descriptivas
- Evitar ciclos infinitos

## Ejercicios prácticos
1. Imprime los números del 1 al 10 usando for.
2. Usa while para pedir un número hasta que sea mayor a 5.

## Mini reto
Haz un ciclo que imprima los números pares del 0 al 10.
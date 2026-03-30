# 03 - Condicionales en Python

## Concepto
Las condicionales permiten tomar decisiones en el código según ciertas condiciones.

## Analogía sencilla
Imagina un semáforo: según el color, decides si avanzas o te detienes. Así funcionan las condicionales.

## Estructura básica
- `if`: si se cumple la condición
- `elif`: si no, prueba otra condición
- `else`: si ninguna se cumple

## Ejemplo explicado
```python
edad = 18
if edad >= 18:
    print("Eres mayor de edad")
elif edad >= 13:
    print("Eres adolescente")
else:
    print("Eres niño")
```

## Errores comunes
- Olvidar la indentación
- Usar `=` en vez de `==` para comparar
- No cubrir todos los casos

## Buenas prácticas
- Usar condiciones claras
- Comentar decisiones importantes

## Ejercicios prácticos
1. Escribe un programa que indique si un número es positivo, negativo o cero.
2. Crea una condicional para verificar si tienes acceso a un sitio web según tu edad.

## Mini reto
Haz un programa que pida una calificación y muestre si es "Aprobado" (>=6) o "Reprobado" (<6).
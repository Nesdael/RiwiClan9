# 13 - Introducción a Data Analysis

## Concepto
El análisis de datos permite extraer información útil de grandes cantidades de datos.

## Analogía sencilla
Piensa en un detective: busca pistas en los datos para encontrar respuestas.

## Herramientas principales
- pandas: manipulación de datos
- Lectura de CSV
- Filtrado de datos
- Estadísticas básicas

## Ejemplo explicado
```python
import pandas as pd
# Leer CSV
df = pd.read_csv('datos.csv')
print(df.head())

# Filtrar datos
filtrados = df[df['edad'] > 18]
print(filtrados)

# Estadísticas
print(df['edad'].mean())  # Promedio
```

## Errores comunes
- No instalar pandas
- Escribir mal el nombre de la columna
- No manejar datos faltantes

## Buenas prácticas
- Revisar los datos antes de analizarlos
- Usar nombres claros para columnas

## Ejercicios prácticos
1. Crea un CSV con nombres y edades.
2. Usa pandas para leerlo y mostrar el promedio de edad.

## Mini reto
Filtra y muestra solo los registros de personas mayores de 30 años.
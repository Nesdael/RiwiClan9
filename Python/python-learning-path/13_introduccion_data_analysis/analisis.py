# Ejemplo de análisis de datos con pandas

import pandas as pd

# Crear un DataFrame desde un CSV
# Supón que tienes un archivo 'personas.csv' con columnas 'nombre' y 'edad'
df = pd.read_csv('personas.csv')
print("Datos:")
print(df)

# Filtrar personas mayores de 18 años
mayores = df[df['edad'] > 18]
print("Mayores de 18:")
print(mayores)

# Estadísticas básicas
print("Promedio de edad:", df['edad'].mean())
print("Edad máxima:", df['edad'].max())
print("Edad mínima:", df['edad'].min())

# Mini reto: filtrar mayores de 30
mayores_30 = df[df['edad'] > 30]
print("Mayores de 30:")
print(mayores_30)

# Ejercicio: explora tus propios datos
# ...
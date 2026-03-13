bajo_compromiso = 0
compromiso_medio = 0
compromiso_alto = 0

personas = 0

while personas < 5:
    try:    
        nombres = str(input("Nombre:"))
        dias = int(input("Dias asistidos esta semana: "))
        minutos = int(input("Aprox. minutos entrenados: "))
    except:
        print("favor poner bien ")
        break    
    
    personas += 1    
    print(f"van {personas}")
     
    if dias < 3:
        bajo_compromiso += 1

    elif 3 <= dias <= 4:
        compromiso_medio += 1

    else:
        compromiso_alto += 1


print("Resultados finales")
print(f"Bajo compromiso: {bajo_compromiso}")
print(f"Compromiso medio: {compromiso_medio}")
print(f"Compromiso alto: {compromiso_alto}")
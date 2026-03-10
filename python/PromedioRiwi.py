total_coders = 0
suma_promedios = 0

reprobados = 0
regulares = 0
excelentes = 0

mejor_promedio = 0
mejor_coder = ""

continuar = "si"

# lista donde se guardarán los coders
coders = []

while continuar == "si":

    modulo = input("Ingrese el nombre del módulo: ")
    while not modulo.isalpha():
        print('Solo se permite letras')
        modulo = input("Ingrese el nombre del módulo: ")

    nombre = input("\nIngrese el nombre del coder: ")
    while not nombre.isalpha():
        print('Solo se permite letras')
        nombre = input("Ingrese el nombre del coder: ")

    dev = float(input("Nota de Desarrollo de Software (0-100): "))
    while dev < 0 or dev > 100:
        dev = float(input("Nota inválida. Ingrese nuevamente (0-100): "))

    socio = float(input("Nota de Habilidades Socioemocionales (0-100): "))
    while socio < 0 or socio > 100:
        socio = float(input("Nota inválida. Ingrese nuevamente (0-100): "))

    ingles = float(input("Nota de Inglés (0-100): "))
    while ingles < 0 or ingles > 100:
        ingles = float(input("Nota inválida. Ingrese nuevamente (0-100): "))

    promedio = (dev * 0.6) + (socio * 0.2) + (ingles * 0.2)

    if promedio < 50:
        clasificacion = "Reprobado"
        reprobados += 1
    elif promedio < 80:
        clasificacion = "Regular"
        regulares += 1
    else:
        clasificacion = "Excelente"
        excelentes += 1

    print("\n--- Resultado ---")
    print("Coder:", nombre)
    print("Módulo:", modulo)
    print("Promedio final:", round(promedio, 2))
    print("Clasificación:", clasificacion)

    if dev < 50:
        print("Observación: Debe reforzar el frente técnico principal.")

    # guardar mejor coder
    if promedio > mejor_promedio:
        mejor_promedio = promedio
        mejor_coder = nombre

    total_coders += 1
    suma_promedios += promedio

    #  diccionario del coder
    coder = {
        "nombre": nombre,
        "modulo": modulo,
        "dev": dev,
        "socio": socio,
        "ingles": ingles,
        "promedio": round(promedio, 2),
        "clasificacion": clasificacion
    }

    # guardar coder en la lista
    coders.append(coder)

    continuar = input("\n¿Desea registrar otro coder? (si/no): ")

# resumen final
if total_coders > 0:
    promedio_general = suma_promedios / total_coders
else:
    promedio_general = 0

print("\n====== RESUMEN DEL MÓDULO ======")
print("Módulo:", modulo)
print("Total de coders:", total_coders)
print("Promedio general:", round(promedio_general, 2))
print("Reprobados:", reprobados)
print("Regulares:", regulares)
print("Excelentes:", excelentes)
print("Mejor coder:", mejor_coder, "con promedio", round(mejor_promedio, 2))

# 🔹 mostrar todos los coders guardados
print("\nLista de coders guardados:")
for coder in coders:
    print(coder)
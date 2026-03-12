turno = int(input("Hora de llegada del cliente? (0 a 23 horas)\n"))

if 6 <= turno <= 11:
    print("Hora de la mañana")

elif 12 <= turno <= 17:
    print("Hora de la tarde")

elif 18 <= turno <= 22:
    print("Hora de la noche")

else:
    print("Fuera de horario")
estudiante = int(input("Cuantas veces asistio el estudiante de baile a clases?\n"))

if estudiante < 5:
    print("Asistencia baja")
elif 5 <= estudiante <= 8:
    print("Asistencia media") 
else:
    print("asistencia alta")
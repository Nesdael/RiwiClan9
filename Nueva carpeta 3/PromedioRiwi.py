# Pesos de cada frente
#   • Desarrollo de Software = 60%
#   • Habilidades Socioemocionales = 20%
#   • Inglés = 20%

# Clasificación del resultado
#   • 0 a 49 → Reprobado
#   • 50 a 79 → Regular
#   • 80 a 100 → Excelente


coders = int(input("Cuantos coders va a procesar?\n "))

while coders:
    
    modulo = str(input("Ingrese el modulo del coder?\n "))
    coder = str(input("Ingrese el nombre del coder?\n "))
    
    desarrollo_de_Software = float(input("Digite la nota de Desarrollo de Software del coder?\n "))
    while desarrollo_de_Software < 0 or desarrollo_de_Software > 100:
        print("Error: debe ser entre 0 a 100")
        desarrollo_de_Software = float(input("Ingrese nuevamente la nota de Desarrollo de Software del coder?\n "))
    if desarrollo_de_Software < 50:
        print ("Debe reforzar el frente técnico principal.")
    ingles = float(input("Digite la nota de ingles del coder?\n "))
    while ingles < 0 or ingles > 100:
        print("Error: debe ser entre 0 a 100")
        ingles = float(input("Ingrese nuevamente la nota de ingles del coder?\n "))
    habilidades_Socioemocionales = float(input("Digite la nota de habilidades socioemocionales del coder?\n "))
    while habilidades_Socioemocionales < 0 or habilidades_Socioemocionales > 100:
        print("Error: debe ser entre 0 a 100")
        habilidades_Socioemocionales = float(input("Ingrese nuevamente la nota de habilidades socioemocionales del coder?\n "))
        
        
    
        nota = ((desarrollo_de_Software * 0.60) + (ingles * 0.20) + (habilidades_Socioemocionales * 0.20))
        
        notafinal = nota
        
        if 0 <= notafinal <= 49:
            print(f"Usted a reprobado su nota es: {str(nota)}" )
        elif 50 <= notafinal <= 79:
            print("Usted a sido regular su nota es: " + str(nota))
        elif 80 <= notafinal <= 100:
            print("Usted a sido excelente su nota es " + str(nota))
        else:
            print("No ha habido ninguna nota")
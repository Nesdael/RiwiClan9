from cargando import mostrar_progreso , mostrar_saliendo
from ansi_colores import *

historial=[]

while True:
    print(f"{BG_GREEN}-------------------------------------{RESET}")
    print(f"{BG_GREEN}Bienvenido a la calculadora en Python{RESET}")
    print(f"{BG_GREEN}-------------------------------------{RESET}")
    print(f"{GREEN}1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Potenciación")
    print("6. Raíz cuadrada")
    print("7. modulo")
    print("8. porcentaje")
    print("9. promedio")
    print(f"10. Ver historial{RESET}")
    print(f"{RED}11. Salir{RESET}")
    operacion = int(input("Ingrese el número de la operación que desea realizar: \n"))

    #Suma
    if operacion == 1:
        print("Ingrese el primer número:")
        num1 = float(input())
        print("Ingrese el segundo número:")
        num2 = float(input())
        resultado = num1 + num2
        mostrar_progreso()

        if resultado.is_integer():
            print("El resultado de la suma es:", int(resultado))
        else:
            print("El resultado de la suma es:", resultado)

        historial.append(f"Suma: {num1} + {num2} = {resultado}")

    #Resta    
    elif operacion == 2:
        print("Ingrese el primer número:")
        num1 = float(input())
        print("Ingrese el segundo número:")
        num2 = float(input())
        resultado = num1 - num2
        mostrar_progreso()

        if resultado.is_integer():
            print("El resultado de la restar es:", int(resultado))
        else:
            print("El resultado de la restar es:", resultado)
        
        historial.append(f"Suma: {num1} + {num2} = {resultado}")

    #Multiplicación   
    elif operacion == 3:
        print("Ingrese el primer número:")
        num1 = float(input())
        print("Ingrese el segundo número:")
        num2 = float(input())
        resultado = num1 * num2
        mostrar_progreso()

        if resultado.is_integer():
            print("El resultado de la multiplicacion es:", int(resultado))
        else:
            print("El resultado de la multiplicacion es:", resultado)

        historial.append(f"Suma: {num1} + {num2} = {resultado}")

    #División   
    elif operacion == 4:
        print("Ingrese el primer número:")
        num1 = float(input())
        print("Ingrese el segundo número:")
        num2 = float(input())
        if num2 != 0:
            resultado = num1 / num2
            mostrar_progreso()

            if resultado.is_integer():
                print("El resultado de la division es:", int(resultado))
            else:
                print("El resultado de la division es:", resultado)
        else:
            print("Error: No se puede dividir por cero.")
        
        historial.append(f"Suma: {num1} + {num2} = {resultado}")

    #Potenciación        
    elif operacion == 5:
        print("Ingrese la base:")
        base = float(input())
        print("Ingrese el exponente:")
        exponente = float(input())
        resultado = base ** exponente
        mostrar_progreso()

        if resultado.is_integer():
            print("El resultado de la potencia es:", int(resultado))
        else:
            print("El resultado de la potencia es:", resultado)

        historial.append(f"Suma: {num1} + {num2} = {resultado}")

    #Raíz cuadrada
    elif operacion == 6:
        print("Ingrese el número:")
        num = float(input())
        if num >= 0:
            resultado = num ** 0.5
            mostrar_progreso()

            if resultado.is_integer():
                print(f"El resultado de la raiz cuadrada de {num} es:", int(resultado))
            else:
                print(f"El resultado de la raiz cuadrada de {num} es:", resultado)
        else:
            print("Error: No se puede calcular la raíz cuadrada de un número negativo.")
        
        historial.append(f"Suma: {num1} + {num2} = {resultado}")

    #Módulo        
    elif operacion == 7:
        print("Ingrese el primer número:")
        num1 = float(input())
        print("Ingrese el segundo número:")
        num2 = float(input())
        resultado = num1 % num2
        mostrar_progreso()

        if resultado.is_integer():
            print("El resultado del modulo es:", int(resultado))
        else:
            print("El resultado del modulo es:", resultado)

        historial.append(f"Suma: {num1} + {num2} = {resultado}")

    #Porcentaje   
    elif operacion == 8:       
        print("Ingrese el número:")
        num1 = float(input())
        print("Ingrese el porcentaje:")
        porcentaje = float(input())
        resultado = (num1 / 100) * porcentaje
        mostrar_progreso()

        if resultado.is_integer():
            print("El resultado del porcentaje es:", int(resultado))
        else:
            print("El resultado del porcentaje es:", resultado)

        historial.append(f"Suma: {num1} + {num2} = {resultado}")

    #Promedio
    elif operacion == 9:
        print("Ingrese el primer número:")
        num1 = int(input())
        print("Ingrese el segundo número:")
        num2 = int(input())
        resultado = (num1 + num2) / 2
        mostrar_progreso()

        if resultado.is_integer():
            print(f"El promedio entre {num1} y {num2} es: {int(resultado)}")
        else:
            print(f"El promedio entre {num1} y {num2} es: {resultado}")

        historial.append(f"Suma: {num1} + {num2} = {resultado}")


    #Mirar Historial
    elif operacion == 10:
        if historial:
            print("Historial de operaciones:")
            for i, operacion in enumerate(historial, 1):
                print(f"{i}. {operacion}")
        else:
            print("No hay operaciones en el historial.")

    #Salir
    elif operacion == 11:
            mostrar_saliendo()
            print("Gracias por usar la calculadora. ¡Hasta luego!")
            break

    respuesta = input("¿Desea realizar otra operación? (si/no): ").lower()
    if respuesta != 'si':
        print("Gracias por usar la calculadora. ¡Hasta luego!")
        break
    
  
    
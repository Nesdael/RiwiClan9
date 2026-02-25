while True:
    print("Bienvenido a la calculadora en Python")
    print("Seleccione la operación que desea realizar:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Potenciación")
    print("6. Raíz cuadrada")
    print("7. modulo")
    print("8. porcentaje")
    print("9. promedio")
    print("10. Salir")
    operacion = int(input("Ingrese el número de la operación que desea realizar: \n"))

    #Suma
    if operacion == 1:
        print("Ingrese el primer número:")
        num1 = float(input())
        print("Ingrese el segundo número:")
        num2 = float(input())
        resultado = num1 + num2
        print("El resultado de la suma es:", resultado)

    #Resta    
    elif operacion == 2:
        print("Ingrese el primer número:")
        num1 = float(input())
        print("Ingrese el segundo número:")
        num2 = float(input())
        resultado = num1 - num2
        print("El resultado de la resta es:", resultado)

    #Multiplicación   
    elif operacion == 3:
        print("Ingrese el primer número:")
        num1 = float(input())
        print("Ingrese el segundo número:")
        num2 = float(input())
        resultado = num1 * num2
        print("El resultado de la multiplicación es:", resultado)

    #División   
    elif operacion == 4:
        print("Ingrese el primer número:")
        num1 = float(input())
        print("Ingrese el segundo número:")
        num2 = float(input())
        if num2 != 0:
            resultado = num1 / num2
            print("El resultado de la división es:", resultado)
        else:
            print("Error: No se puede dividir por cero.")

    #Potenciación        
    elif operacion == 5:
        print("Ingrese la base:")
        base = float(input())
        print("Ingrese el exponente:")
        exponente = float(input())
        resultado = base ** exponente
        print("El resultado de la potenciación es:", resultado)

    #Raíz cuadrada
    elif operacion == 6:
        print("Ingrese el número:")
        num = float(input())
        if num >= 0:
            resultado = num ** 0.5
            print("El resultado de la raíz cuadrada es:", resultado)
        else:
            print("Error: No se puede calcular la raíz cuadrada de un número negativo.")

    #Módulo        
    elif operacion == 7:
        print("Ingrese el primer número:")
        num1 = float(input())
        print("Ingrese el segundo número:")
        num2 = float(input())
        resultado = num1 % num2
        print("El resultado del módulo es:", resultado)

    #Porcentaje   
    elif operacion == 8:       
        print("Ingrese el número:")
        num1 = float(input())
        print("Ingrese el porcentaje:")
        porcentaje = float(input())
        resultado = (num1 / 100) * porcentaje
        print("El resultado del porcentaje es:", resultado)

    #Promedio
    elif operacion == 9:
        print("Ingrese el primer número:")
        num1 = int(input())
        print("Ingrese el segundo número:")
        num2 = int(input())
        resultado = (num1 + num2) / 2
        print(f"El promedio entre {num1} y {num2} es: {resultado}")
        

    #Salir
    elif operacion == 10:
            print("Gracias por usar la calculadora. ¡Hasta luego!")
            break

    respuesta = input("¿Desea realizar otra operación? (si/no): ").lower()
    if respuesta != 'si':
        print("Gracias por usar la calculadora. ¡Hasta luego!")
        break
    
  
    

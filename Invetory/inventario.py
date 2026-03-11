print("Bienvenido a nuestro inventario")

#Variable de control para repetir el registro de productos
continuar = "si"

#Mientras continuar no sea diferencia a "si" el ciclo continuara hasta que este sea negativo
while continuar == "si":
    #Se le pide al usuario que agregue un producto
    nombre = str(input("Ingrese el nombre del producto\n"))
    #Si el usuario ingresa un digito en lugar de una letra le saltara este if, y el .replace permite letras y espacios
    #Por que .isalpha no permite espacios
    if not nombre.replace(" ", "").isalpha():
        print("Solo se pueden colocar letras")
        continue
    
    # Validación del precio (debe ser un número decimal)
    while True:
        try:
            #Se le pide al usuario que ingrese un precio del producto unitario
            precio = float(input("Ingrese el precio unitario del producto\n"))
            if precio <= 0:
                print("Coloque el precio que es")
                continue
            break
        except ValueError:
                print("Favor solo ingresar digitos")
                break
        
    # Validación del precio (debe ser un número decimal)
    while True:
        try:
            #Se le pide al usuario que ingrese la cantidad que desea del producto
            cantidad = int(input("Ingrese la cantidad que desea del producto\n"))
            if cantidad <= 0:
                print("Coloque la cantidad que es")
                continue
            break
        except ValueError:
                print("Por favor solo ingresar numeros")
                break
        
    
    print("")
    print("==========================================")
    print("")
    
    print("Factura")
    historial = print(f"Producto: {nombre.capitalize()} | Precio: {round(precio, 2)} | Cantidad: {cantidad}")
    costo_total = print(f"Costo total de los produdctos: {precio * cantidad}" )
    
    # Preguntar al usuario si desea registrar otro producto
    continuar = input("\n¿Desea registrar otro coder? (si/no): ").lower()
    
    # Mensaje final al salir del programa
    if continuar != "si":
        print("Gracias por utilizar nuestro inventario")

    

def agregar_producto():
    
    while True:
        nombre_producto = input("Ingrese el nombre del producto\n")
        if not nombre_producto.replace(" ", "").isalpha():
                print("Solo se pueden colocar letras")
                continue
            
        while True:
            try:
                precio = float(input(f"Ingrese el precio unitario de {nombre_producto}\n"))
                if precio <= 0:
                    print("Error: No se puede colocar 0")
                    continue
                break
            except ValueError:
                print("Error: Favor solo ingresar digitos")
                
        while True:
            try:
                # Se le pide al usuario que ingrese la cantidad que desea del producto
                cantidad = int(input(f"Ingrese la cantidad que desea de {nombre_producto}\n"))
                if cantidad <= 0:
                    print("Error: No se puede colocar 0")
                    continue
                break
            except ValueError:
                print("Error: Por favor solo ingresar numeros")
                

if __name__ == "__main__":
    agregar_producto() 

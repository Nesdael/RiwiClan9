from diccionario_producto import inventario
    

def agregar_producto():
    
    continuar = "si"
    
    while continuar == "si":
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
                cantidad = int(input(f"Ingrese la cantidad que desea de {nombre_producto}\n"))
                if cantidad <= 0:
                    print("Error: No se puede colocar 0")
                    continue
                break
            except ValueError:
                print("Error: Por favor solo ingresar numeros")
            
            
                
        producto = {
            'nombre': nombre_producto,
            'precio': precio,
            'cantidad': cantidad          
            }
                
                
                
        inventario.append(producto)
                
                  
        continuar = input("Desea seguir agregando productos? (Si/No)\n").lower()
        
        
def mostrar_inventario():
    if len(inventario) == 0:
        print("Aun no hay nada ")
        return
    
    else:
        print("INVENTARIO")
        for producto in inventario:
            print(f"producto: {producto['nombre']} | precio: {producto['precio']} | cantidad: {producto['cantidad']}" )
            print()
            
def calcular_estadisticas():
    
    cantidad_total = 0
    valortotal = 0
    
    for producto in inventario:
        cantidad_total += producto["cantidad"]
        valortotal += producto["precio"] * producto["cantidad"]
        
    print(f"La cantidad total de productos registrados es: {cantidad_total}\n")
    print(f"El valor total del inventario es: {valortotal}\n")        
            
    
if __name__ == "__main__": 
    agregar_producto()
    mostrar_inventario()
    calcular_estadisticas()
                
                        
                
                
        
                    
                

    
    
                



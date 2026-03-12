vainilla = 0
chocolate = 0
fresa = 0
ventas_realizadas = 0

print("heladeria popeye")
print("1: vainilla")
print("2: chocolate")
print("3: fresa")

while ventas_realizadas < 5:
    try:
        sabor= int(input("Que tipo de helado quieres? \n"))
        if sabor == 1:
            vainilla += 1
            ventas_realizadas += 1
        elif sabor == 2:
            chocolate += 1
            ventas_realizadas += 1
        elif sabor == 3:
            fresa += 1
            ventas_realizadas += 1
        else:
            print("esa opcion no esta") 
    except ValueError:
        print("Ingrese un valor correcto")
        
print(f"EL sabor de vainilla fue pedido {vainilla}")    
print(f"EL sabor de chocolate fue pedido {chocolate}")  
print(f"EL sabor de fresa fue pedido {fresa}")  

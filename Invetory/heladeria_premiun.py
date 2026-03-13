cono = 3000
vaso = 4000
banana_split = 9000

total_vendido = 0
clientes_aten = 0
cono_veces = 0
vaso_veces = 0
banana_split_veces = 0


continuar = "si"

print("Heladeria premiun")
print("1. cono")
print("2. vaso")
print("3. banana split")

while continuar == "si":
    producto = int(input("Que producto desea?\n"))
    
    if producto == 1:
        cantidad = int(input("Cuantas desea? \n"))
        clientes_aten += 1
        cono_veces += cantidad
        total_vendido += cantidad
        total_pagar= cono * cantidad
        print(f"Pediste el producto cono y fueron {cantidad} el precio a pagar es {total_pagar}")
        
    elif producto == 2:
        cantidad = int(input("Cuantas desea? \n"))
        clientes_aten += 1
        vaso_veces += cantidad
        total_vendido += cantidad
        total_pagar= vaso * cantidad
        print(f"Pediste el producto cono y fueron {cantidad} el precio a pagar es {total_pagar}")
        
    elif producto == 3:
        cantidad = int(input("Cuantas desea? \n"))
        clientes_aten += 1
        banana_split_veces += cantidad
        total_vendido += cantidad
        total_pagar= banana_split * cantidad
        print(f"Pediste el producto cono y fueron {cantidad} el precio a pagar es {total_pagar}")
        
    else:
        print("Digite un valor valido (1/2/3)")
        continue
              
    continuar = input("Desea continuar? (si/no)\n").lower()     
        
if cono_veces > vaso_veces and cono_veces > banana_split_veces:
    print(f"El producto mas comprado fue el cono con {cono_veces} ventas")

elif vaso_veces > cono_veces and vaso_veces > banana_split_veces:
    print(f"El producto mas comprado fue el vaso con {vaso_veces} ventas")

elif banana_split_veces > cono_veces and banana_split_veces > vaso_veces:
    print(f"El producto mas comprado fue el banana split con {banana_split_veces} ventas")

else:
    print("Hubo empate entre productos")      
    
        
print(f"El total vendido es {total_vendido}")
print(f"Se atendieron {clientes_aten} clientes el dia de hoy")        
    
print("Gracias por preferirnos")
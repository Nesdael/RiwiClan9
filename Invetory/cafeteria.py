cafe = 4000
te = 3500
jugo = 5000

pedidos = 0

print("cafeteria")
print(
    """
    menu
    1. cafe
    2.te
    3.jugo
    """
)

sabor = int(input("Que bebida desea pedir?\n"))
unidades = int(input("Cuantas unidades desea pedir?\n"))

if sabor == 1:
    sabor = "cafe"
    valor_pagar = cafe * unidades
        
elif sabor == 2:
    sabor = "te"
    valor_pagar = te * unidades  
elif sabor == 3:
    sabor = "jugo"
    valor_pagar = jugo * unidades
else:
    print("ese sabor no esta disponible")

print(f"Eligio el sabor de {sabor} y pidio {unidades} unidades")
print(f"El valor a pagar es de ${valor_pagar}")
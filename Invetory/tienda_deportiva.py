import random

ventas = 0

balon = random.randint(30000, 150000)
raqueta = random.randint(30000, 150000)
guantes = random.randint(30000, 150000)
mancuernas = random.randint(30000, 150000)
colchoneta = random.randint(30000, 150000)
cuerda = random.randint(30000, 150000)

cien = []

print("Productos disponibles")
print("1. balon")
print("2. raqueta")
print("3. guantes")
print("4. mancuernas")
print("5. colchoneta")
print("6. cuerda")

while ventas < 6:

    print("")
    producto = int(input("Por cual opcion desea preguntar el precio (1/2/3/4/5/6): \n"))
    print("")

    if producto == 1:
        valor = balon
        print(f"El precio del balon es ${valor}")

    elif producto == 2:
        valor = raqueta
        print(f"El precio de la raqueta es ${valor}")

    elif producto == 3:
        valor = guantes
        print(f"El precio de los guantes es ${valor}")

    elif producto == 4:
        valor = mancuernas
        print(f"El precio de las mancuernas es ${valor}")

    elif producto == 5:
        valor = (colchoneta)
        print(f"El precio de la colchoneta es ${valor}")

    elif producto == 6:
        valor = cuerda
        print(f"El precio de la cuerda es ${valor}")

    else:
        print("Ingrese una opción válida")
        continue

    if valor >= 100000:
        cien.append(valor)

    ventas += 1

print("Productos que cuestan más de 100000:", len(cien))
        

    

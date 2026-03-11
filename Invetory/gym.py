edad = int(input("Que edad tienes?\n"))

if edad < 13:
    print("No puedes ingresar")
elif 13 >= edad <= 17:
    print("Estas en el grupo de la clase juvenil")
elif 18 >= edad <= 59:
    print("Estas en el grupo de la clase general")
else:
    print("Estas en el grupo de la clase senior")
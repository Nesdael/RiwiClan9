edad = int(input("Que edad tienes?\n"))

if edad < 12:
    print(f"Tienes {edad} años y debes pagar $8.000")
elif 12 >= edad <= 59:
    print(f"Tienes {edad} años y debes pagar $12.000")  
else:
    print (f"Tienes {edad} años y debes pagar $9.000")
    
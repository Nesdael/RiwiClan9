saldo = 1000
veces = int(input("Ingrese el numero de operaciones\n"))
print("\n---Menu---")
for i in range (veces):
	print("1. Consultar saldo")
	print("2. Retiros")
	print("3. Depositos")
	opcion = int(input("Ingrese una opcion\n"))
	if opcion == 1:
		print(saldo)
	elif opcion==2:
		retiro = int(input("Ingrese un valor\n"))
		if retiro <= 0:
			print("No es una valor valido")
		elif retiro > saldo:
			print("Fondos insuficientes")
		else:
			saldo = saldo-retiro
			print(saldo)
	elif opcion == 3:
			deposito = int(input("Ingresar el valor\n"))
			if deposito <= 0:
				print("Ingrese un valor valido")
			else:
				saldo = saldo + deposito
				print(saldo)
	else:
				print("Gracias por usar el cajero")
				
				
			
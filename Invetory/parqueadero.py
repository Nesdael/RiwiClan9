hora_parqueo= int(input("Cuanto tiempo estuvo en carro en el parqueadero?\n"))
primera_hora =  5000
tiempo_adicional_por_h = 3000

if hora_parqueo <= 1:
    print(f"el precio a pagar por {hora_parqueo} hora de parqueo es {primera_hora}")
else:
    hora_parqueo -= 1
    total= hora_parqueo * tiempo_adicional_por_h + primera_hora
    print(f"Estuvo {hora_parqueo + 1} horas en el parqueadero y su total a pagar es {total} ")
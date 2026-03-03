# Cajero Electronico Basico
-----------

Es una cajero permite cosas basicas, como:

- Depositar
- Mirar saldo
- Retirar
- Hacer transferencias

Este codigo se hizo en **python**.

--------------------

## Explicacion de codigo

Primero debe haber una variable que guarde el dinero en la "cuenta de banco" y la llamaremos:

**`saldo = 0`**

Luego ponemos un bucle que se puede con dos formas _for i in range()_ 
o tambien _while_, el ultimo es que vamos a utilizar, ya que con ese se puede poner un bucle infinito, que seria:

**`while True:`**

**"True"** significa que el bucle siempre va hacer verdadero y se va a repetir todas las veces que el usuario lo necesite.

Luego colocamos lo que el usuario va a ver en la pantalla para que vea las opciones que puede elegir, para eso colocamos varios ***"print"*** como se mostrara ahora:

```
print("-----cajero estrellita-----")
    print("1.consulta de saldo")
    print("2.Retiro")
    print("3.deposito")
    print("4.transferencias")
    print("5. Salir")

    operacion = int(input("Ingresa una opcion"))
```

y podremos una varible que se llamara _**operacion**_, para poner en esa variable el valor que el usuario desea elegir.

A continuacion, se pondra el codigo las opciones que va a poder elegir el usuario, y lo haremos con las condicionales _**if, elif y else**_, con estas podremos que si no es una opcion es otra, y si no es esa otra y asi, hasta que salga la opcion que es, y si no pode ningun opcion que aparezca se le pondra un alerta de error.

```
 if operacion == 1:
        print(saldo)
        
    elif operacion == 2:
        retiro=int(input("ingresar valor a retirar"))
    
        if retiro > saldo:
            print("porfavor ingrese un valor menor al saldo")
   
        else:
            saldo=(saldo-retiro)
            print("su nuevo saldo es de", saldo)

    elif operacion == 3:
        deposito=int(input("ingresar valor a depositar"))
        saldo=(saldo+deposito)
        print(saldo)

    elif operacion == 4:
         cuenta = int(input("Ingresar cuenta del destino"))
         monto = int(input("Ingrese el monto que desea transferir"))
         if monto <= saldo:
             saldo = saldo - monto
             print("Transferencia exitosamente a la cuenta " + str(cuenta))
             print ("Nuevo saldo: " + str(saldo))

         else :
             print("No se pudo hacer la transferencia")
    
    elif operacion == 5:
        print("adios")
        break

    else:
        print("Coloca una opcion disponible")    
```

#### Autor
Nestor D. Duran Fuentes






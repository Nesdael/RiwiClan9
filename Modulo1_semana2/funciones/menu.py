from colores import *
from limpiar_pantalla import limpiar_pantalla
from funciones import agregar_producto, mostrar_inventario, calcular_estadisticas



def menu():
    
    continuar = "si"
    
    while continuar == "si":
        limpiar_pantalla()
        
        print(f"{F_VERDE}--- Menu de inventario ---{RESET}")
        print("1. Agregar producto")
        print("2. Mostrar inventario")
        print("3. Calcular estadisitcas")
        print("4. Salir")
     
    
        opcion = int(input("Que opcion desea realizar?\n")) 
    
        if opcion == 1:
            limpiar_pantalla()
            print("Haz elegido la opcion agregar producto")
            agregar_producto()
            
        elif opcion == 2:
            limpiar_pantalla()
            print("Haz elegido la opcion mostrar producto")
            mostrar_inventario()
            
        elif opcion == 3:
            limpiar_pantalla()
            print("Calculando estadisticas... ")
            calcular_estadisticas()

        elif opcion == 4:
            print("Ha salido del programa") 
            exit()

        else:
            print("Ingrese una opcion valida")
            input("Oprima cualquier boton para intentar de nuevo...")
            continue    
        
        limpiar_pantalla()
        continuar = input("Desea hacer otra consulta? (Si/No)\n").lower()
        print("Hasta luego")
        
        
           
        
menu()               
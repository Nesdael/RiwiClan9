from colores import *
from limpiar_pantalla import limpiar_pantalla
from agregar_producto import agregar_producto



#if __name__ == "__main__":
#    menu()



def menu():
    
    while True:
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
            print("xd")
            

        elif opcion == 3:
            print("sad") 

        elif opcion == 4:
            print("Ha salido del programa") 
            exit()

        else:
            print("Ingrese una opcion valida")
            input("Oprima cualquier boton para intentar de nuevo...")
            continue    
        
           
        
menu()               
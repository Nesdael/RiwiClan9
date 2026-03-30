# app.py - Agenda de contactos

import os

CONTACTOS_FILE = 'contactos.txt'

def mostrar_menu():
    print("\n--- Agenda de Contactos ---")
    print("1. Agregar contacto")
    print("2. Ver contactos")
    print("3. Eliminar contacto")
    print("4. Buscar contacto")
    print("5. Salir")

def agregar_contacto():
    nombre = input("Nombre: ")
    telefono = input("Teléfono: ")
    with open(CONTACTOS_FILE, 'a') as f:
        f.write(f"{nombre},{telefono}\n")
    print("Contacto agregado.")

def ver_contactos():
    if not os.path.exists(CONTACTOS_FILE):
        print("No hay contactos.")
        return
    with open(CONTACTOS_FILE, 'r') as f:
        for linea in f:
            nombre, telefono = linea.strip().split(',')
            print(f"Nombre: {nombre}, Teléfono: {telefono}")

def eliminar_contacto():
    nombre_borrar = input("Nombre a eliminar: ")
    if not os.path.exists(CONTACTOS_FILE):
        print("No hay contactos.")
        return
    contactos = []
    with open(CONTACTOS_FILE, 'r') as f:
        contactos = f.readlines()
    with open(CONTACTOS_FILE, 'w') as f:
        borrado = False
        for linea in contactos:
            nombre, telefono = linea.strip().split(',')
            if nombre != nombre_borrar:
                f.write(linea)
            else:
                borrado = True
        if borrado:
            print("Contacto eliminado.")
        else:
            print("Contacto no encontrado.")

def buscar_contacto():
    nombre_buscar = input("Nombre a buscar: ")
    if not os.path.exists(CONTACTOS_FILE):
        print("No hay contactos.")
        return
    with open(CONTACTOS_FILE, 'r') as f:
        encontrados = False
        for linea in f:
            nombre, telefono = linea.strip().split(',')
            if nombre_buscar.lower() in nombre.lower():
                print(f"Nombre: {nombre}, Teléfono: {telefono}")
                encontrados = True
        if not encontrados:
            print("No se encontraron contactos.")

def main():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")
        if opcion == '1':
            agregar_contacto()
        elif opcion == '2':
            ver_contactos()
        elif opcion == '3':
            eliminar_contacto()
        elif opcion == '4':
            buscar_contacto()
        elif opcion == '5':
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()

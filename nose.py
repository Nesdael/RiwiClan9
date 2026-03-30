import os
import csv
from data_clientes import clientes

CARPETA_DATA = "data"
ARCHIVO_CSV = os.path.join(CARPETA_DATA, "data.csv")

# Los campos (columnas) que tendrá tu CSV
CAMPOS = ["usuario_id", "nombre", "email", "telefono"]

def crear_carpeta_si_no_existe():
    if not os.path.exists(CARPETA_DATA):
        os.makedirs(CARPETA_DATA)

def leer_registros_csv():
    if not os.path.exists(ARCHIVO_CSV):
        return []
    with open(ARCHIVO_CSV, "r", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        return list(lector)

def cargar_clientes(clientes):
    try:
        with open(ARCHIVO_CSV, "r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                clientes.append(fila)
    except FileNotFoundError:
        pass

def guardar_clientes(clientes):
    crear_carpeta_si_no_existe()
    with open(ARCHIVO_CSV, "w", encoding="utf-8", newline="") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=CAMPOS)
        escritor.writeheader()
        for cliente in clientes:
            escritor.writerow(cliente)

def actualizar_cliente(clientes, usuario_id, nuevos_datos):
    for cliente in clientes:
        if cliente["usuario_id"] == usuario_id:
            cliente.update(nuevos_datos)
            guardar_clientes(clientes)
            return True
    return False

def eliminar_cliente(clientes, usuario_id):
    for cliente in clientes:
        if cliente["usuario_id"] == usuario_id:
            clientes.remove(cliente)
            guardar_clientes(clientes)
            return True
    return False
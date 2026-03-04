import time

def mostrar_progreso(total=5):
    """
    Muestra una barra de progreso en la terminal usando '#'
    total: cantidad de pasos de la barra
    """
    print("Haciendo tarea...")
    
    for i in range(total):
        hashes = "#" * i
        espacios = " " * (total - i)
        porcentaje = int((i / total) * 100)
        print(f"Pensando: [{hashes}{espacios}] {porcentaje}%", end="\r")
        time.sleep(0.3)

    # Al final asegura que la barra llegue a 100%
    print(f"Pensando: [{'#'*total}] 100%")

def mostrar_saliendo(total=5):

    print("Saliendo del programa...")
    print("Espere un momento...")
    
    for i in range(total):
        hashes = "#" * i
        espacios = " " * (total - i)
        porcentaje = int((i / total) * 100)
        print(f"Saliendo: [{hashes}{espacios}] {porcentaje}%", end="\r")
        time.sleep(0.3)

    # Al final asegura que la barra llegue a 100%
    print(f"haz salido con exito: [{'#'*total}] 100%")
    
# Esto evita que se ejecute al importar
if __name__ == "__main__":
    mostrar_progreso()
    mostrar_saliendo()
# Ejemplos de POO

class Auto:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    def mostrar_info(self):
        print(f"Auto: {self.marca} {self.modelo}")

mi_auto = Auto("Toyota", 2022)
mi_auto.mostrar_info()

class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre
    def estudiar(self):
        print(f"{self.nombre} está estudiando.")

alumno = Estudiante("Luis")
alumno.estudiar()

# Mini reto: CuentaBancaria
class CuentaBancaria:
    def __init__(self, saldo=0):
        self._saldo = saldo  # Encapsulación básica
    def depositar(self, cantidad):
        self._saldo += cantidad
        print(f"Depósito: {cantidad}. Saldo actual: {self._saldo}")
    def retirar(self, cantidad):
        if cantidad > self._saldo:
            print("Fondos insuficientes.")
        else:
            self._saldo -= cantidad
            print(f"Retiro: {cantidad}. Saldo actual: {self._saldo}")

cuenta = CuentaBancaria(100)
cuenta.depositar(50)
cuenta.retirar(30)
cuenta.retirar(200)

# Ejercicio: crea tus propias clases
# ...
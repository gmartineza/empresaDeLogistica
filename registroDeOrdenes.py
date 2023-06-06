import csv

class Colchon:
    def __init__(self, marca, tipo, medida):
        self.marca = marca
        self.tipo = tipo
        self.medida = medida


class RegistroOrdenes:
    def __init__(self):
        self.ordenes = []

    def agregar_orden(self, colchon):
        self.ordenes.append(colchon)

    def guardar_en_csv(self, nombre_archivo):
        with open(nombre_archivo, 'a', newline='') as archivo_csv:
            writer = csv.writer(archivo_csv)
            if archivo_csv.tell() == 0:
                writer.writerow(['Marca', 'Tipo', 'Medida'])  # Escribir encabezados solo si el archivo está vacío
            for orden in self.ordenes:
                writer.writerow([orden.marca, orden.tipo, orden.medida])

    def mostrar_ordenes(self):
        for orden in self.ordenes:
            print("Marca:", orden.marca)
            print("Tipo:", orden.tipo)
            print("Medida:", orden.medida)
            print("--------------------")


# Ejemplo de uso
registro = RegistroOrdenes()

# Solicitar entrada al usuario y agregar la orden
marca = input("Ingrese la marca del colchón: ")
tipo = input("Ingrese el tipo de colchón: ")
medida = input("Ingrese la medida del colchón: ")

colchon_usuario = Colchon(marca, tipo, medida)
registro.agregar_orden(colchon_usuario)

# Guardar las órdenes en un archivo CSV
nombre_archivo = 'ordenes.csv'
registro.guardar_en_csv(nombre_archivo)

# Mostrar todas las órdenes registradas
registro.mostrar_ordenes()

"""
Un hotel de playa cuenta con un recepcionista que se encarga de
presentar a los clientes las opciones de habitaciones disponibles junto
con sus precios. Tras la elección de la habitación, el recepcionista
solicita los datos personales del cliente y el número de noches que
permanecerá en el hotel. Finalmente, entrega al cliente una factura
detallada con el total de los gastos.
 Adicionalmente, los clientes pueden solicitar servicios extra,
como el uso de la piscina o la cancha de golf, que tienen un costo
adicional. Implementa esta funcionalidad en tu programa
"""
class Habitacion:
    def __init__(self, tipo, precio):
        self.tipo = tipo
        self.precio = precio

class ServicioExtra:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class Cliente:
    def __init__(self, nombre, dni, noches, habitacion, servicios):
        self.nombre = nombre
        self.dni = dni
        self.noches = noches
        self.habitacion = habitacion
        self.servicios = servicios

    def calcular_total(self):
        total_habitacion = self.noches * self.habitacion.precio
        total_servicios = sum(servicio.precio for servicio in self.servicios)
        total = total_habitacion + total_servicios
        return total

    def generar_factura(self):
        print("\n----- FACTURA -----")
        print(f"Nombre: {self.nombre}")
        print(f"Identificaion: {self.dni}")
        print(f"Noches: {self.noches}")
        print(f"Habitación: {self.habitacion.tipo}")
        print(f"Precio por noche: ${self.habitacion.precio}")
        print(f"Total por habitación: ${self.noches * self.habitacion.precio}")
        if self.servicios:
            print("\nServicios adicionales:")
            for servicio in self.servicios:
                print(f"{servicio.nombre}: ${servicio.precio}")
            print(f"Total por servicios: ${sum(servicio.precio for servicio in self.servicios)}")
        else:
            print("No se solicitaron servicios adicionales.")
        print(f"\nTotal a pagar: ${self.calcular_total()}")
        print("--------------------")

def Registrar():
    # Definir las habitaciones disponibles
    habitaciones = [
        Habitacion("Sencilla", 100),
        Habitacion("Doble", 150),
        Habitacion("Suite", 250)
    ]

    # Mostrar las opciones de habitaciones disponibles
    print("Habitaciones disponibles:")
    for i, habitacion in enumerate(habitaciones, start=1):
        print(f"{i}. {habitacion.tipo} - ${habitacion.precio} por noche")

    # Seleccionar habitación
    habitacion_seleccionada = int(input("\nSeleccione el número de la habitación deseada: ")) - 1
    habitacion = habitaciones[habitacion_seleccionada]

    # Solicitar datos del cliente
    nombre = input("Ingrese su nombre: ")
    dni = input("Ingrese su DNI: ")
    noches = int(input("Ingrese el número de noches de estancia: "))

    # Definir los servicios adicionales
    servicios_disponibles = [
        ServicioExtra("Piscina", 20),
        ServicioExtra("Cancha de golf", 50),
        ServicioExtra("Spa", 30)
    ]

    # Seleccionar servicios adicionales
    print("\nServicios adicionales disponibles:")
    for i, servicio in enumerate(servicios_disponibles, start=1):
        print(f"{i}. {servicio.nombre} - ${servicio.precio}")
    servicios_seleccionados = input("\nSeleccione los números de los servicios deseados separados por comas (o deje en blanco si no desea servicios): ").strip()

    servicios = []
    if servicios_seleccionados:
        servicios_indices = [int(x) - 1 for x in servicios_seleccionados.split(',')]
        for i in servicios_indices:
            servicios.append(servicios_disponibles[i])

    # Crear el objeto cliente
    cliente = Cliente(nombre, dni, noches, habitacion, servicios)

    # Generar y mostrar la factura
    cliente.generar_factura()

Registrar()

"""
Este enfoque asegura que el cliente pueda ver todas las opciones de habitaciones y servicios 
disponibles antes de proceder con la reserva, y que reciba una factura detallada al final.
Este programa permite a un recepcionista de hotel manejar de manera eficiente la selección 
de habitaciones y servicios adicionales, registrar la información del cliente y generar una
factura detallada. Se puede adaptar fácilmente para incluir más habitaciones y servicios según
las necesidades del hotel.
"""

        
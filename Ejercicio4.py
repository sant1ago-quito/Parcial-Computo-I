"""
Una empresa cuenta con dos tipos de empleados: aquellos con plaza
fija y aquellos que trabajan por horas. Se han registrado los datos de
ambos tipos y, al generar la planilla de pago, se realizan dos cálculos
diferentes. A los empleados de plaza fija se les paga el salario base más
comisiones, mientras que a los empleados por horas se les paga en
función de la cantidad de horas trabajadas.
 Adicionalmente, si un empleado ha laborado más de 5 años, sin
importar su tipo de contrato, se le otorga un bono adicional.
Implemente esto en su código

"""
class Empleado:
    def __init__(self, nombre, años_trabajados):
        self.nombre = nombre
        self.años_trabajados = años_trabajados

    def calcular_pago(self):
        pass

    def calcular_bono(self):
        return 100 if self.años_trabajados > 5 else 0

class EmpleadoPlazaFija(Empleado):
    def __init__(self):
        nombre = input("Ingrese el nombre del empleado con plaza fija: ")
        años_trabajados = int(input(f"Ingrese los años trabajados por {nombre}: "))
        super().__init__(nombre, años_trabajados)
        self.salario_base = float(input(f"Ingrese el salario base de {nombre}: "))
        self.comisiones = float(input(f"Ingrese las comisiones de {nombre}: "))
#Aca creamos la clase para los empleados con plaza fija  y su metodo para calcular su salario base mas sus comisiones, agregando también su bono si es que tiene
    def calcular_pago(self):
        pago = self.salario_base + self.comisiones
        bono = self.calcular_bono()
        return pago + bono
#calculamos el pago del empleado con plaza fija
class EmpleadoPorHoras(Empleado):
    def __init__(self):
        nombre = input("Ingrese el nombre del empleado por horas: ")
        años_trabajados = int(input(f"Ingrese los años trabajados por {nombre}: "))
        super().__init__(nombre, años_trabajados)
        self.tarifa_hora = float(input(f"Ingrese la tarifa por hora de {nombre}: "))
        self.horas_trabajadas = int(input(f"Ingrese las horas trabajadas por {nombre}: "))
#Aca creamos la clase para los empleados por horas y su metodo para calcular su salario basado en sus  horas, agregando también su bono si es que tiene
    def calcular_pago(self):
        pago = self.tarifa_hora * self.horas_trabajadas
        bono = self.calcular_bono()
        return pago + bono
#calculamos el pago del empleado por horas
tipo_empleado = input("El empleado es de plaza fija? (s/n): ").lower()

if tipo_empleado == "s":
    empleado = EmpleadoPlazaFija()
elif tipo_empleado == "n":
    empleado = EmpleadoPorHoras()
else:
    print("Opción no válida.")
    empleado = None

print(f"\nPago para {empleado.nombre}: ${empleado.calcular_pago()}")

"""
Esta solución utiliza una estructura de clases para calcular el pago de empleados con plaza fija y 
por horas. La clase base "Empleado" gestiona los datos comunes y el cálculo del bono por antigüedad, 
mientras que "EmpleadoPlazaFija" y "EmpleadoPorHoras" realizan cálculos específicos para cada 
tipo de empleado. Los datos se ingresan mediante "input()", permitiendo al usuario proporcionar la
información necesaria para los cálculos. Esta estructura facilita la gestión de diferentes 
tipos de empleados y sus pagos de manera organizada y extendible.
"""
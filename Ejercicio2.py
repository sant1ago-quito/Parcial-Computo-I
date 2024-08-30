"""
Un colegio privado desea registrar la asistencia de sus estudiantes a las
clases cada docente tiene su listado de los estudiantes en los cuáles se
les ha solicitado colocar a la par de cada estudiante si ha asistido, si
cuenta con permiso o tiene inasistencia con la fecha respectiva.
Actualmente esto se maneja por unas hojas de papel impreso y se
entregan al director al final del día; la escuela necesita agilizar este
proceso.
 Si el estudiante tiene un permiso el director necesita la razón de
dicha falta, ¿Cómo solventarías esta situación? Agrega tu
propuesta al código
"""
class Asistencia():
    def __init__(self,fecha,salon,nombre,asistencia,razon):
        self.fecha=fecha
        self.salon=salon
        self.nombre=nombre
        self.razon=razon
        self.asistencia=asistencia
    #mostrar los datos de la asistencia para el reporte 
    def mostrarDatos(self):
        print("*******************************")
        print(f"Fecha: {self.fecha}")
        print(f"Salón: {self.salon}")
        print(f"Nombre: {self.nombre}")
        print(f"Asistencia: {self.asistencia}")
        print(f"Comentarios: {self.razon if self.razon else 'N/A'}") 
        print("*******************************")

#Diccionario para el salon
salones = {
    "1A": ["Juan Pérez", "Ana Gómez"],
    "2B": ["Luis Martínez", "María López", "Carlos Sánchez"]
}
#funcion para tomar la asistencia
def tomar_asistencia():
    fecha = input("Ingresa la fecha: ")
    salon = input("¿Cuál es su salón? ").strip().upper()

    # Verificar que el salón existe en la lista
    if salon not in salones:
        print("Salón no válido. Intente de nuevo.")
        return tomar_asistencia()  # Volver a pedir si el salón no es válido

    alumnos = salones[salon]  # Obtener la lista de alumnos del salón
    registros = []

    # Recorrer la lista de alumnos y tomar asistencia
    for nombre in alumnos:
        estado = input(f"¿Cuál es el estado de {nombre}? (P: Presente, A: Ausente, M: Permiso): ").strip().upper()
        
        razon = ""
        if estado == 'M':  # Si el estado es "Permiso", se pide la razón
            razon = input(f"Razón del permiso para {nombre}: ").strip()
        elif estado == 'P' or estado == 'A':  # Si el estado es "Presente" o "Ausente"
            razon = "N/A"
        else:
            print("Estado no válido, por favor intente de nuevo.")
            return tomar_asistencia()  # Volver a pedir si la entrada no es válida

        registro = Asistencia(fecha, salon, nombre, estado, razon)
        registros.append(registro)

    # Mostrar el reporte de asistencia
    for i, registro in enumerate(registros, start=1):
        print(f"\nAsistencia {i}:")
        registro.mostrarDatos()

# Ejemplo de uso
tomar_asistencia()
"""
El usuario ingresa la fecha y selecciona el salón de clase. Si el salón no existe, se solicita nuevamente.
Se recorre la lista de estudiantes del salón seleccionado, y se solicita el estado de asistencia para cada uno.
Según el estado de asistencia (Presente, Ausente, Permiso), se maneja la razón de la falta:
Si es "Permiso", se pide que se ingrese la razón.
Si es "Presente" o "Ausente", se asigna "N/A" como razón.
Los registros de asistencia se almacenan en una lista registros.
Al final, se muestra un reporte para cada estudiante utilizando el método mostrarDatos de la clase Asistencia.
Este código permite tomar asistencia de manera eficiente utilizando una lista de alumnos predefinida para cada
salón. La simplicidad del flujo de trabajo mejora la experiencia del usuario al evitar la necesidad de 
ingresar manualmente los nombres de los estudiantes, permitiendo un proceso más rápido y menos propenso 
a errores.
"""

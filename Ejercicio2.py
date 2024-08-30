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

#funcion para tomar la asistencia
def tomar_asistencia():
    fecha = input("Ingresa la fecha: ")
    salon = input("¿Cuál es su salón? ")
    Alumnos = int(input("¿Cuántos alumnos son en su salón? "))
    alumnos = []

    for i in range(Alumnos):
        print(f"\nIngresar alumno y asistencia {i + 1}:")
        nombre = input("Nombre del alumno: ")
        estado = input(f"¿Cuál es el estado de {nombre}? (P: Presente, A: Ausente, M: Permiso): ").strip().upper()
        
        razon = ""
        if estado == 'M':  # Si el estado es "Permiso", se pide la razón
            razon = input(f"Razón del permiso para {nombre}: ").strip()
        elif estado == 'P':  # Si el estado es "Presente" queda "vacio"
            razon = "N/A"
        elif estado == 'A':  # Si el estado es "Ausente" queda "vacio"
            razon = "N/A"
        else:
            print("Estado no válido, por favor intente de nuevo.")
            return tomar_asistencia()  # Volver a pedir la asistencia si la entrada no es válida

        alumno = Asistencia(fecha, salon, nombre, estado, razon)
        alumnos.append(alumno)
    
    for i, alumno in enumerate(alumnos, start=1):
        print(f"\nAsistencia {i}:")
        alumno.mostrarDatos()

tomar_asistencia()

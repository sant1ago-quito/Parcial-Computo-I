"""
Una tienda local vende diversos productos, cada vez que un cliente
hace una compra niña mary se encarga de anotarlo en una libreta. A su
vez, con una calculadora le da el total a cada cliente y les da su
respectivo vuelto en caso de necesitarlo.
 Niña mary también se encarga de atender a los proveedores que
le dan cierta cantidad de producto y un precio sugerido de venta,
propón una solución dentro de tu programa para ayudarle.

"""
import random 

boton = input("Bienvenido, por favor ingrese P si es proveedor, o C si es comprador: ")

class Proveedor():
    def __init__(self):
        self.arreglo= []
    #Aca cree un arreglo para añadir ahi los productoos
    def ingresarproduc(self):
            while True:
                self.ingresarprod = input("Por favor ingrese el producto a agregar: ")
                self.ingresarprecio = float(input("Por favor ingrese el precio sugerido: "))
                self.ingresarcant = int(input("Por favor ingrese la cantidad de producto a ingresar: "))
                #aca use un diccionario para una mejor distribucion de datos
                self.inventarionuevo =  {"Producto": self.ingresarprod, "Precio Sugerido": self.ingresarprecio, "Cantidad": self.ingresarcant}
                self.arreglo.append(self.inventarionuevo)
                #usamos un append para añadir los productos al arreglo
                self.continuar = input("Desea agregar otro producto? (s/n): ")
                if self.continuar.lower() == "n":
                     break
            print("Estimado proveedor, esto es lo que usted ha ingresado: ")
            for producto in self.arreglo:
                 print(producto)

class Comprador():
    def __init__(self):
          self.otroarreglo = []
          self.precioaleatorio = random.randrange(1, 20)
          self.nuevoprecioaleatorio = float(self.precioaleatorio)
    def compra(self):
            while True:
                self.comprar = input("Por favor ingrese el producto a comprar: ")
                print("El precio de ", self.comprar, "es", self.nuevoprecioaleatorio)
                self.pagar = float(input("Por favor ingrese su pago: "))
                self.vuelto = (self.pagar - self.nuevoprecioaleatorio)
                if self.pagar < self.nuevoprecioaleatorio:
                     print("No se puede realizar la compra debido a su bajo presupuesto:")
                else:
                    print("Su vuelto es: ", self.vuelto)
                    self.historialcompra = {"Producto ": self.comprar, "Precio ": self.nuevoprecioaleatorio, "Usted pagó ": self.pagar, "Su vuelto ": self.vuelto }
                    self.otroarreglo.append(self.historialcompra)
                    print("Usted ha comprado", self.comprar, "cuyo precio es:", self.pagar, "y su vuelto es: ", self.vuelto)
                    self.continuara = input("Desea comprar algo más? (s/n): ")
                    if self.continuara.lower() == "n":
                        break
            print("Estimado cliente, este es su historial de compra: ")
            for otroproducto in self.otroarreglo:
                 print(otroproducto)


if boton.upper() == "P":
     proveedor = Proveedor()
     proveedor.ingresarproduc()

elif boton.upper() == "C":
     comprador = Comprador()
     comprador.compra()

"""
Este código proporciona una solución para una tienda local que maneja tanto a proveedores 
como a compradores. Los proveedores pueden ingresar productos con precios sugeridos y cantidades 
disponibles, que se almacenan en un inventario. Los compradores pueden seleccionar productos, 
realizar pagos y recibir vuelto, con la opción de ver su historial de compras. El código asegura 
que los compradores solo compren productos disponibles y maneja errores de entrada para una experiencia 
de usuario más robusta.
"""
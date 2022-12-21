from persona import Persona
from producto import Producto
from factura_detalle import FacturaDetalle
from datetime import datetime
fecha = datetime.now()

class Factura:
    """ Clase que implementa una factura"""

    def __init__(self, numero: int, cliente: Persona,fecha):
        self.serie: str = 'F001'
        self.numero: int = numero
        self.cliente: Persona = cliente
        self.base_imponible: float = 0.0
        self.igv: float = 0.0
        self.total: float = 0.0
        self.fecha = fecha
        self.detalle: FacturaDetalle = []
        print(self.convertir_a_string())
        pass

    def convertir_a_string(self):
        return print("| {} | {} | {} | {} |  base imponible: {} | IGV: {} | Total: {} | Fecha: {} |".format(self.serie, self.numero, self.cliente.dni, self.cliente.nombres, self.base_imponible, self.igv, self.total, self.fecha))

    def agregar_detalle(self, producto: Producto):
        self.detalle.append(FacturaDetalle(producto))
    def calcular_igv(self):
        for detalle in self.detalle:
            self.base_imponible=self.base_imponible+detalle.base_imponible
            self.igv=self.igv+detalle.igv
            self.total=self.total+detalle.total

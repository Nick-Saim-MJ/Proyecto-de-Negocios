class Producto:
    """ Clase que construye producto accesiorios electronicos"""

    def __init__(self, codigo, nombre, precio, marca, color, diseño, calidad):
        self.codigo: str = codigo
        self.nombre: str = nombre
        self.precio: str = precio
        self.marca: str = marca
        self.color: str = color
        self.diseño:str = diseño
        self.calidad:str = calidad
        print(self.convertir_a_string())
        pass

    def convertir_a_string(self):
        return print("| {} | {} | {} | {} | {} | {} | {} |".format(self.codigo, self.nombre, self.precio, self.marca, self.color, self.diseño, self.calidad))

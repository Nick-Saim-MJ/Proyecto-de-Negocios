from persona import Persona
from producto import Producto
from factura import Factura
from factura_detalle import FacturaDetalle
from datetime import datetime

personas: Persona = []
productos: Producto = []
factutas: Factura = []


lista_personas: list = [{"dni":"11111","nombres": "Henyelrey", "apellidos":"Garcia",
                         "direccion": "parque la paz", "telefono": "910200200"},
                         {"dni":"22222","nombres": "Nick", "apellidos":"Mayta",
                         "direccion": "seguro", "telefono": "910100100"},
                         {"dni":"33333","nombres": "Jhan", "apellidos":"Ramos",
                         "direccion": "estadio", "telefono": "910300300"},
                         {"dni":"44444","nombres": "David", "apellidos":"Romero",
                         "direccion": "jr. san martin", "telefono": "910400400"}]

lista_productos: list = [{"codigo": "1", "nombre": "audifonos", "precio": float(89), "marca": "decibel", "color": "negro", "diseño": "true wireles", "calidad": "media"},
                        {"codigo": "2", "nombre": "teclado", "precio": float(29), "marca": "missoni", "color": "negro", "diseño": "CYB K103 USB C", "calidad": "media"},
                        {"codigo": "3", "nombre": "mouse", "precio": float(49), "marca": "XBLADE", "color": "negro RGB", "diseño": "mouse gaming", "calidad": "media"},
                        {"codigo": "4", "nombre": "smartwatch", "precio": float(139), "marca": "Haylou", "color": "negro", "diseño": "LS0P IP68 GLOBAL VER", "calidad": "media"}]




def cargar_datos():
    for persona in lista_personas:
        persona: Persona = Persona(persona["dni"], persona["nombres"], persona["apellidos"], persona["direccion"], persona["telefono"] )
        personas.append(persona)

def datos_product():
    for producto in lista_productos:
        producto: Producto = Producto(producto["codigo"], producto["nombre"], producto["precio"], producto["marca"], producto["color"], producto["diseño"], producto["calidad"])
        productos.append(producto)

#Personas 
def persona():
    dni: str = str(input("Ingrese DNI: "))
    nombres: str = str(input("Ingrese Nombres: "))
    apellidos: str = str(input("Ingrese Apellidos: "))
    direccion: str = str(input("Ingrese Direccion: "))
    telefono: str = str(input("Ingrese Telefono: "))
    persona: Persona = Persona(dni, nombres, apellidos, direccion, telefono)
    personas.append(persona)
    

    


def listar_personas():
    for persona in personas:
        Persona.convertir_a_string(persona)


def buscar_persona():
    dni: str = str(input("Ingrese DNI para buscar persona: "))
    for persona in personas:
        if persona.dni == dni:
            Persona.convertir_a_string(persona)
            return persona


def editar_persona():
    dni: str = str(input("Ingrese DNI para buscar persona: "))
    for persona in personas:
        if persona.dni == dni:
            print("1. para el nombre") 
            print("2. para el apellido") 
            print("3. para la direccion") 
            print("4. para el telefono")
            c= int(input("ingrese el caso: "))
            
            if c == 1:
                persona.nombres = str(input("ingrese el nuevo nombre: "))
            if c == 2:
                persona.apellidos = str(input("ingrese el nuevo apellido: "))
            if c == 3:
                persona.direccion= str(input("ingrese la nueva direccion: "))
            if c == 4:
                persona.telefono= str(input("ingrese el nuevo telefono: "))
           
            Persona.convertir_a_string(persona)


def eliminar_persona():
    dni: str = str(input("Ingrese DNI para buscar persona: "))
    for indice, persona in enumerate(personas):
        if persona.dni == dni:
            personas.pop(indice)

#Productoooo
def producto():
    codigo: str = str(input("Ingrese código del producto: "))
    nombre: str = str(input("Ingrese nombre del producto: "))
    precio: float = float(input("Ingrese precio del producto: "))
    marca: str = str(input("Ingrese marca del producto: "))
    color: str = str(input("Ingrese el color del producto: "))
    diseño: str = str(input("Ingrese el diseño del producto: "))
    calidad: str = str(input("Ingrese la calidad del producto: "))
    producto: Producto = Producto(
        codigo, nombre, precio, marca, color, diseño, calidad)
    productos.append(producto)


def listar_producto():
    for producto in productos:
        Producto.convertir_a_string(producto)


def buscar_producto():
    codigo: str = str(input("Ingrese Código para buscar el producto: "))
    for producto in productos:
        if producto.codigo == codigo:
            Producto.convertir_a_string(producto)
            return producto

def editar_producto():
    codigo: str = str(input("Ingrese el codigo para buscar producto: "))
    for producto in productos:
        if producto.codigo == codigo:
            print("1. *   para el nombre   *") 
            print("2. *   para el precio   *") 
            print("3. *   para la marca    *") 
            print("4. *   para el color    *")
            print("5. *   para el diseño   *")
            print("6. *   para el calidad  *")
            p= int(input("ingrese el caso: "))
            
            if p == 1:
                producto.nombre = str(input("ingrese el nuevo nombre: "))
            if p == 2:
                producto.precio = str(input("ingrese el nuevo precio: "))
            if p == 3:
                producto.marca= str(input("ingrese la nueva marca: "))
            if p == 4:
                producto.color= str(input("ingrese el nuevo color: "))
            if p == 5:
                producto.diseño= str(input("ingrese el nuevo diseño: "))
            if p == 6:
                producto.calidad= str(input("ingrese la nueva calidad: "))

            Producto.convertir_a_string(producto)

def eliminar_producto():
    codigo: str = str(input("Ingrese el codigo para buscar producto: "))
    for indice, producto in enumerate(productos):
        if producto.codigo == codigo:
            productos.pop(indice)

#Factura
def nueva_factura():
    print("para generar una factura busca un cliente")
    fecha = datetime.now() 
    cliente: Persona = buscar_persona()
    factura: Factura = Factura(len(factutas)+1, cliente, fecha)
    continuar: bool = True

    while continuar:

        producto: Producto = buscar_producto()
        cantidad: int = int(input("Ingrese la cantidad: "))
        
        factura.detalle.append(FacturaDetalle(producto.codigo, producto.nombre, cantidad, producto.precio))

        condicion: str = str(input("SI para agregar productos: "))

        if condicion == "SI":
            continuar = True
        else:
            continuar = False
            factura.calcular_igv()
            factutas.append(factura)


def listar_factura():
    for factura in factutas:
        Factura.convertir_a_string(factura)


def buscar_factura():
    numero: int = int(input("Ingrese el numero de la factura: "))
    for factura in factutas:
        if factura.numero == numero:
            print("************************")
            print("*    TIENDAS PIPIPI    *")
            print("*   R.U.C 20220055000  *")
            print("*       FACTURA        *")
            print("************************")
            Factura.convertir_a_string(factura)
            print("===========================")

            for detalle in factura.detalle:
                FacturaDetalle.convertir_a_string(detalle)

def imprimir_detalle(numero):
    for factura in factutas:
        if factura.numero == numero:
            print("===========================")
            Factura.convertir_a_string(factura)
            print("===========================")

            for detalle in factura.detalle:
                FacturaDetalle.convertir_a_string(detalle)
        
def editar_factura():
    numero: int = int(input("Ingrese el numero de la factura: "))
    for factura in factutas:
        if factura.numero == numero:
            print("1) EDITAR CLIENTE")
            print("2) EDITAR PRODUCTO")
            opcion = int(input("ingrese la opcion: "))
            if opcion == 1:
                factura.cliente = buscar_persona()
            if opcion == 2:
                factura.producto = buscar_producto()
                


        
def eliminar_factura():
    numero: int = int(input("Ingrese el numero de la factura: "))
    for indice, factura in enumerate(factutas):
        if factura.numero == numero:
            factutas.pop(indice)
           
cargar_datos()
datos_product()


def main():
    continuar: bool = True

    while continuar:
        print("*****************************************")
        print("***********SISTEMA DE VENTAS*************")
        print("*   TIENDA DE ACCESORIOS ELECTRONICOS   *")
        print("-------------------MENÚ------------------")
        print("**************INGRESE OPCIONES***********")
        print("*       1: PARA MENU PERSONAS           *")
        print("*       2: PARA MENU DE PRODUCTO        *")
        print("*       3: PARA MENU DE FACTURA         *")
        print("*       4: PARA SALIR                   *")
        print("*****************************************")
        caso: str = str(input("INGRESE OPCIÓN: "))
        match caso:
            case "1":
                
                print("---------------------------")
                print("-  1) agregar persoonas   -")
                print("-  2) listar personas     -")
                print("-  3) buscar personas     -")
                print("-  4) editar personas     -")
                print("-  5) eliminar persona    -")
                cas:str = str(input("ingrese la opcion: "))
                match cas:
                    case "1":
                        persona()
                    case "2":
                        listar_personas()
                    case "3": 
                        buscar_persona()
                    case "4":
                        editar_persona()
                    case "5":
                        eliminar_persona()



            case "2":
                print("---------------------------")
                print("-  1) agregar producto    -")
                print("-  2) listar producto     -")
                print("-  3) buscar producto     -")
                print("-  4) editar producto     -")
                print("-  5) eliminar producto   -")
                menu_producto: str = str(input("ingrese la opcion: "))
                match menu_producto:
                    case "1":
                        producto()
                    case "2":
                        listar_producto()
                    case "3":
                        buscar_producto()
                    case "4":
                        editar_producto()
                    case "5":
                        eliminar_producto()

            case "3":
                print("---------------------------")
                print("-  1) agregar factura     -")
                print("-  2) listar factura      -")
                print("-  3) buscar factura      -")
                print("-  4) editar factura      -")
                print("-  5) eliminar factura    -")
                menu_factura:str=str(input("ingrese la opcion: "))
                match menu_factura:
                    case "1":
                        nueva_factura()
                    case "2":
                        listar_factura()
                    case "3":
                        buscar_factura()
                    case "4":
                        editar_factura()
                    case "5":
                        eliminar_factura()




            case "4":
                continuar = False


if __name__ == '__main__':
    main()

# Zona de clase
class refresqueria:
    #Zona de atributos
    id_venta = 0
    id_empleado = 0
    iantidad = 0
    pd_cliente = 0
    crecio = 0
    fecha = ""
    dire = ""
#funciones
    def mostrar(self):
        print(f"id venta: {ale.id_venta} \nid_empleado: {ale.id_empleado} \nid_cliente: {ale.id_cliente}")
        print(f"cantidad: {ale.cantidad} \nprecio: {ale.precio} \nfecha: {ale.fecha} \ndireccion: {ale.dire}")
    def lista_refe (self):
        lis_ref=[10,220,123,300,60000,"3 de Marzo del 2024","Calle San miguel 8231-41, Col. Santa Monica"]
        for x in lis_ref:
            print(x)
    def tupla_ref (self):
        tup_ref = (10,220,123,300,60000,"3 de Marzo del 2024","Calle San miguel 8231-41, Col. Santa Monica")
        for x in tup_ref:
            print(x)
    def dicc_ref(self):
        dic_ref = {"id venta: ": "010",
                    "id empleado:": "220",
                    "id cliente": 123,
                    "Cantidad": 300,
                    "Precio: ": 60000,
                    "Fecha: ":"3 de Marzo del 2024",
                    "Direccion: ":"Calle San miguel 8231-41, Col. Santa Monica"}
        for x,y in dic_ref.items():
            print(x,y)
    def alta_ref(self):
        print("Se dio de ALTA el pedido de la venta Coca-Cola")
    def baja_ref(self):
        print("Se dio de BAJA el pedido de la venta Coca-Cola")
# objetos
ale = refresqueria()

# Usando objetos
ale.id_venta = 10
ale.id_empleado = 220
ale.id_cliente = 123
ale.cantidad = 300
ale.precio = 600000
ale.fecha = "3 de Marzo del 2024"
ale.dire = "Calle San miguel 8231-41, Col. Santa Monica"

print("Mostrando datos")
ale.mostrar()
print("")
print("Lista de Refresqueria")
ale.lista_refe()
print("")
print("Tupla de Refresqueria")
ale.tupla_ref()
print("")
print("Diccionario de Refresqueria")
ale.dicc_ref()
print("")
ale.alta_ref()
print("")
ale.baja_ref()
# Zona de clase
class refresqueria:
    #Zona de atributos
    id_prod = 0
    nombre = ""
    tipo = ""
    sabor =""
    precio_uni = 0
    peso = ""

#funciones
    def mostrar(self):
        print(f"id producto: {ale.id_prod} \nNombre: {ale.nombre} \nTipo: {ale.tipo}")
        print(f"Sabor: {ale.sabor} \nprecio: {ale.precio_uni} \nPeso {ale.peso}")
    def lista_refe (self):
        lis_ref=[10,"Coca-Cola","Refresco","Cola",18,600]
        for x in lis_ref:
            print(x)
    def tupla_ref (self):
        tup_ref = (10,"Coca-Cola","Refresco","Cola",18,600)
        for x in tup_ref:
            print(x)
    def dicc_ref(self):
        dic_ref = {"id venta: ": "010",
                    "nombre: ": "Coca-Cola",
                    "tipo ": "Refresco",
                    "Sabor ": "Cola",
                    "Precio unidad: ": 18,
                    "peso: ": 600,}
        for x,y in dic_ref.items():
            print(x,y)
    def alta_ref(self):
        print("Se dio de ALTA el pedido de la venta Coca-Cola")
    def baja_ref(self):
        print("Se dio de BAJA el pedido de la venta Coca-Cola")
# objetos
ale = refresqueria()

# Usando objetos
ale.id_prod = 10
ale.nombre = "Coca-Cola"
ale.tipo = "Refresco"
ale.sabor = "Cola"
ale.precio_uni = 18
ale.peso = 600

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
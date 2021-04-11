class Producto():
    id=''
    ref =''
    nombre = ''
    referencia = ''
    valor = ''
    cantidad_inventario = ''
    def __init__(self, id, nombre, referencia, valor, cantidad_inventario):
        self.id = id
        self.nombre = nombre
        self.referencia = referencia
        self.valor = valor
        self.cantidad_inventario = cantidad_inventario
from Producto import Producto
contador = 0 
names_objects_id = {
}


def populate_data():
    productos = []
    inventario = []

    #---Popular productos ----
    id = autoIncrement('productos')
    producto_1 = Producto(
        id = id,
        nombre = 'Jabón en Polvo',
        referencia = 'producto_{}'.format(id),
        valor = '14500',
        cantidad_inventario = 10 
    )
    id = autoIncrement('productos')
    producto_2 = Producto(
        id = id,
        nombre = 'Arroz costal',
        referencia = 'producto_{}'.format(id),
        valor = '24000',
        cantidad_inventario = 10 
    )
    id = autoIncrement('productos')
    producto_3 = Producto(
        id = id,
        nombre = 'Panela',
        referencia = 'producto_{}'.format(id),
        valor = '5500',
        cantidad_inventario = 10 
    )
    id = autoIncrement('productos')
    producto_4 = Producto(
        id = id,
        nombre = 'Gelatina',
        referencia = 'producto_{}'.format(id),
        valor = '10000',
        cantidad_inventario = 10 
    )
    productos.append(producto_1)
    productos.append(producto_2)
    productos.append(producto_3)
    productos.append(producto_4)

    return {
        'productos' : productos
    }

def autoIncrement(name_object):
    if name_object in names_objects_id:
        contador = int(names_objects_id.get(name_object))
    else:
        contador = 0
    contador = contador+1
    names_objects_id[name_object] = contador
    return contador    

data = populate_data()
venta = []




def inicio():
    '''
    Esta función se encarga de dar la bienvenida y seleccionar entre realizar una venta, 
    o ver inventario
    '''
    print('********************** BIENVENIDO **********************')
    opcion = int(input('Digita 0 para realizar una venta\nó 1 para revisar el inventario'))
    if opcion == 0:
        registrarVenta()
    else:
        revisarInventario()

def registrarVenta():
    '''
    Esta función se encarga de agregar productos a una venta, verificar si existe el producto, 
    y si hay productos disponibles
    '''
    print('********************** Agrega productos a la venta **********************')
    productos = data.get('productos')
    referencia = input('Digita la referencia del producto')
    cantidad = int(input('Digite la cantidad de unidades'))
    producto_existe = False
    
    data_producto = {}
    for producto in productos:
        if producto.referencia == referencia:
            producto_existe = True
            if producto.cantidad_inventario >= cantidad:
                producto.cantidad_inventario = producto.cantidad_inventario-cantidad
                data_producto['producto'] = referencia
                data_producto['valor'] = int(producto.valor)*cantidad
                data_producto['nombre_producto'] = producto.nombre
                data_producto['cantidad'] = cantidad 
                venta.append(data_producto)
                break
            else:
                print('No hay suficientes productos en existencia')
                
    
    if producto_existe == False:
        print('Este producto no existe en nuestro sistema')
        registrarVenta()
    
    opcion = int(input('Digite 0 para agregar otro producto ó 1 para ver Factura'))
    if opcion == 0:
        registrarVenta()
    else:
        print(imprimirVenta())
        inicio()



def imprimirVenta():
    print('************************** LA FACTURA DE VENTA ************************** ')
    sentence = ''
    total = 0
    for producto in venta:
        sentence += '{}*{}(unidades) = {}\n'.format(producto.get('nombre_producto'),producto.get('cantidad'),producto.get('valor'))
        total = total + int(producto.get('valor'))
    sentence += 'TOTAL A PAGAR: {}'.format(total)
    return sentence

def revisarInventario():
    print('************************** PRODUCTOS EN INVENTARIO ************************** ')
    sentence = ''
    productos = data.get('productos')
    for producto in productos:
        sentence += '{} ref: {} -> cantidad:{}\n'.format(producto.nombre,producto.referencia,producto.cantidad_inventario)
    print(sentence)
    inicio()
inicio()



# Ejercicio de ejemplo
# teniendo el diccionario de pagos mensuales, define un algoritmo para calcular el pago que debes realizar mensualmente si solo debes pagar un tercio de los recibos sin incluir el internet

valores_servicios = { 
    'agua': 130000, 
    'luz': 150000, 
    'gas': 40000, 
    'internet': 90000 
}

pago_yo = ['agua', 'gas', 'luz']
pago_total = 0

for nombre_servicio, valor in valores_servicios.items():
    if nombre_servicio in pago_yo:
        pago_total = pago_total + (valor*0.33)

print(pago_total)

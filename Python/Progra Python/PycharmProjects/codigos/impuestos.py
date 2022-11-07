sueldo = int(input("ingrese su sueldo"))
if sueldo < 1000:
    impuesto = 0.00
if 1000<=sueldo<2000:
    impuesto = 0.05
if 2000<=sueldo<4000:
    impuesto = 0.10
if sueldo > 4000:
    impuesto = 0.12
print("lo que tienes que pagar en impuestos es", sueldo*impuesto)
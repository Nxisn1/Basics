a = int(input("ingrese su renta anual"))
if a<10000:
    print("debes pagar", a*0.05)
elif a<=10000 and a<20000:
    print("debes pagar", a * 0.15)
elif a<=20000 and a<35000:
    print("debes pagar", a * 0.20)
elif a<=35000 and a<60000:
    print("debes pagar", a * 0.30)
else:
    print("debes pagar", a * 0.45)
    print("culiao millo")
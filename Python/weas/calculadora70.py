
p1 = int(input("Ingrese nota certamen 1: "))
p2 = int(input("Ingrese nota certamen 2: "))

res = p1*0.3+p2*0.35
if res >= 55:
    print("Ya pasaste.")
else:
    x = (55-res)/0.35
    if(x > 100):
        print("F")
    else:
        print("Debes sacar un", x, "en el próximo certamen.")
input("")

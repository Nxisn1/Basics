def horas(x):
    a=x//60
    return a
def minutos(x):
    b=x%60
    return b
flag=True
x=0
while flag==True:
    j=int(input("ingresa cuantos minutos llevai de viaje"))
    x+=j
    if j==0:
        flag=False
print("llevas de viaje ", horas(x),"hora(s) y ",minutos(x), "minutos")
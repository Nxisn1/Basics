#W metodo write
try:
    f = open("nuevo.txt","w")
except OSError:
    print("no se puede abrir el archivo para escritura", f.name)
else:
    print("Bytes escritos: ", f.write("soy un nuevo archivo\nquiereme!!\n porfa :D\n no se que mas poner aquí"))
    f.close()
#intenté varias veces poner un read arriba pero mandaba un error de que no soportaba leerlo y creo que por que lo abrí de forma write (w)
# creo que para leerlo necesitas primero abrirlo como read (r)
f=open("nuevo.txt"); print(f.read())
f.close()

#a es para agregar cosas al final del archivo a=append/add, se pone cuando se abre 
f=open("nuevo.txt", "a")
print("Bytes escrito: ", f.write("\nla wea que sea"))
f.close()
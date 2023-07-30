# Peidir al usuario 3 numeros diferentes y indicar si alguno de ellos es la suma de los otros dos

# Pedimos 3 numeros diferentes

x = int(input("Pon un numero: "))
y = int(input("Otro numero diferente: "))
z = int(input("Otro numero diferente: "))

# Miramos si algunos de ellos es la suma de los otros dos e indicamos

if x==y+z:
    print("La suma del numero:",y,"y",z,"es igual a numero:", x)
elif y==x+z:
    print("La suma del numero:",x,"y",z,"es igual a numero:", y)
elif z==x+y:
    print("La suma del numero:",x,"y",y,"es igual a numero:", z)
else:
    print("No hay suma de los numeros introducidos")
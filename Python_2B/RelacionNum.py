# Peidir al usuario 3 numeros diferentes y indicar si alguno de ellos es la suma de los otros dos

# Pedimos 3 numeros diferentes

num1 = int(input("Pon un numero: "))
num2 = int(input("Otro numero diferente: "))
num3 = int(input("Otro numero diferente: "))

# Miramos si algunos de ellos es la suma de los otros dos e indicamos

if num1 + num2 == num3:
    print("La suma del numero:",num1,"y",num2,"es igual a numero:", num3)
elif num1 + num3 == num2:
    print("La suma del numero:",num1,"y",num3,"es igual a numero:", num2)
elif num3 + num2 == num1:
    print("La suma del numero:",num3,"y",num2,"es igual a numero:", num1)
elif num3 + num1 == num2:
    print("La suma del numero:",num3,"y",num1,"es igual a numero:", num2)

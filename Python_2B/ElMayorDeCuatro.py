# Pedir al usuario 4 numeros diferentes y imprimir el mayor de los cuatro

# Pedimos 4 numeros diferentes
num1 = int(input("Pon un numero: "))
num2 = int(input("Otro numero diferente: "))
num3 = int(input("Otro numero diferente: "))
num4 = int(input("Otro numero diferente: "))

# Comprobamos el mayor e imprimimos !

if num1 > num2 and num1 > num3 and num1 > num4:
    print("El numero mayor es: ", num1)
elif num2 > num3 and num2 > num4:
    print("El numero mayor es: ", num2)
elif num3 > num4: 
    print("El numero mayor es: ", num3)
else:
    print("El numero mayor es: ", num4)

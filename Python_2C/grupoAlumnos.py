# En uno de los cursos se ha dividido a una clase en dos grupos A y B.
# Para mezclar a los alumnos lo mejor posible se ha asignado a todas las chicas 
# con nombres empezando por letra E hasta la M en el grupo A y el resto en B
# A los chichos con nombre empezando por letra A hasta la H y R hasta la Z se les ha asignado al grupo A timbien, el resto estan en el B
# 
# Preguntar al usuario si es chica o chico y el nombre.
# Hay que mostrar por pantalla el grupo que le corresponde a ese alumno

# Preguntamos si es chica o chico y su nombre

genero = input("Ingresa tu genero (chica / chico): ")
nombre = input("Dime tu nombre: ")
nombres_chicas_A = "EHIJKLM"
nombres_chicos_A = "ABCDEFGHRSTUVWXYZ"

# Elegimos el grupo que corresponde
# chica
## E hasta M --> A
## El resto --> B

#chico
## A hasta H y R hasta Z --> A
## El resto --> B

if genero.lower() == "chica":
    if nombre[0].upper() in nombres_chicas_A:
        print("Tu grupo es el A")
    else:
        print("Tu grupo es el B")
elif genero.lower() == "chico":
    if nombres_chicos_A[0].upper() in nombres_chicos_A:
        print("Tu grupo es el A")
    else:
        print("Tu grupo es el B")
else:
    print("Introduzca bien tu genero!")

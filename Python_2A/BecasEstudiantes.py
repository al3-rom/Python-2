# El gobierno quere otorgar becas de excelencia a los estudiantes con un minimo de un 8 de media
# Para acceder a la beca, el estudiante debe tener entre 17 y 21 años
# 1.Pedir el nombre, la edad y la nota media del estudiante e indicar si puede optar a la beca o no

# Pedimos el nombre
estudiante = input("Pon tu nombre!: ")
# La edad
edad = int(input("Pon tu edad!: "))
edadApto = list(range(17,21))
# La nota media
nota = int(input("Pon tu nota media!: "))
notaApto = list(range(8,10))

if edad in edadApto and nota in notaApto:
 print("!Enhorabuena!", estudiante, "\n", "!Puedes pedir tu beca!")
else:
 print("Oh, pedimos disculpas,", estudiante, ", no puedes acceder a la beca!")
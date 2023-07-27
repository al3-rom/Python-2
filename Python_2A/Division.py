# 1.Pedir dos numeros
# 2.Mostrar por pantalla su division
# 3.Si divisor es 0 el programa tiene que mostrar "Error"

# Pidimos numeros
num1 = int(input("Pon un numero para una division: "))
num2 = int(input("Pon otro numero: "))

# Si num1 o num2 es 0 - mostramos error
# Hacemos funcion, si el num1 o num2 no es 0, dividimos y mostramos el resultado
# !Primero hay que mostrar error, saldra error de programa a la hora de intentar dividir los numeros!

if num1 or num2 == 0:
 print("Error 404, no se puede devidir en 0")
else:
  division = (num1/num2)
  print("La division de los numeros:",num1,"y",num2,"es:", division)



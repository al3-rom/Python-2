# 1.Pedir dos numeros
# 2.Mostrar por pantalla su division
# 3.Si divisor es 0 el programa tiene que mostrar "Error"

# Pidimos numeros
n = float (input("Intorduce el dividendo: "))
m = float (input("Introduce el divisor: "))

# Si num1 o num2 es 0 - mostramos error
# Hacemos funcion, si el num1 o num2 no es 0, dividimos y mostramos el resultado


if m == 0.0:
  print("Error 404, no se puede devidir por 0")
else:
  division = n/m
  print("La division de los numeros:", n ,"y", m ,"es:", division)

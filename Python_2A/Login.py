 # Pedimos una contraseña(ordenador sabe cual es correcta)
 # Si contraseña es correcta, damos la bienvenida al usuario
 # Si no es correcta, demos segunda oportunidad para introducir la contraseña
 # AL segundo fallo mostramos un mensaje de error

 # Ponemos nuestra contraseña correcta

password1 = "vexisthebest1"

 # Pedimos una contraseña al usuario
passUser = input("Pon la contraseña del usuario: ")
 # Creamos la funcion, para comprobar si la contraseña es correcta o no

if passUser == password1:
  print("!Bienvenido Alejandro!")
else:
  print("Incorrecto! Tienes segunda oportunidad! ")
  passUser=input("Pon la contraseña del usuario: ")
if passUser == password1:
  print("!Bienvenido Alejandro!")
else:
  print("Error, la contraseña no es correcta!")
  print("Cerramos el sistema!")



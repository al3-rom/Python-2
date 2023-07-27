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
 print("!Bienvenida Alejandro!")

else:
  print("Incorrecto! Tienes segunda oportunidad! ")
  passUser=input()
  

if passUser != password1:
  print("!Error al entrar a la cuenta del usuario!")
else:
  #No se como parar el codigo
  print("Bienvenida Alejandro!!")

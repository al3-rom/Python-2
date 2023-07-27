# Un ordenador tiene 3 usuarios(Alejandro, Naomi y Sergio) y otro usuario invitado
# 1. Pedir el nombre al usuario y dar una bienvenida personalizada.
# *(Si el usuario no es ninguno de los tres, se le de un saludo generico)
# !Prevenir error si el nombre es en minusculas, mayusculas, con punto y con almohadilla!

# Creamos variables
user1 = "Alejandro"
user2 = "Naomi"
user3 = "Sergio"
invitado = input("Hola, pon tu nombre!: ")

# Comprobamos el nombre y imprimimos por pantalla
if invitado == user1:
    print("Buenas dias ", user1, ", te doy un saludo!")
elif invitado == user2:
   print("Buenas dias ", user2, ", te doy un saludo!")
elif invitado == user3:
   print("Buenas dias ", user3, ", te doy un saludo!")
else:
   print("Buenas dias", invitado,"!")




# Un ordenador tiene 3 usuarios(Alejandro, Naomi y Sergio) y otro usuario invitado
# 1. Pedir el nombre al usuario y dar una bienvenida personalizada.
# *(Si el usuario no es ninguno de los tres, se le de un saludo generico)
# !Prevenir error si el nombre es en minusculas, mayusculas, con punto y con almohadilla!

# Creamos variables
user1 = "alejandro"
user2 = "naomi"
user3 = "sergio"
invitado = input("Hola, pon tu nombre!: ")

# Prevenimos error si el si el nombre es en minusculas o mayusculas, con punto o con almohadilla!
invitado = invitado.lower()
invitado = invitado.replace(".", "")
invitado = invitado.replace("#", "")



# Comprobamos el nombre y imprimimos por pantalla
if invitado == user1:
    print("Buenas dias ", user1.title(), ", te doy un saludo!")
elif invitado == user2:
   print("Buenas dias ", user2.title(), ", te doy un saludo!")
elif invitado == user3:
   print("Buenas dias ", user3.title(), ", te doy un saludo!")
else:
   print("Buenas dias", invitado.title(),"!")




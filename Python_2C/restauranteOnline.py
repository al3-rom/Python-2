# En una hamburgueseria han abierto la posibilidad de hacer pedidos online.
# Ofrecen basicamente dos productos de fama mundial: hamburguesa clasica y vegana

# Los ingredientes extra de la hamburguesa clasica son:
#  -Queso idiazabal
#  -Bacon
#  -Huevo

# De vegana:
#  -Tofu
#  -Cebolla caramelizada

# Preguntar al usuario que tipo de hamburguesa quiere. 
# En funcion de la respuesta hay que enseñar los ingredientes extra disponibles y permetir escoger uno de ellos.
# Imprimir que tipo de hamburguesa se ha elegido y cuales son sus ingredientes.

# Preguntamos que tipo de hamburguesa quiere y en funcion de la respuesta, enseñamos los los ingredientes extra disponibles

hamburguesaUser = input( "Que hamburguesa te apetece? Tenemos clasica y vegana!: ")

if hamburguesaUser.lower() == "clasica":
   Ingredientes = input("Ingredientes exta disponibles para clasica son: -queso, -bacon y huevo, escoge un ingrediente!: ")
elif hamburguesaUser.lower() == "vegana":
  Ingredientes = input("Ingredientes exta para vegana disponibles son: -tofu y -cebolla, escoge un ingrediente!: ")
else:
   print("Lo sentimos, tenemos solo estas 2 hamburguesas!")

# Imprimimos que tipo de hamburguesa se ha elegido y cuales son sus ingredientes.
if hamburguesaUser.lower() == "clasica":
    print("Tu tipo de hamburguesa es:", hamburguesaUser, "y tu exta es:", Ingredientes)
elif hamburguesaUser.lower() == "vegana":
    print("Tu tipo de hamburguesa es:", hamburguesaUser, "y tu exta es:", Ingredientes)


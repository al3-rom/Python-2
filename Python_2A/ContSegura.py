# Crear una contraseña 
# 1.Debe tener una vocal en minuscula
# 2.Un simbolo especial (Solo * o #)
# 3.Comprobar si es una contraseña segura y imprimir por pantalla

# Pedimos contraseña al usuario
password = input("Introduce la contraseña: ")


# Comprobamos la contraseña
if ("a" in password or "e" in password or "o" in password) and ("*" in password or "#" in password):
    print("!La contraseña es segura!")
else:
    print("La contraseña no es segura! :( ")



# Permitir que el usuario introduzca una letra(del alfabeto latino) como input. Comprombar si esta es una mayuscula o una minuscula


# Pedimos una letra
letra = input("Pon una letra: ")

# Comprobamos si en una mayuscula o minuscula
if letra.islower():
    print("La letra:", letra, "es una minuscula")
elif letra.isupper():
    print("La letra:", letra, "es una mayuscula")
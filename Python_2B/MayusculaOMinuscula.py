# Permitir que el usuario introduzca una letra(del alfabeto latino) como input. Comprombar si esta es una mayuscula o una minuscula

letra = input("Pon una letra: ")

if letra.islower():
    print("La letra:", letra, "es una minuscula")
elif letra.isupper():
    print("La letra:", letra, "es una mayuscula")
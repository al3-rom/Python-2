# 1.Comprobar un numero y una potencia
# 2.Si ese numero elevado a esa potencia es par o impar 

num1 = int(input("Pon un numero: "))
num2 = int(input("Potencia para este numero: "))

elev = (num1 * num2)


if elev % 2 == 0:
    print("Numero: ", num1, "elevado a", num2, "es par")
else:
    print("Numero:", num1, "elevado a", num2, "es impar")

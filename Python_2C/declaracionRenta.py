# Comprobar si soy mayor de edad(para poder pagar impuestos) y en caso afirmativo imprimir cual tocaria
# RENTA            TIPO IMPOSITIVO
# > 15k eu             5%
# 15k - 20k eu         15%
# 25k - 35k eu         20%
# 35k - 60k eu         30%
# 60K+                  45%

# Comprobamos si es apto para pagar impuestos o no

edad = input("Pon tu edad!: ")
edad = int(edad)
pagar = False

if edad >= 18:
    print("Muy bien, puedes pagar impuestos!")
    pagar = True
else:
    print("Eres menor de edad, no tienes que pagar impuestos!")
    pagar = False

# Preguntamos su sueldo y calculamos que impuesto le toca

if pagar == True:
  nomina = int(input("Cuanto cobras al mes?: "))
  nomina = nomina * 12
  if nomina <= 15000:
    print("Te tocaria pagar 5% de impuestos, al año son: ", nomina * 0.05)
  elif nomina > 15000 and nomina < 25000:
    print("Te tocaria pagar 15% de impuestos, al año son: ", nomina  * 0.15)
  elif nomina > 25000 and nomina < 35000:
    print("Te tocaria pagar 20% de impuestos, al año son: ", nomina * 0.2)
  elif nomina > 35000 and nomina < 60000 :
    print("Te tocaria pagar 30% de impuestos, al año son: ", nomina * 0.3)
  elif nomina >= 60000:
     print("Te tocaria pagar 45% de impuestos, al año son: ", nomina * 0.45)


 






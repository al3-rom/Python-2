# Pedir al usuario 3 longitudes
long1 = float(input("Ingresa la primera longitud: "))
long2 = float(input("Ingresa la segunda longitud: "))
long3 = float(input("Ingresa la tercera longitud: "))
# Comprobar si pueden conformar un triangulo (Para 3 longitudes)
# long2 + long3 > long1
# long1 + long3 > long2
# long1 + long2 > long3 
if long1 + long2 > long3 and long1 + long3 > long2 and long2 + long3 > long1:
    print("Con las piezas puedes crear un trianagulo")
else:
    print("Con las piezas no podras crear un tiangulo")


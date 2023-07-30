# Dado un precio introducido por el usuario, si el precio
# del producto esta por debajo de 100 dolares, el bot imprima por pantalla la orden de comprar
# Si esta entre 100 y 150 dolares el bot debera imprimir la orden de hold
# Si el precio esta estrictamente por encima de 150 el bot debera imprimir la orden de vender

# Pedimos el precio
precio = float(input("Ingresa el precio en $: "))
# Comprobamos el precio y vemos si debemos comprar, holdear o vender
if precio < 100.0:
    print("Es hora de comprar")
elif 100 <= precio <= 150:
    print("Toca holdear")
else: 
    print("Es hora de vender")
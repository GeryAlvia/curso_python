#56. Realiza un programa que gestione un establecimiento de venta de bocadillos. Un pedido se compone de: bocadillo, acompañamiento y bebida. Un cliente puede pedir más de un pedido. El dependiente a partir del menú (ver imagen), se encarga de introducir los datos. El menú solo se visualiza una vez al ejecutar el programa. El programa debe preguntar al dependiente tras la realización de un pedido, si quiere gestionar otro. 
#El establecimiento contempla los siguientes descuentos:
#Si el total a pagar es entre 20 y 30 euros, se aplica un descuento del 5%
#Si el total a pagar es superior a 30 euros, se aplica un descuento del 15%
#Una vez se finaliza la introducción de todos los pedidos de un cliente, debe aparecer por pantalla:
#• El número de pedidos realizados
#• Total a pagar.
#• Total con IVA (10%)
#• Total con el descuento aplicado.
import time
Repetir=True
precio=0
while Repetir:
    print("MENÚ")
    time.sleep(0.5)
    print("1. Bocadillo de calamares - 9 €")
    time.sleep(0.5)
    print("2. Bocadillo de chistorra - 4.5 €")
    time.sleep(0.5)
    print("3. Bikini de jamón - 2.5 €")
    time.sleep(0.5)
    Input = input("Introduzca su elección: ")
    if Input == "1": precio += 9
    elif Input == "2": precio += 4.5
    elif Input == "3": precio += 2.5
    else: exit
    time.sleep(0.5)
    print("ACOMPAÑAMIENTO")
    time.sleep(0.5)
    print("1. Patatas fritas finas - 1.5 €")
    time.sleep(0.5)
    print("2. Patatas gruesas - 1.75 €")
    time.sleep(0.5)
    print("3. Patatas rústicas - 2 €")
    time.sleep(0.5)
    Input = input ("Introduzca su elección: ")
    if Input == "1": precio += 1.5
    elif Input == "2": precio += 1.75
    elif Input == "3": precio += 2
    else: exit
    time.sleep(0.5)
    print("BEBIDAS")
    time.sleep(0.5)
    print("1. Coca cola - 2")
    time.sleep(0.5)
    print("2. Aquarius - 1.5 €")
    time.sleep(0.5)
    print("3. Agua - 1 €")
    time.sleep(0.5)
    Input = input ("Introduzca su elección: ")
    if Input == "1": precio += 2
    elif Input == "2": precio += 1.5
    elif Input == "3": precio += 1
    else: exit
    if input("Quiere pedir otro menú? (s/n) ") == "s": Repetir = True
    else: Repetir = False
print(f"Total a pagar: {precio}")
print(f"Total a pagar con IVA (10%): {precio+precio*0.1} ")
print(f"Total a pagar con descuento {round(precio*.85,2)}")


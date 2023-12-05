#56. Realiza un programa que gestione un establecimiento de venta de bocadillos. Un pedido se compone de: bocadillo, acompañamiento y bebida. Un cliente puede pedir más de un pedido. El dependiente a partir del menú (ver imagen), se encarga de introducir los datos. El menú solo se visualiza una vez al ejecutar el programa. El programa debe preguntar al dependiente tras la realización de un pedido, si quiere gestionar otro. 
#El establecimiento contempla los siguientes descuentos:
#Si el total a pagar es entre 20 y 30 euros, se aplica un descuento del 5%
#Si el total a pagar es superior a 30 euros, se aplica un descuento del 15%
#Una vez se finaliza la introducción de todos los pedidos de un cliente, debe aparecer por pantalla:
#• El número de pedidos realizados
#• Total a pagar.
#• Total con IVA (10%)
#• Total con el descuento aplicado.

def calcular_descuento(total):
    if 20 <= total <= 30:
        return total * 0.05
    elif total > 30:
        return total * 0.15
    else:
        return 0
def mostrar_menu():
    print("Menú:")
    print("1. Bocadillo de calamares- 9 €")
    print("2. Bocadillo de chistorra - 4.5 €")
    print("3. Bikini de jamón - 2.5 €")
    print("ACOMPAÑAMIENTO")
    print("1. Patatas finas - 1.5 €")
    print("2. Patatas gruesas - 1.75 €")
    print("3. Patatas rústicas - 2 €")
    print("BEBIDAS")
    print("1. Coca cola - 2 €")
    print("2. Aquarius - 1.5 €")
    print("3. Agua - 1 €")
num_pedidos = 0
total_pagar = 0
while True:
    if num_pedidos == 0:
        mostrar_menu()
    bocadillo = int(input("Elige que tipo de bocadillo deseas: "))
    acompañamiento = int(input("Que acompañamiento desearia usted escojer?: "))
    bebida = int(input("Que bebida le apetece?: "))
    total_pedido = (bocadillo * 5) + (acompañamiento * 3) + (bebida * 2)
    total_pagar += total_pedido
    print("\nResumen del pedido:")
    print(f"Bocadillos: {bocadillo} x 5 euros = {bocadillo * 5} euros")
    print(f"Acompañamientos: {acompañamiento} x 3 euros = {acompañamiento * 3} euros")
    print(f"Bebidas: {bebida} x 2 euros = {bebida * 2} euros")
    print(f"Total a pagar por este pedido: {total_pedido} euros")

    gestionar_otro = input("\n¿Desea gestionar otro pedido? (s/n): ")
    if gestionar_otro.lower() != 's':
        break
    num_pedidos += 1
descuento = calcular_descuento(total_pagar)
total_con_descuento = total_pagar - descuento
total_con_iva = total_con_descuento * 1.1
print(f"\nNúmero de pedidos realizados: {num_pedidos + 1}")
print(f"Total a pagar: {total_pagar}")
print(f"Total con IVA (10%): {total_con_iva} euros")
print(f"Precio total con descuento del: {total_con_descuento} euros (Descuento: {descuento} euros)")
input()         

#56b.Opcional. Haz alguna o todas las mejoras en el programa anterior que a continuación se indican:
#- Cuando se pregunta “si desea realizar otro pedido”, el encargado puede introducir s ó n en mayúscula o minúscula.
#- Si el encargado introduce otro valor distinto a S o N, el programa debe repetir la pregunta e informar de que ha introducido un valor equivocado.
#- El lugar de almacenar los precios en variables, utiliza una biblioteca (busca información) e investiga como moverte por los índices.
#- Un pedido puede estar formado por 3, 2 o 1 componentes. Ej. Un usuario puede pedir únicamenteuna bebida.
import time
menu = {
    'bocadillo': {'Bocadillo de calamares': 9, 'Bocadillo de chistorra': 4.5, 'Bikini de jamón': 2.5},
    'acompañamiento': {'Patatas finas': 1.5, 'Patatas gruesas': 1.75, 'Patatas rústicas': 2},
    'bebida': {'Coca cola': 2, 'Aquarius': 1.5, 'Agua': 1}
}
def calcular_descuento(total):
    if 20 <= total <= 30:
        descuento = 0.05
    elif total > 30:
        descuento = 0.15
    else:
        descuento = 0
    return total * (1 - descuento)
def main():
    repetir = True
    precios = {'bocadillo': 0, 'acompañamiento': 0, 'bebida': 0}
    while repetir:
        print("\nMENÚ")
        time.sleep(0.5)
        for categoria, opciones in menu.items():
            print(f"{categoria.capitalize()}:")
            for i, (nombre, precio) in enumerate(opciones.items(), start=1):
                print(f"{i}. {nombre} - {precio} €")
                time.sleep(0.5)

            cantidad = int(input(f"¿Cuántos {categoria}s desea? "))
            for _ in range(cantidad):
                eleccion = int(input(f"Seleccione un {categoria} (1-{len(opciones)}): "))
                precios[categoria] += list(opciones.values())[eleccion - 1]

        if input("¿Quiere realizar otro pedido? (s/n) ").lower() not in ['s', 'n']:
            print("¡Valor incorrecto! Por favor, introduzca 's' para continuar o 'n' para salir.")
            continue

        if input("¿Quiere realizar otro pedido? (s/n) ").lower() != 's':
            repetir = False
    total_pagar = sum(precios.values())
    total_con_iva = total_pagar * 1.10
    total_con_descuento = calcular_descuento(total_pagar)
    print(f"\nRESUMEN")
    print(f'Número de pedidos: {len(precios)}')
    print(f'Total a pagar: {total_pagar} €')
    print(f'Total con IVA: {total_con_iva} €')
    print(f'Precio total con descuento del 5%: {total_con_descuento} €')
if __name__ == "__main__":
    main()

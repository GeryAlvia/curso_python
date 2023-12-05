#40. Crea un programa que cuente todos los números pares hasta el número 50
numero = 1
total_pares = 0
total_impares = 0
while numero <= 50:
     if numero % 2 == 0:
        total_pares += 1
else:
        total_impares += 1
numero += 1
print(f"El total de pares es: {total_pares}")
print(f"El total de impares es: {total_impares}")
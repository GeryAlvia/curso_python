#34. Corrige los 4 errores o añade el código que necesites para que el siguiente programa se ejecute correctamente

var_numero = 6734
var_suma = 0
var_numero_str = str(var_numero)
for digito in var_numero_str:
    var_suma += int(digito)
if var_suma % 2 == 0:
    print(f"El valor de {var_suma} es par")
else:
    print(f"El valor de {var_suma} es impar")
input()

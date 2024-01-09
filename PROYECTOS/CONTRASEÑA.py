#La contraseña
print("INSTRUCCIONES")
print("1.La longitud del password té que tenir entre 6 i 8 caracteres")
print("2.Fuerza los siguientes valores según la posición indicada:")
print("     Posición 1 Un número mayor o igual a 1 y menor o igual que 5")
print("     Posición 2 Una letra minúscula")
print("     Posición 3 Una letra mayuscula")
print("     Posición 4 Uno de estos símbolos *, _, @")
print("     Posición 5 Una letra minúscula")
print("     Posición 6 Un número mayor o igual a 6 y menor o igual que 9")
print("     Posición 7 Uno de estos símbolos &,/,#")
print("     Posición 8 Un número menor o igual que 5")
contraseña = input("Introduce la contraseña clave: ")
errores = []
if not(len(contraseña)==6 or len(contraseña)==7 or len(contraseña)==8):
    errores.append("Error: La contraseña debe tener exactamente entre 6  7 u 8 caracteres.")
else:
    if not (1 <= int(contraseña[0]) <= 5):
        errores.append("Error en el caracter 1")
    if not contraseña[1].islower():
        errores.append("Error en el caracter 2")
    if not contraseña[2].isupper():
        errores.append("Error en el caracter 3")
    if contraseña[3] not in "*_@":
        errores.append("Error en el caracter 4")
    if not contraseña[4].islower():
        errores.append("Error en el caracter 5")
    if not (6 <= int(contraseña[5]) <= 9):
        errores.append("Error en el caracter 6")
    if len(contraseña)>=7:
        if contraseña[6] not in "&/#":
            errores.append("Error en el caracter 7")
    if len(contraseña)==8:
        if not (int(contraseña[7]) <= 5):
            errores.append("Error en el caracter 8")
if errores:
    print(errores)
else:
    print("El format del PASSWORD és correcte")
input()
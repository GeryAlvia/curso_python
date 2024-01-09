#67. Realiza de nuevo el programa de Password (fase 2). El password debe tener las siguientes consideraciones:
#Debe tener una longitud entre 6 y 8 caracteres.
#Debe contener como mínimo:
#2 números mayores o iguales que 1 y menor o igual que 5
#2 letras minúsculas
#1 letra mayúscula
#2 símbolos (*, _, @, &,/,#)
#1 número mayor o igual que 6 y menor o igual que 5
password = input("Introdueix la paraula clau: ")
errors = ""
Apariciones=0
Len = len(password)
x=0
if not (6 <= Len <= 8):
    errors += ("Error, la longitud del password ha de tenir entre 6 i 8 dígits")
else:
    for x in range (0,Len):
        if password[x].isnumeric():
            if (1 <= int(password[0]) <= 5): Apariciones += 1
    if Apariciones < 2: errors += "El password ha de tenir almenys dos nombres entre l'1 i el 5 (incluits). "
    Apariciones=0; x=0
    for x in range (0,Len):
        if password[x].islower(): Apariciones += 1
    if Apariciones < 2: errors += "El password ha de tenir almenys dos lletres minúscules"
    Apariciones=0; x=0
    for x in range (0,Len):
        if password[x].isupper(): Apariciones += 1
    if Apariciones < 1: errors += "El password ha de tenir almenys una lletra majúscula"
    Apariciones=0; x=0
    for x in range (0,Len):
        if password[x] in ['*','_','@','&','/','#']: Apariciones +=1
    if Apariciones < 2: errors += "El password ha de tenir almenys dos símbols ('*','_','@','&','/','#')"
    Apariciones=0; x=0
    for x in range (0,Len):
        if password[x].isnumeric(): Apariciones += 1
    Apariciones=0; x=0 
if errors == "":
    errors = "El format del PASSWORD és correcte"
print(errors)
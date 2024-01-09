#68. Añade al ejercicio anterior la posibilidad de que el programa pregunte si deseas o no continuar introduciendo passwords. Ej. “¿Deseas introducir otro password s/n?
password = input("Introdueix la paraula clau: ")
errors = ""
Apariciones=0
Len = len(password)
x=0
Repetir="s"
while Repetir == "s":
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
    Repetir = input("Desitja introduir un altre password? (s/n)")
print("Fi del programa")
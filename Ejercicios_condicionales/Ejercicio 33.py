#33. Programa un código que permita contar el número de vocales de la siguiente frase: No hay mal que dure cien años


frase = "No hay mal que dure cien años"
a_count = 0
e_count = 0
i_count = 0
o_count = 0
u_count = 0
frase = frase.lower()
for letra in frase:
    if letra == 'a':
        a_count += 1
    elif letra == 'e':
        e_count += 1
    elif letra == 'i':
        i_count += 1
    elif letra == 'o':
        o_count += 1
    elif letra == 'u':
        u_count += 1
print("El número de a es",a_count,"el número de e es",e_count,"el número de i es",i_count,"el número de o es",o_count,"y el número de u es",u_count,"")


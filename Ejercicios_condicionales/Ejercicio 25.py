#25. Repite el programa número 23 pero en esta ocasión utilizando operadores lógicos.
nota = float(input("Introduce la nota: "))
if nota >=8 and nota <=11:
        print(f"La nota es un {nota} Excelente")    
elif nota >=6.5 and nota <=8:
        print (f"La nota es un {nota} Notable")
elif nota >=5 and nota <6:
        print(f"La nota es un {nota} Satisfactorio")
elif nota <5 and nota>-1:
        print(f"La nota es un {nota} Insuficiente")
else:
    print("La nota esta fuera de los parametros")
input()
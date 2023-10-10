#12. Realiza un programa que, introduciendo en los valores de lado, base menor, base mayor y altua de un trapecio isósceles, nos devuelva por pantalla en el área y el perímetro.


alt=int(input("Introduce la altura del trapecio: "))
menor=int(input("Introduce base mayor: "))
mayor=int(input("Introduce base menor: "))
lado=input("Introduce el lado: ")
per=int(lado)*2+int(menor)+int(mayor)
A=float((menor)+float(mayor))*float(alt)/2
print("El perímetro es: ",per)
print("El área es: ",A)
input()

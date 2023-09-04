'''
Salamone Constanza

Ejercicio 2:
Pedir una edad. Informar si la persona es mayor de edad (más de 18 años), adolescente (entre 13 y 17 años) o niño (menor a 13 años).

'''

edad = int(input("Ingrese su edad: "))

if edad > 18:
    print("La persona es mayor de edad")
else:
    if edad >= 13: 
        print("Es un adolescente")
    else: 
        print("Es un niño/a")
    


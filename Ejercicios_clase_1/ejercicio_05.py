'''
Salamone Constanza


Ejercicio 5:
Una agencia de viajes debe sacar las tarifas de los viajes , se cobra $15.000
por cada estadía como base, se pide el ingreso de una estación del
año(Invierno/Verano/Otoño/Primavera) y localidad(Bariloche/Cataratas/Mar del
Plata/Córdoba) para vacacionar para poder calcular el precio final:

-en Invierno: Bariloche tiene un aumento del 20% Cataratas y Córdoba tiene un
descuento del 10% Mar del Plata tiene un descuento del 20%

-en Verano: Bariloche tiene un descuento del 20% Cataratas y Córdoba tiene
un aumento del 10% Mar del Plata tiene un aumento del 20%

-en Otoño y Primavera: Bariloche tiene un aumento del 10% Cataratas tiene un
aumento del 10% Mar del Plata tiene un aumento del 10% y Córdoba tiene el
precio sin descuento.

Validar el ingreso de datos


'''
precio_base= 15000
descuento_aumento = 0


estacion = input('Ingrese la estacion en la que viajará (Invierno/Verano/Otoño/Primavera):  ')
while estacion != 'Invierno' and estacion != 'Verano' and estacion != 'Otoño' and estacion != 'Primavera':
    estacion = input('Verifique que las estaciones válidas son: Invierno/Verano/Otoño/Primavera  ')

localidad = input('Ingrese el destino (Bariloche/Cataratas/Mar del Plata/Cordoba): ')
while localidad != 'Bariloche' and localidad != 'Cataratas' and localidad != 'Mar del Plata' and localidad != 'Cordoba':
    localidad = input('Verifique que las localidades válidas son:  Bariloche/Cataratas/Mar del Plata/Cordoba ')


if estacion == 'Invierno':
    if localidad == 'Bariloche':
        descuento_aumento = 1.2
    else:
        if localidad == 'Cordoba' or localidad == 'Cataratas':
            descuento_aumento = 0.9
        else:
            if localidad == 'Mar del Plata':
                descuento_aumento = 0.8 

if estacion == 'Verano':
    if localidad == 'Bariloche':
        descuento_aumento = 0.8
    else:
        if localidad == 'Cordoba' or 'Cataratas':
            descuento_aumento = 1.1
        else:
            if localidad == 'Mar del Plata':
                descuento_aumento = 1.2

if estacion == 'Otoño' or estacion == 'Primavera':
    if localidad == 'Bariloche' or localidad == 'Cataratas' or localidad == 'Mar del Plata':
        descuento_aumento = 1.1
    else:
        if localidad == 'Cordoba':
            descuento_aumento = 1

precio_final = precio_base * descuento_aumento

print(precio_final)


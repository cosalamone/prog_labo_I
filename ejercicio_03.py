'''
Salamone constanza

Ejercicio 3

Ingresar 5 números enteros, distintos de cero.
Informar:
a. Cantidad de pares e impares.
b. El menor número ingresado.
c. De los pares el mayor número ingresado.
d. Suma de los positivos.
e. Producto de los negativos.

'''


lista_numeros = []
lista_par = []
lista_impar = []
mensaje = ""

for i in range(5):
    
    numero = int(input("Ingrese un numero: "))
    while numero == 0:
        numero = int(input("El número ingresado no puede ser 0: "))
        
    lista_numeros.append(numero)

for numero in lista_numeros:
    if numero % 2 == 0:
        lista_par.append(numero)
    else:
        lista_impar.append(numero)

cant_numeros_pares = len(lista_par)
cant_numeros_impares = len(lista_impar)

mensaje += f"Se ingresaron {cant_numeros_pares} numeros pares\n"
mensaje += f"Se ingresaron {cant_numeros_impares} numeros impares\n"

menor_numero_ingresado = None

for menor in lista_numeros:
    if menor_numero_ingresado == None or menor < menor_numero_ingresado:
        menor_numero_ingresado = menor

mensaje += f"El menor numero ingresado fue el: {menor_numero_ingresado}\n"


mayor_numero_par = None

for mayor in lista_par:
    if mayor_numero_par == None or mayor > mayor_numero_par:
        mayor_numero_par = mayor

mensaje += f"El mayor numero par ingresado fue el: {mayor_numero_par}\n"


suma_positivos = 0

for num in lista_numeros:
    if num > 0:
        suma_positivos += num

mensaje += f"El resultado de la suma de todos los numeros positivos ingresados es: {suma_positivos}\n"


producto_numeros_negativos = True

for num in lista_numeros:
    if num < 0:
        if producto_numeros_negativos == True:
            producto_numeros_negativos = num
        else:
            producto_numeros_negativos *= num
            
if producto_numeros_negativos != True:        
    mensaje += f"El producto de los numeros negativos es: {producto_numeros_negativos}"
else:
    mensaje += f"No se registraron numeros negativos"
    
print(mensaje)

'''
Salamone Constanza

Ejercicio 8:
Dada la siguiente lista:
[82, 3, 49, 38, 94, 85, 95, 92, 64, 8, 75, 37, 97, 45, 12, 64, 48, 78, 29, 58]
mostrar el número repetido

'''

lista_numeros = [82, 3, 49, 38, 94, 85, 95, 92, 64, 8, 75, 37, 97, 45, 12, 64, 48, 78, 29, 58]

mensaje = ''

for i in range(len(lista_numeros)): 
    for x in range(i+1,len(lista_numeros)):
        if lista_numeros[i] == lista_numeros[x]:
            mensaje += f' {lista_numeros[i]}'

print(mensaje)

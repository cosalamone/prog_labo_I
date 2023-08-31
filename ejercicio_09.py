'''
Salamone Constanza

Ejercicio 9:
Dadas las siguientes listas:
edades = [25,36,18,23,45]
nombre = ["Juan","Ana","Sol","Mario","Sonia"]
y considerando que la posición en la lista corresponde a la misma persona,
mostar el nombre de la persona más joven

'''
edades = [25,36,18,23,45]
nombre = ["Juan","Ana","Sol","Mario","Sonia"]


menor_edad = None
for i in range(len(edades)):
    if menor_edad == None or menor_edad > edades[i]:
        menor_edad = edades[i]
        persona_mas_joven = nombre[i]

mensaje = f'La persona más joven es {persona_mas_joven}'
print(mensaje)
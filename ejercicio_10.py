'''
Salamone Constanza

Ejercicio 10:
Pedir al usuario que ingrese los datos de 5 alumnos y guardarlos en sus
respectivas listas. Validar el ingreso de datos según su criterio.
Datos:
nombre, sexo (f/m), nota (validar).
Una vez cargados los datos:
Mostrar el nombre del hombre con nota más baja
Mostrar el promedio de notas de las mujeres
Ejemplo:
nombres = ["Juan","Pedro","Sol","Paco","Ana"]
sexo = ["m","m","f","m","f"]
nota = [6,8,10,8,5]

'''

nombres = []
sexos = []
notas = []

mensaje = ''

for i in range(5):
    nombre = input('Ingrese el nombre del alumno/a ')
    while len(nombre) < 3:
        nombre = input('El nombre del alumno debe tener al menos 3 caracteres ')
    nombres.append(nombre)

    sexo = input('Ingrese el sexo del alumno/a ')
    while sexo != 'f' and sexo != 'm':
        sexo = input('Ingrese f o m ')
    sexos.append(sexo)


    nota = int(input('Ingrese la nota '))
    while nota < 1 or nota > 10:
        nota = int(input('Las notas van del 1 al 10 '))
    notas.append(nota)

# Mostrar el nombre del hombre con nota más baja
menor_nota = None
nombre_menor_nota = ''
for i in range(len(nombres)):
    if sexos[i] == 'm':
        if menor_nota == None or notas[i]< menor_nota:
            menor_nota = notas[i]
            nombre_menor_nota = nombres[i]
mensaje += f'La menor nota es de {nombre_menor_nota} \n'


# Mostrar el promedio de notas de las mujeres
contador = 0
acumulador = 0
for i in range(len(nombres)):
    if sexos[i] == 'f':
        contador += 1
        acumulador += notas[i]

promedio = acumulador/contador
mensaje = f'El promedio de las muejes es de {promedio}'

print(mensaje)



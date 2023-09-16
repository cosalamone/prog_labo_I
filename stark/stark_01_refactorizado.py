'''
Salamone Constanza


########################### Desafio Stark ###########################
Industrias Stark es principalmente una empresa de defensa que desarrolla y fabrica
armas avanzadas y tecnologías militares.

Recientemente ha decidido ampliar su departamento de IT y para acceder a las
entrevistas es necesario completar el siguiente desafío, el cual estará dividido en
etapas. Cada semana recibiremos un nuevo pedido de parte de la empresa.

La empresa compartió con todos los participantes cierta información confidencial
de un grupo de superhéroes. Y semana a semana enviará una lista con los nuevos
requerimientos. Quien supere todas las etapas accedera a una entrevista con el
director para de la compañía.
Set de datos
La información a ser analizada se encuentra en el archivo data_stark.py, por tratarse
de una lista, bastará con incluir dicho archivo en el proyecto de la siguiente manera:


Luego de analizar el set de datos correspondiente resolver el Desafío #01:

A. Recorrer la lista imprimiendo por consola todos los datos de cada superhéroe
B. Recorrer la lista y mostrar la identidad y el peso del superhéroe con mayor
fuerza (MÁXIMO)
C. Recorrer la lista y mostrar nombre e identidad del superhéroe más bajo
(MÍNIMO)
D. Recorrer la lista y determinar el peso promedio de los superhéroes
masculinos (PROMEDIO)
E. Recorrer la lista y mostrar nombre y peso de los superhéroes (cualquier
género) los cuales su fuerza supere a la fuerza promedio de todas las
superhéroes de género femenino

NOTA: Se debe construir un menú en el que se sea posible acceder a cada una de
las opciones (A-E)
'''

from data_stark import lista_personajes

mensaje_menu = '''Seleccione una de las siguientes opciones: 

A. Ver todos los datos de los superheroes
B. Ver la identidad y el peso del superhéroe con mayor fuerza
C. Ver el nombre e identidad del superhéroe más bajo
D. Ver el peso promedio de los superhéroes masculinos 
E. Ver nombre y peso de los superhéroes los cuales su fuerza supere a la fuerza promedio de todas las superhéroes de género femenino

------------------------------------------------------------------------------------------------------------------------------------
'''

# A. Recorrer la lista imprimiendo por consola todos los datos de cada superhéroe

def imprimir_lista_superheroes(lista):

    mensaje = ''
    for i in range(len(lista)): 
        nombre = lista[i]["nombre"]
        identidad = lista[i]["identidad"]
        empresa = lista[i]["empresa"]
        altura = lista[i]["altura"]
        peso = lista[i]["peso"]
        genero = lista[i]["genero"]
        color_ojos = lista[i]["color_ojos"]
        color_pelo = lista[i]["color_pelo"]
        fuerza = lista[i]["fuerza"]
        inteligencia = lista[i]["inteligencia"]
        
        mensaje += f'''DATOS:
* Nombre: {nombre} 
* Identidad: {identidad} 
* Tranajo: {empresa} 
* Altura: {altura} 
* Peso: {peso}
* Genero: {genero} 
* Color de pelo: {color_pelo} 
* Color de ojos: {color_ojos} 
* Fuerza {fuerza} 
* Inteligencia: {inteligencia}. 
------------------------------------
        '''
        
    return mensaje

def buscar_mayor_o_menor_caracteristica(lista:list, operador, caracteristica:str):
    mayor_o_menor_caracteristica = None
    for heroe in lista:
        if operador == 'mayor':
            if mayor_o_menor_caracteristica == None or mayor_o_menor_caracteristica > heroe[caracteristica]:
                pass
        
        if operador == 'menor':
            if mayor_o_menor_caracteristica == None or mayor_o_menor_caracteristica < heroe[caracteristica]:
                pass
# B. Recorrer la lista y mostrar la identidad y el peso del superhéroe con mayor fuerza (MÁXIMO)

def mostrar_identidad_y_peso_de_heroe_mayor_fuerza(lista):
    mayor_fuerza = 0
    identidad_con_mayor_fuerza = ''
    peso_con_mayor_fuerza = ''

    for i in range(len(lista)):
        identidad = lista[i]["identidad"]
        peso = lista[i]["peso"]
        fuerza = int(lista[i]["fuerza"])

        if fuerza > mayor_fuerza:
            mayor_fuerza = fuerza

    for i in range (len(lista)):
        identidad = lista[i]["identidad"]
        peso = lista[i]["peso"]
        fuerza = int(lista[i]["fuerza"])

        if mayor_fuerza == fuerza:
            identidad_con_mayor_fuerza += f"{identidad} "
            peso_con_mayor_fuerza += f"{peso} "

    mensaje = f'La identidad de quien tiene más fuerza es {identidad_con_mayor_fuerza} y su peso es {peso_con_mayor_fuerza} \n'

    return mensaje


# C. Recorrer la lista y mostrar nombre e identidad del superhéroe más bajo (MÍNIMO)

def mostrar_nombre_e_identidad_de_heroe_mas_bajo(lista):
    menor_altura = None
    identidad_menor_altura = ''
    nombre_menor_altura = ''
    for i in range(len(lista)):
        altura = lista[i]["altura"]

        if menor_altura == None or altura < menor_altura:
            menor_altura = altura

    for i in range(len(lista)):
        nombre = lista[i]["nombre"]
        identidad = lista[i]["identidad"]
        altura = lista[i]["altura"]

        if menor_altura == altura:
            nombre_menor_altura += nombre
            identidad_menor_altura += identidad
    
    mensaje = f'{nombre_menor_altura} es el superheroe con altura mas baja y su identidad es {identidad_menor_altura} '

    return mensaje


def calcular_promedio(acumulador, contador):
    promedio = acumulador/contador
    return promedio


# D. Recorrer la lista y determinar el peso promedio de los superhéroes masculinos (PROMEDIO)

def peso_promedio_de_sh_masculinos(lista):
    acumulador_peso_masculino = 0 
    contador = 0

    for i in range(len(lista)):
        peso = float(lista[i]["peso"])
        genero = lista[i]["genero"]



        if genero == 'M':
            acumulador_peso_masculino += peso
            contador += 1

    if contador != 0:
        promedio = calcular_promedio(acumulador_peso_masculino, contador)
        

    mensaje = f'El promedio de peso promedio de los superhéroes masculinos es {promedio}'

    return mensaje


# E. Recorrer la lista y mostrar nombre y peso de los superhéroes (cualquier
# género) los cuales su fuerza supere a la fuerza promedio de todas las
# superhéroes de género femenino

def mostrar_nombre_y_peso(lista):
    contador_femenino = 0
    acumulador_femenino = 0

    mensaje = ''
    for i in range(len(lista)): 
        genero = lista[i]["genero"]
        fuerza = int(lista[i]["fuerza"])

        if genero == 'F':
            contador_femenino += 1
            acumulador_femenino += fuerza

    if contador_femenino != 0: 
        promedio_femenino = acumulador_femenino/contador_femenino

    for i in range(len(lista)): 
        nombre = lista[i]["nombre"]
        peso = lista[i]["peso"]
        fuerza = int(lista[i]["fuerza"])

        if fuerza > promedio_femenino:
                mensaje += f" Nombre: {nombre} - Peso: {peso:} kg \n"
            
    mensaje_dos = f'El resultado es: \n{mensaje}'

    return mensaje_dos


####### MENU ########

while True:
    rta = input(f'{mensaje_menu}')
    
    match rta:
        case 'A':
            print(imprimir_lista_superheroes(lista_personajes))
        case 'B':
            print(mostrar_identidad_y_peso_de_heroe_mayor_fuerza(lista_personajes))
        case 'C':
            print(mostrar_nombre_e_identidad_de_heroe_mas_bajo(lista_personajes))
        case 'D':
            print(peso_promedio_de_sh_masculinos(lista_personajes))
        case 'E':
            print(mostrar_nombre_y_peso(lista_personajes))
        case _:
            break
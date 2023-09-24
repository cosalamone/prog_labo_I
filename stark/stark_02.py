'''
Desafio Stark
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

from data_stark import lista_personajes
Formato de los datos recibidos

Desafío #02:
Usando como base lo realizado en el anterior desafío realizar los siguientes
informes en un menú
A. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de
género NB
B. Recorrer la lista y determinar cuál es el superhéroe más alto de género F
C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M
D. Recorrer la lista y determinar cuál es el superhéroe más débil de género M
E. Recorrer la lista y determinar cuál es el superhéroe más débil de género NB
F. Recorrer la lista y determinar la fuerza promedio de los superhéroes de
género NB
G. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
H. Determinar cuántos superhéroes tienen cada tipo de color de pelo.
I. Listar todos los superhéroes agrupados por color de ojos.
J. Listar todos los superhéroes agrupados por tipo de inteligencia

NOTA: Se debe aplicar el tema Funciones visto en clase para cada opción del menú
'''

'''
Antes de programar un fx hay que respondernos:
* ¿Que hace?
* ¿Que recibe? 
* ¿Que retorna? 
'''

from data_stark import lista_personajes
from funciones import *

# A. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género NB

mostrar_nombre_segun_genero(lista_personajes, 'NB')

# B. Recorrer la lista y determinar cuál es el superhéroe más alto de género F

mostrar_heroe_mas_alto(lista_personajes, 'F')

# C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M

mostrar_heroe_mas_alto(lista_personajes, 'M')



# D. Recorrer la lista y determinar cuál es el superhéroe más débil de género M
def mostrar_sh_M_mas_debil(lista:list):
    sh_M = []
    menor_fuerza = None 
    sh_M_mas_debil  = ""
    
    for i in lista:
        nombre = i['nombre']
        genero = i['genero']

        if genero == 'M':
            sh_M.append(i)
    for i in sh_M:
        nombre = i['nombre']
        fuerza = int(i['fuerza'])
        genero = i['genero']

        if menor_fuerza == None or fuerza < menor_fuerza:
            menor_fuerza = fuerza

    for i in sh_M:
        nombre = i['nombre']
        fuerza = int(i['fuerza'])
        genero = i['genero']
        if fuerza == menor_fuerza:
            sh_M_mas_debil += nombre

    return sh_M_mas_debil

# print(mostrar_sh_M_mas_debil(lista_personajes))

# E. Recorrer la lista y determinar cuál es el superhéroe más débil de género NB

def mostrar_sh_NB_más_debil(lista:list):
    sh_NB = []
    menor_fuerza = None 
    sh_NB_mas_debil  = ""
    
    for i in lista:
        nombre = i['nombre']
        genero = i['genero']

        if genero == 'NB':
            sh_NB.append(i)
    for i in sh_NB:
        nombre = i['nombre']
        fuerza = int(i['fuerza'])
        genero = i['genero']

        if menor_fuerza == None or fuerza < menor_fuerza:
            menor_fuerza = fuerza
    for i in sh_NB:
        nombre = i['nombre']
        fuerza = int(i['fuerza'])
        genero = i['genero']
        if fuerza == menor_fuerza:
            sh_NB_mas_debil += nombre

    return sh_NB_mas_debil

# print(mostrar_sh_NB_más_debil(lista_personajes))

# F. Recorrer la lista y determinar la fuerza promedio de los superhéroes de género NB
def mostrar_fuerza_promedio_sh_NB(lista:list):
    contador = 0
    acumulador = 0 

    for i in lista:
        genero = i['genero']
        fuerza = int(i['fuerza'])

        if genero == 'NB':
            contador += 1
            acumulador += fuerza

    if contador != 0:
        promedio = acumulador/contador

    return promedio

# print(mostrar_fuerza_promedio_sh_NB(lista_personajes))

# G. Determinar cuántos superhéroes tienen cada tipo de color de ojos.

def mostrar_cantidad_sh_segun_tipo_color_ojos(lista:list):
    brown = 0
    green = 0
    blue = 0 
    yellow_without_irises = 0
    yellow =  0
    hazel = 0 
    silver = 0
    red = 0
    
    for i in lista:
        color_ojos = i['color_ojos']

        if color_ojos == 'Brown':
            brown += 1 
        else:
            if color_ojos == 'Green':
                green += 1
            else:
                if color_ojos == 'Blue':
                    blue += 1 
                else:
                    if color_ojos == 'Yellow (without irises)':
                        yellow_without_irises += 1 
                    else: 
                        if color_ojos == 'Hazel':
                            hazel += 1
                        else:
                            if color_ojos =='Yellow':
                                yellow += 1 
                            else:
                                if color_ojos == 'Silver':
                                    silver += 1 
                                else:
                                    if color_ojos =='Red':
                                        red += 1 
                            
    mensaje = f'''La cantidad de superheroes con cada tipo de color son:
Marron: {brown}
Verde: {green}
Azul: {blue}
Amarrillo sin iris: {yellow_without_irises}
Avellana: {hazel}
Amarillo: {yellow}
Plateado: {silver}
Rojo: {red}
'''
    return mensaje

# print(mostrar_cantidad_sh_segun_tipo_color_ojos(lista_personajes))

# H. Determinar cuántos superhéroes tienen cada tipo de color de pelo.
def mostrar_cantidad_sh_segun_tipo_color_pelo(lista:list):
    brown = 0
    green = 0
    red = 0
    yellow = 0
    black = 0
    auburn = 0
    red_orange = 0
    white = 0
    no_hair = 0
    blond = 0 
    brown_white = 0
    no_especified = 0 

    for i in lista:
        color_pelo = i['color_pelo']

        if color_pelo == 'Brown':
            brown += 1 
        else:
            if color_pelo == 'Green':
                green += 1
            else:
                if color_pelo == 'Black':
                    black += 1 
                else:            
                    if color_pelo =='Red':
                        red += 1 
                    else:
                        if color_pelo == 'Yellow':
                            yellow += 1 
                        else:
                            if color_pelo == 'Auburn':
                                auburn += 1
                            else:
                                if color_pelo == 'Red / Orange':
                                    red_orange += 1
                                else:
                                    if color_pelo == 'White':
                                        white += 1 
                                    else:
                                        if color_pelo == 'No Hair':
                                            no_hair += 1
                                        else:
                                            if color_pelo == 'Blond' or color_pelo == 'blond':
                                                blond += 1 
                                            else:
                                                if color_pelo == 'Brown / White':
                                                    brown_white += 1 
                                                else:
                                                    no_especified+= 1 

                            
    mensaje = f'''La cantidad de superheroes con cada tipo de color son:
Marron: {brown}
Verde: {green}
Rojo: {red}
Amarillo: {yellow}
Negro: {black}
Castaño: {auburn}
Rojo/Naranja: {red_orange}
Blanco: {white}
Sin pelo: {no_hair}
Rubio: {blond}
Marron/Blanco: {brown_white}
Sin especificar: {no_especified}
'''
    return mensaje

# print(mostrar_cantidad_sh_segun_tipo_color_pelo(lista_personajes))

# I. Listar todos los superhéroes agrupados por color de ojos.
def mostrar_sh_segun_color_ojos(lista:list):

    brown = ''
    green = ''
    blue = '' 
    yellow_without_irises = ''
    yellow =  ''
    hazel = '' 
    silver = ''
    red = ''

    for i in lista:
        color_ojos = i['color_ojos']
        nombre = i['nombre']

        if color_ojos == 'Brown':
            brown += f'{nombre} \n'
        else:
            if color_ojos == 'Green':
                green += f'{nombre} \n'
            else:
                if color_ojos == 'Blue':
                    blue += f'{nombre} \n'
                else:
                    if color_ojos == 'Yellow (without irises)':
                        yellow_without_irises += f'{nombre} \n'
                    else: 
                        if color_ojos == 'Hazel':
                            hazel += f'{nombre} \n'
                        else:
                            if color_ojos =='Yellow':
                                yellow += f'{nombre} \n'
                            else:
                                if color_ojos == 'Silver':
                                    silver += f'{nombre} \n'
                                else:
                                    if color_ojos =='Red':
                                        red += f'{nombre} \n'
    mensaje = f'''Los superhéroes agrupados por color de ojos son:
Marron: 
{brown}
-----------
Verde: 
{green}
-----------
Azul: 
{blue}
-----------
Amarrillo sin iris: 
{yellow_without_irises}
-----------
Avellana: 
{hazel}
-----------
Amarillo: 
{yellow}
-----------
Plateado: 
{silver}
-----------
Rojo: 
{red}
-----------
'''
        
    return mensaje

# print(mostrar_sh_segun_color_ojos(lista_personajes))
# J. Listar todos los superhéroes agrupados por tipo de inteligencia


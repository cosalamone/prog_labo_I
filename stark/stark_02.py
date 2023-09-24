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

mostrar_heroe_segun_caracteristica(lista_personajes, 'F', 'altura', 'mayor')

# C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M

mostrar_heroe_segun_caracteristica(lista_personajes, 'M', 'altura', 'mayor')

# D. Recorrer la lista y determinar cuál es el superhéroe más débil de género M
mostrar_heroe_segun_caracteristica(lista_personajes, 'M', 'fuerza', 'menor')

# E. Recorrer la lista y determinar cuál es el superhéroe más débil de género NB

mostrar_heroe_segun_caracteristica(lista_personajes, 'NB', 'fuerza', 'menor')

# F. Recorrer la lista y determinar la fuerza promedio de los superhéroes de género NB
imprimir_promedio(calcular_fuerza_promedio_segun_genero(lista_personajes, 'NB'))


# G. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
mostrar_cantidad_heroes_segun_caracteristica(lista_personajes,'color_ojos')

# H. Determinar cuántos superhéroes tienen cada tipo de color de pelo.
mostrar_cantidad_heroes_segun_caracteristica(lista_personajes, 'color_pelo')

# I. Listar todos los superhéroes agrupados por color de ojos.
mostrar_nombre_heroes_por_cada_característica(lista_personajes, 'color_ojos')

# J. Listar todos los superhéroes agrupados por tipo de inteligencia
mostrar_nombre_heroes_por_cada_característica(lista_personajes, 'inteligencia')



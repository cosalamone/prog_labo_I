

from data_stark import lista_personajes
from funciones_03 import *

def stark_marvel_app(lista:list):
    while True:
            
        respuesta = stark_menu_principal()
        match respuesta:
            case 1:
                stark_normalizar_datos(lista)
            case 2:
                print(menu_obtener_nombre_nb(lista, 'genero'))
            case 3:
                menu_por_genero_mas_alto(lista,'genero','altura', 'F' )
            case 4:
                menu_por_genero_mas_alto(lista,'genero','altura', 'M')
            case 5:
                menu_por_genero_min_fuerza(lista,'genero','fuerza', 'M')
            case 6:
                menu_por_genero_min_fuerza(lista,'genero','fuerza', 'NB')
            case 7:
                menu_promedio_por_genero(lista,'genero','fuerza', 'NB')
            case 8:
                menu_mostrar_cantidad_por_caracteristica(lista, 'color_ojos')
            case 9:
                menu_mostrar_cantidad_por_caracteristica(lista, 'color_pelo')
            case 10:
                mostrar_nombre_heroes_por_cada_característica(lista,'color_ojos')
            case 11:
                mostrar_nombre_heroes_por_cada_característica(lista,'inteligencia')
            case 12:
                if respuesta == False:
                    break

stark_marvel_app(lista_personajes)
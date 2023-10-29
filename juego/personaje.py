import pygame
from constantes import *

def crear(img_path: str, x:int ,y:int, ancho, alto):
    
    dict_groot = {}
    dict_groot['surface']  = pygame.image.load(img_path)
    dict_groot['surface']  = pygame.transform.scale( dict_groot['surface'] , (ancho,alto))
    dict_groot['rect_posicion'] =  pygame.Rect(x,y, 200,200)
    dict_groot['rect_colision'] =  pygame.Rect((x+ancho/2)-15,y+75,40,30)
    dict_groot['score'] = 0

    return dict_groot

def actualizar_pantalla(personaje, ventana_ppal):
    ventana_ppal.blit(personaje['surface'], personaje['rect_posicion'])
    pygame.draw.rect(ventana_ppal, COLOR_CELESTE, personaje['rect_colision'])

def update(personaje, incremento_x):
    nueva_posicion = personaje['rect_posicion'].x + incremento_x
    if nueva_posicion > 10 and nueva_posicion < 750:
        personaje['rect_posicion'].x = personaje['rect_posicion'].x + incremento_x
        personaje['rect_colision'].x = personaje['rect_colision'].x + incremento_x
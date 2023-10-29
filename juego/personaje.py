import pygame
from constantes import *

def crear(img_path: str, x:int ,y:int, ancho, alto):
    
    dict_groot = {}
    dict_groot['surface']  = pygame.image.load(img_path)
    dict_groot['surface']  = pygame.transform.scale( dict_groot['surface'] , (ancho,alto))
    dict_groot['rect_posicion'] =  pygame.Rect(x,y, 200,200)
    dict_groot['rect_colision'] =  pygame.Rect(x+ancho/3,y+70,40,40)

    return dict_groot

def actualizar_pantalla(personaje, ventana_ppal):
    ventana_ppal.blit(personaje['surface'], personaje['rect_posicion'])
    pygame.draw.rect(ventana_ppal, COLOR_CELESTE, personaje['rect_colision'])
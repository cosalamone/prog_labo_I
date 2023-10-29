import pygame
from constantes import *

def crear(img_path: str, x:int ,y:int):
    imagen_planta = pygame.image.load(img_path)
    imagen_planta = pygame.transform.scale(imagen_planta, (50,40))

    rect_planta = imagen_planta.get_rect()

    rect_planta.x = x
    rect_planta.y = y

    dict_planta = {}
    dict_planta['surface'] = imagen_planta
    dict_planta['rect'] = rect_planta

    return dict_planta


def actualizar_pantalla(lista_plantas, ventana_ppal):
    for planta in lista_plantas:
        pygame.draw.rect(ventana_ppal, COLOR_CELESTE, planta['rect'])
        ventana_ppal.blit(planta['surface'], planta['rect'])



def crear_lista_plantas(cantidad):
    lista_plantas = []
    for i in range(cantidad):
        lista_plantas.append(crear('juego/assets/planta_uno.png', 0+(i * 110), 0))

    return lista_plantas

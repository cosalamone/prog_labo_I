import pygame
from constantes import *

def crear(img_path: str, x:int ,y:int, ancho:int, alto:int):
    imagen_planta = pygame.image.load(img_path)
    imagen_planta = pygame.transform.scale(imagen_planta, (alto,ancho))

    rect_planta = imagen_planta.get_rect()

    rect_planta.x = x
    rect_planta.y = y

    dict_planta = {}
    dict_planta['surface'] = imagen_planta
    dict_planta['rect'] = rect_planta
    dict_planta['visible'] = True


    return dict_planta

def update(lista_plantas):
    for planta in lista_plantas:
        rect_planta = planta['rect']
        rect_planta.y = rect_planta.y + 2 #cantidad de px que van bajando 


def actualizar_pantalla(lista_plantas, personaje, ventana_ppal):
    for planta in lista_plantas:
        if planta['visible'] and personaje['rect_colision'].colliderect(planta['rect']):
            planta['visible'] = False
            personaje['score'] = personaje['score']+ 10

        # cuantas pasadas va por el while
        #base de tiempoque llama una fx que actualiza las plantas 
        if planta['visible']: 
            pygame.draw.rect(ventana_ppal, COLOR_CELESTE, planta['rect'])
            ventana_ppal.blit(planta['surface'], planta['rect'])
        
    font = pygame.font.SysFont('Arial', 50)
    text = font.render('SCORE: {0}'.format(personaje['score']), True, (255,0,0))
    ventana_ppal.blit(text, (50,50))
def crear_lista_plantas(cantidad):
    lista_plantas = []
    for i in range(cantidad):
        lista_plantas.append(crear('juego/assets/planta_uno.png', 0+(i * 110),0,40,50))

    return lista_plantas



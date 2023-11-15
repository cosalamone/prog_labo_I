import pygame
import sys
from constantes import *
from player import Player
from enemigo import Enemigo


pygame.init()
screen = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption('Save the plant!')
clock = pygame.time.Clock() #controla la cantidad de frames x segundo

#Fondo
img_background = pygame.image.load('assets/background/Forest of Illusion Files/Previews/Previewx3.png')
# img_background = pygame.transform.scale(img_background,(ANCHO_VENTANA, ALTO_VENTANA))

#Jugador
player = Player(0,0,10,20)

#Enemigo
enemigo = Enemigo(550,550,'assets/enemigos/Animations/Blazing Slug/BlazingSlugIdleSide.png',4,1)

#Plataforma
plataforma = pygame.image.load('assets\plataforma\plataform (1).png')
plataforma = pygame.transform.scale(plataforma, (250,40))
flag_playing = True

while flag_playing:
    lista_events = pygame.event.get()
    for event in lista_events:
        if event.type == pygame.QUIT:
            flag_playing = False
            pygame.quit()
            sys.exit() # cierra la app

    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_UP] and player.jumping == False:
        player.action = 'jump'
    
    elif teclas[pygame.K_RIGHT]:
        player.action='walk_right'
    
    elif teclas[pygame.K_LEFT]:
        player.action='walk_left'
    
    else:
        player.action='stand_up'

    screen.blit(img_background,img_background.get_rect())
    screen.blit(plataforma,plataforma.get_rect())
    # screen.blit(enemigo,enemigo.get_rect())
    player.update(screen)
    enemigo.update(screen)

    # player update -> verifica como el py interactua c/ nivel
    # enemigo update
    # player dibujar
    # dibujar nivel


    pygame.display.flip()
    # print(clock.tick(FPS))
    delta_ms = clock.tick(FPS) # limita la cantidad de veces x seg que se genera el while

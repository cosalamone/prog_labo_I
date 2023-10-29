import pygame
import personaje 
import planta
from constantes import *
pygame.init()

#pantalla del juego
ventana_ppal = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))

# setear el titulo
pygame.display.set_caption('Pygame Groot')


# TIMER - Independiente a lo que haga el ususario
timer_milesimas = pygame.USEREVENT  + 0
pygame.time.set_timer(timer_milesimas, 15)


# LEER IMAGEN
imagen_fondo_uno = pygame.image.load('juego/assets/fondo_uno.jpg')
imagen_fondo_uno = pygame.transform.scale(imagen_fondo_uno, (ANCHO_VENTANA, ALTO_VENTANA))

groot = personaje.crear('juego/assets/groot_sin_fondo_2.png',100,550,100, 157)
lista_plantas = planta.crear_lista_plantas(10)


flag_running = True
while flag_running:
    #detectar que el usuario cierra la ventana
    lista_eventos = pygame.event.get() #obtiene los eventos

    # for que analiza los eventos
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            flag_running = False # deja de correr el juego

        if evento.type == pygame.USEREVENT:
            if evento.type == timer_milesimas:
                planta.update(lista_plantas)
                    # llamo a fx que recorre donas y las hace caer

        if evento.type == pygame.MOUSEBUTTONDOWN:
                    print(evento.pos) #posicion del mousedown en forma de tupla x,y
                    pos_circulo = list(evento.pos)

        # if evento.type == pygame.USEREVENT:
        #     if evento.type == timer_500_milesimas:
        #         if (pos_circulo[0] < ANCHO_VENTANA + 80):
        #             pos_circulo[0] = pos_circulo[0] + 10
        #         else:
        #             pos_circulo[0] = -80



    # lista que devuelve todas las teclas presionadas
    lista_teclas = pygame.key.get_pressed()
    if lista_teclas[pygame.K_LEFT]:
        pos_circulo[1] = pos_circulo[1] + 1


    ventana_ppal.fill(COLOR_NEGRO)
    ventana_ppal.blit(imagen_fondo_uno,(0,0)) #fundimos/pegamos la imagen en la suf de la pantalla

    personaje.actualizar_pantalla(groot, ventana_ppal)
    planta.actualizar_pantalla(lista_plantas, ventana_ppal)


    pygame.display.flip() # Se las muestra al usuario


pygame.quit() # cierra de manera prolija el programa

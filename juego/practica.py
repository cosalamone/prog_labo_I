import pygame
from constantes import *
pygame.init()

#pantalla del juego
ventana_ppal = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))

# setear el titulo
pygame.display.set_caption('Pygame Connie')
print(type(ventana_ppal)) # type: <class 'pygame.surface.Surface'>


flag_running = True
pos_circulo = [30,60]

# TIMER - Independiente a lo que haga el ususario
timer_segundo = pygame.USEREVENT
pygame.time.set_timer(timer_segundo, 100)




# LEER IMAGEN
imagen_groot = pygame.image.load('juego/groot_sin_fondo_2.png')
imagen_planta_uno = pygame.image.load('juego/planta_uno.png')
groot_rect = imagen_groot.get_rect()
rect_planta_uno = imagen_planta_uno.get_rect()
groot_rect.x = 100
groot_rect.y = 100
rect_planta_uno.x = 350
rect_planta_uno.y = 350


# CREAR TEXTO
fuente = pygame.font.SysFont('Arial', 30)
texto = fuente.render('Hola Groot', True, COLOR_GRIS)

while flag_running:
    #detectar que el usuario cierra la ventana
    lista_eventos = pygame.event.get() #obtiene los eventos

    # for que analiza los eventos
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            flag_running = False # deja de correr el juego

        if evento.type == pygame.MOUSEBUTTONDOWN:
            print(evento.pos) #posicion del mousedown en forma de tupla x,y
            pos_circulo = list(evento.pos)

        
        if evento.type == pygame.USEREVENT:
            if evento.type == timer_segundo:
                if (pos_circulo[0] < ANCHO_VENTANA + 80):
                    pos_circulo[0] = pos_circulo[0] + 10
                else:
                    pos_circulo[0] = -80


        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_RIGHT:
                pos_circulo[1] = pos_circulo[1] + 10

    # lista que devuelve todas las teclas presionadas
    lista_teclas = pygame.key.get_pressed()
    if lista_teclas[pygame.K_LEFT]:
        pos_circulo[1] = pos_circulo[1] + 1


    ventana_ppal.fill(COLOR_GRIS_CLARO)
    pygame.draw.rect(ventana_ppal, COLOR_NEGRO, (30,60,100,200))
    pygame.draw.circle(ventana_ppal, COLOR_AMARILLO, pos_circulo, 80)


    pygame.draw.rect(ventana_ppal, COLOR_CELESTE, groot_rect)
    ventana_ppal.blit(imagen_groot, groot_rect)

    pygame.draw.rect(ventana_ppal, COLOR_CELESTE, rect_planta_uno)
    ventana_ppal.blit(imagen_planta_uno, rect_planta_uno)


    pygame.display.flip() # Se las muestra al usuario


pygame.quit() # cierra de manera prolija el programa

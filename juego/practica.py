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
imagen_fondo = pygame.image.load('juego/fondo_espacial_con_plantas.jpg')
imagen_plantas = pygame.image.load('juego/plantas.jpg')
imagen_plantas =  pygame.transform.scale(imagen_plantas, (70,50))


# CREAR TEXTO
fuente = pygame.font.SysFont('Arial', 30)
texto = fuente.render('Hola homero', True, COLOR_GRIS)

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
    ventana_ppal.blit(imagen_plantas, (50,50,100,100))
    ventana_ppal.blit(texto, (300,300))


    pygame.display.flip() # Se las muestra al usuario


pygame.quit() # cierra de manera prolija el programa

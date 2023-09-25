import pygame
from data_stark import *
from constantes import *

heroe = ''
posicion = 0 
lista_heroes = []
for heroe in lista_personajes:
    lista_heroes.append(heroe['nombre'])

#print(lista_heroes)

pygame.init()

#Pantalla
pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA)) #Tamaño de la pantalla
pygame.display.set_caption('PyGame') #Titulo

#Imagen
imagen = pygame.image.load("preguntados/foto.jpg") #Poner ruta completa
imagen = pygame.transform.scale(imagen,(100,100))

#Texto
fuente = pygame.font.SysFont('Arial', 30)
texto_heroe = fuente.render(str(heroe), True, COLOR_GRIS)

flag_correr = True
while flag_correr:

    lista_eventos= pygame.event.get()

    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            flag_correr = False #Para cortar el programa cuando el ususario toca la cruz

        if evento.type == pygame.MOUSEBUTTONDOWN:
            posicion_click= list(evento.pos) #trae tupla no puede modificarse por eso lo pasamos a lista
            # print(posicion_click)
                        #ancho del boton                        and     alto del boton
            if(posicion_click[0]>300 and posicion_click[0]< 500) and (posicion_click[1]>20 and posicion_click[1] <120):
                heroe= lista_heroes[posicion]
                texto_heroe = fuente.render(str(heroe), True, COLOR_GRIS)
                if posicion > len(lista_heroes):
                    posicion =  0
                else: 
                    posicion = posicion + 1

    pantalla.fill(COLOR_LILA)
    pygame.draw.rect(pantalla, COLOR_BLANCO,(300,20,200,100)) # left top, ancho y alto
    pantalla.blit(imagen,(POSICION_IMAGEN),) #fundimos/pegamos la imagen en la suf de la pantalla
    pantalla.blit(texto_heroe, (150,170))
    pygame.display.flip() #Actualizacion de pantalla


pygame.quit()

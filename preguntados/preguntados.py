'''
Desafío:
A. Analizar detenidamente el set de datos.
B. Recorrer la lista guardando en sub-listas: la pregunta, cada opción y la respuesta
correcta.
C. Crear 2 botones (rectángulos) uno con la etiqueta “Pregunta”, otro con la etiqueta
“Reiniciar”
D. Imprimir el Score: 999 donde se va a ir acumulando el puntaje de las respuestas
correctas. 
### Cada respuesta correcta suma 10 puntos.
E. Al hacer clic en el botón (rectángulo) “Pregunta” debe mostrar las preguntas
comenzando por la primera y las tres opciones, cada clic en este botón pasa a la
siguiente pregunta.
F. Al hacer clic en una de las tres palabras que representa una de las tres opciones, si es
correcta, debe sumar el score y dejar de mostrar las opciones.
G. Solo tiene 2 opciones para acertar la respuesta correcta y sumar puntos, si agotó ambas
opciones, deja de mostrar las opciones y no suma score
H. Al hacer clic en el botón (rectángulo) “Reiniciar” debe mostrar las preguntas
comenzando por la primera y las tres opciones, cada clic pasa a la siguiente pregunta.
También debe reiniciar el Score.
'''




import pygame
from datos import lista

from constantes import *

titulo = "Pregunta"
reiniciar = 'Reiniciar'
puntos = 'Puntos: '
valor_puntaje = 000
pregunta = ''
posicion = 0 
listado_preguntas = []
opciones_a = []
opciones_b = []
opciones_c = []
rtas_correctas = []

#B. Recorrer la lista guardando en sub-listas: la pregunta, cada opción y la respuesta correcta.
for elemento in lista:
    listado_preguntas.append(elemento['pregunta'])
    opciones_a.append(elemento['a'])
    opciones_b.append(elemento['b'])
    opciones_c.append(elemento['c'])
    rtas_correctas.append(elemento['correcta'])

# print('preg', listado_preguntas)
# print('a ',opciones_a)
# print('b', opciones_b)
# print('c', opciones_c)
# print('ctas', rtas_correctas)


pygame.init()

#Pantalla
pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA)) #Tamaño de la pantalla
pygame.display.set_caption('PyGame') #Titulo

#Imagen
imagen = pygame.image.load("preguntados/foto.jpg") #Poner ruta completa
imagen = pygame.transform.scale(imagen,(100,100))

#Texto
fuente = pygame.font.SysFont('Arial', 30)
texto_titulo = fuente.render(str(titulo), True, COLOR_NEGRO)
texto_puntaje = fuente.render(str(puntos), True, COLOR_NEGRO)
texto_valor = fuente.render(str(valor_puntaje), True, COLOR_NEGRO)
texto_pregunta = fuente.render(str(pregunta), True, COLOR_GRIS)
texto_reiniciar = fuente.render(str(reiniciar), True, COLOR_GRIS)


flag_correr = True
while flag_correr: # todo lo que pasa durante el juego - las interacciones 

    lista_eventos= pygame.event.get()

    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            flag_correr = False #Para cortar el programa cuando el ususario toca la cruz

        if evento.type == pygame.MOUSEBUTTONDOWN:
            posicion_click= list(evento.pos) #trae tupla no puede modificarse por eso lo pasamos a lista
            print(posicion_click)
                        #ancho del boton                        and     alto del boton
            if(posicion_click[0]>300 and posicion_click[0]< 500) and (posicion_click[1]>20 and posicion_click[1] <120):
                pregunta= listado_preguntas[posicion]
                texto_pregunta = fuente.render(str(pregunta), True, COLOR_GRIS)
                if posicion > len(listado_preguntas): ## ver 
                    posicion =  0
                else: 
                    posicion = posicion + 1

    pantalla.fill(COLOR_LILA)
    pygame.draw.rect(pantalla, COLOR_BLANCO,(300,20,200,80)) # left top, ancho y alto
    pantalla.blit(imagen,(POSICION_IMAGEN),) #fundimos/pegamos la imagen en la suf de la pantalla
    pantalla.blit(texto_pregunta, (150,170))
    pantalla.blit(texto_titulo, (330,45))
    pantalla.blit(texto_puntaje, (330,115))
    pantalla.blit(texto_valor, (450,115))
    pygame.draw.rect(pantalla, COLOR_BLANCO,(300,500,200,80))
    pantalla.blit(texto_reiniciar, (340,525))


    pygame.display.flip() #Actualizacion de pantalla


pygame.quit()

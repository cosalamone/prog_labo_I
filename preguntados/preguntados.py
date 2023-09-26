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
opciones, deja de mostrar las opciones y no suma score.
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

for elemento in lista:
    listado_preguntas.append(elemento['pregunta'])
    opciones_a.append(elemento['a'])
    opciones_b.append(elemento['b'])
    opciones_c.append(elemento['c'])
    rtas_correctas.append(elemento['correcta'])


pygame.init()

#Pantalla
pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA)) #Tamaño de la pantalla
pygame.display.set_caption('PyGame') #Titulo

#Imagen
imagen = pygame.image.load("preguntados/foto.jpg") #Ruta completa de la carpeta hasta la img
imagen = pygame.transform.scale(imagen,(100,100))

#Texto
fuente = pygame.font.SysFont('Arial', 30)
texto_titulo = fuente.render(str(titulo), True, COLOR_NEGRO)
texto_puntaje = fuente.render(str(puntos), True, COLOR_NEGRO)
texto_valor = fuente.render(str(valor_puntaje), True, COLOR_NEGRO)
texto_pregunta = fuente.render(str(pregunta), True, COLOR_GRIS)
texto_a = fuente.render('', True, COLOR_GRIS)
texto_b = fuente.render('', True, COLOR_GRIS)
texto_c = fuente.render('', True, COLOR_GRIS)
texto_reiniciar = fuente.render(str(reiniciar), True, COLOR_GRIS)

inicio = False ## bandera que cambia que una vez que la persona esta jugando, 
                ## y arranca cuando hace click en pregunta --> a partir de ahi que empieca a sumar puntos
flag_correr = True
unica_vez = True


while flag_correr: # todo lo que pasa durante el juego - las interacciones

    lista_eventos= pygame.event.get()

    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            flag_correr = False #Para cortar el programa cuando el ususario toca la cruz

        if evento.type == pygame.MOUSEBUTTONDOWN:
            posicion_click= list(evento.pos) #trae tupla no puede modificarse por eso lo pasamos a lista
            boton_pregunta = (posicion_click[0]>300 and posicion_click[0]< 500) and (posicion_click[1]>20 and posicion_click[1] <120) 
            boton_reiniciar = (posicion_click[0]>300 and posicion_click[0] < 500) and (posicion_click[1] > 500 and posicion_click[1] < 580)

            print(posicion_click)
            print(posicion)

            if boton_reiniciar:
                print('Reiniciar')
                inicio = True
                unica_vez = True
                contador_intentos = 0

                posicion =  0
                valor_puntaje = 0
                texto_valor = fuente.render(str(valor_puntaje), True, COLOR_NEGRO)

            # BOTON PREGUNTA 
            if boton_pregunta or boton_reiniciar:
                inicio = True
                unica_vez = True
                contador_intentos = 0
                print('pos ', posicion)

                pregunta= listado_preguntas[posicion]
                a = opciones_a[posicion]
                b = opciones_b[posicion]
                c = opciones_c[posicion]
                correcta = rtas_correctas[posicion]
                texto_pregunta = fuente.render(str(pregunta), True, COLOR_GRIS)
                texto_a = fuente.render(str(a), True, COLOR_GRIS)
                texto_b = fuente.render(str(b), True, COLOR_GRIS)
                texto_c = fuente.render(str(c), True, COLOR_GRIS)
                texto_valor = fuente.render(str(valor_puntaje), True, COLOR_NEGRO)

                if posicion < len(listado_preguntas): 
                    posicion += 1
                
                        
            if inicio == True:
                # Boton A
                if(posicion_click[0] > 70 and posicion_click[0] < 270) and (posicion_click[1] > 230 and posicion_click[1] < 310):
                    a = opciones_a[posicion-1]
                    correcta = rtas_correctas[posicion - 1]
                    if 'a' == correcta and unica_vez == True:
                        valor_puntaje = valor_puntaje + 10
                        unica_vez = False
                        texto_pregunta = fuente.render('', True, COLOR_GRIS)
                        texto_a = fuente.render('', True, COLOR_GRIS)
                        texto_b = fuente.render('', True, COLOR_GRIS)
                        texto_c = fuente.render('', True, COLOR_GRIS)
                        texto_valor = fuente.render(str(valor_puntaje), True, COLOR_NEGRO)

                        print('A correcta', valor_puntaje)
                    if contador_intentos < 2: 
                        contador_intentos += 1

                # Boton B
                if(posicion_click[0]>300 and posicion_click[0] < 500) and (posicion_click[1] > 230 and posicion_click[1] < 310):
                    print(posicion)

                    correcta = rtas_correctas[posicion -1]
                    if 'b' == correcta and unica_vez == True:
                        valor_puntaje = valor_puntaje + 10
                        unica_vez = False
                        texto_pregunta = fuente.render('', True, COLOR_GRIS)
                        texto_a = fuente.render('', True, COLOR_GRIS)
                        texto_b = fuente.render('', True, COLOR_GRIS)
                        texto_c = fuente.render('', True, COLOR_GRIS)
                        texto_valor = fuente.render(str(valor_puntaje), True, COLOR_NEGRO)

                        print('b correcta', valor_puntaje)
                    if contador_intentos < 2: 
                        contador_intentos += 1

                # Boton C
                if(posicion_click[0]>500 and posicion_click[0] < 700) and (posicion_click[1] > 230 and posicion_click[1] < 310):
                    print(posicion)
                    correcta = rtas_correctas[posicion-1]
                    if 'c' == correcta and unica_vez == True:
                        valor_puntaje = valor_puntaje + 10
                        unica_vez = False
                        texto_pregunta = fuente.render('', True, COLOR_GRIS)
                        texto_a = fuente.render('', True, COLOR_GRIS)
                        texto_b = fuente.render('', True, COLOR_GRIS)
                        texto_c = fuente.render('', True, COLOR_GRIS)
                        texto_valor = fuente.render(str(valor_puntaje), True, COLOR_NEGRO)

                        print('c correcta', valor_puntaje)
                    if contador_intentos < 2: 
                        contador_intentos += 1

                #Cantidad intentos = 2, borra pregunta y opciones
                if contador_intentos == 2:
                    unica_vez = False
                    texto_pregunta = fuente.render('', True, COLOR_GRIS)
                    texto_a = fuente.render('', True, COLOR_GRIS)
                    texto_b = fuente.render('', True, COLOR_GRIS)
                    texto_c = fuente.render('', True, COLOR_GRIS)
                print('cdor intentos', contador_intentos)

                
            if (posicion) == len(listado_preguntas): 
                posicion =  0
                valor_puntaje = 0


            
    pantalla.fill(COLOR_LILA)
    pygame.draw.rect(pantalla, COLOR_BLANCO,(300,20,200,80)) # left top, ancho y alto
    pantalla.blit(imagen,(POSICION_IMAGEN),) #fundimos/pegamos la imagen en la suf de la pantalla
    pantalla.blit(texto_pregunta, (100,170))
    #A
    pygame.draw.rect(pantalla, COLOR_BLANCO,(70, 230,200,80))
    pantalla.blit(texto_a, (100,250))
    #B
    pygame.draw.rect(pantalla, COLOR_BLANCO,(300, 230,200,80))
    pantalla.blit(texto_b, (320,250))
    #C
    pygame.draw.rect(pantalla, COLOR_BLANCO,(550,230,200,80))
    pantalla.blit(texto_c, (560,250,))

    pantalla.blit(texto_titulo, (330,45))

    #Puntaje
    pantalla.blit(texto_puntaje, (330,115))
    pantalla.blit(texto_valor, (450,115))

    #Reiniciar
    pygame.draw.rect(pantalla, COLOR_BLANCO,(300,500,200,80))
    pantalla.blit(texto_reiniciar, (340,525))


    pygame.display.flip() #Actualizacion de pantalla


pygame.quit()

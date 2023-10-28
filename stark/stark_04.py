from data_stark import lista_personajes
from funciones_04 import *
import re

# 1.1
# Rocket Raccoon -> R.R.
def extraer_iniciales(nombre_heroe: str):
    '''
Brief:
    Extrae del parametro recibido las iniciales del nombre, las convierte en mayusculas, y luego de cada inicial agrega un '.'
    De tener el nombre el articulo 'the', lo elimina. En caso que tenga un guion '-', lo reemplaza por un espacio en blanco ' '.
    Si el parametro recibido esta vacio regregará un 'N/A'
Parametros:
    nombre_heroe: str
Retorno:
    Devuelve las iniciales del nombre seguidas cada una de un '.' Ej: parametro 'the rocket raccon' -> R.R.
    En caso que el parametro se aun string vacio retornará 'N/A'

    '''

    if not nombre_heroe:
        return 'N/A'
    nombre = re.sub('-', ' ', nombre_heroe)
    # print(nombre)

    nombre = re.sub('the', '', nombre)
    # print(nombre)

    filtrado = re.findall('[a-zA-Z]+', nombre)
    # print('filtrado', filtrado)

    iniciales = ''.join([inicial[0].upper() + '.' for inicial in filtrado])

    return iniciales

nombre_1 = 'the stark  - start'


# print(extraer_iniciales(nombre_1))


#1.2 
def obtener_dato_formato(dato:str):
    '''
Brief:
    Recibe un dato por parametro, lo pasa a minuscula y tranforma en formato snake_case.
    Valida que el dato recibido sea en str. De no serlo u ocurrir un error retorna Falso

Parametros:
    

Retorno:
    El dato en formato snake_case y en minuscula
    Falso en caso de ocurrir algun error
    '''
    
    if type(dato) != str:
        respuesta = False
    else:
        dato = dato.lower()

        dato = re.sub(' ', '_', dato)
        dato = re.sub('-', '_', dato)

        respuesta = dato

    return respuesta 

dato1 = 'Spider-Man a 2'
# print(obtener_dato_formato(dato1))

#1.3
'''
Crear la función ‘stark_imprimir_nombre_con_iniciales’ la cual recibirá
como parámetro:
● nombre_heroe: diccionario
Se deberá validar:
● Que el dato recibido sea del tipo diccionario
● Que el diccionario contengan la clave ‘nombre’
La función deberá imprimir el dato en cuestión con el siguiente formato
Delante de cada nombre se deberá agregar un asterisco ‘*’ (de forma de
viñeta) seguido de un espacio.
Si el superhéroe es Howard the Duck se deberá mostrar
* howard_the_duck (H.W.)
La función deberá devolver True en caso de haber finalizado con éxito o False
en caso de que haya ocurrido un error
'''
def stark_imprimir_nombre_con_iniciales(heroe: dict):
    '''
Brief:
    Imprime el nombre de un heroe en formato snake_case. Iniciando con un asterisco '*', luego de un espacio le sigue el nombre, con un espacio al final. Por último, entre parentesis se encuentan  las iniciales en mayusculas, cada una seguida de un punto '.'.
Parametros:
    heroe: diccionario
Retorno:
    Imprime el nombre en le formato indicado

    '''
    
    if type(heroe) != dict:
        boleano = False
    else:
        for clave in heroe:
            if clave == 'nombre':
                nombre_heroe = heroe[clave]

                iniciales = extraer_iniciales(nombre_heroe)
                nombre_en_snake = obtener_dato_formato(nombre_heroe)

                respuesta = f'* {nombre_en_snake} ({iniciales})'
                boleano = True
                print(respuesta) 

                break
            else:
                boleano = False
    return boleano

heroe_prueba = {
    "nombre": "Spider-Man",
    "identidad": "Peter Parker",
    "empresa": "Marvel Comics",
    "altura": "178.28",
    "peso": "74.25",
    "genero": "M",
    "color_ojos": "Hazel",
    "color_pelo": "Brown",
    "fuerza": "55",
    "inteligencia": "high"
    }
# stark_imprimir_nombre_con_iniciales(dic)

# 1.4
def stark_imprimir_nombres_con_iniciales(lista_heroes: list): 
    '''
Brief:
    
Parametros:
    lista_heroe: lista
Retorno:
    
    '''

    if type(lista_heroes) == list and len(lista_heroes) > 0:
        for heroe in lista_heroes:
            stark_imprimir_nombre_con_iniciales(heroe)
            boleano = True
    else:
        boleano = False
    return boleano

# stark_imprimir_nombres_con_iniciales(lista_personajes)



#2.1
def generar_codigo_heroe(heroe: dict, id: int):
    '''
Brief:
    
Parametros:
    diccionario de un héroe
    id (int)
Retorno:
    
    '''
    respuesta = ''
    cadena_numero = str(id)
    cantidad_caracteres_id = len(cadena_numero) #10 : 2


    if heroe['genero'] == 'F'or heroe['genero'] == 'M'or heroe['genero'] == 'NB':
        match heroe['genero']:
            case 'F':
                codigo = 'F-2'
                cantidad_caracteres_genero = 3
                cantidad_ceros = 10 - cantidad_caracteres_genero - cantidad_caracteres_id

                lista_ceros = []

                for i in range(cantidad_ceros):
                    lista_ceros.append('0')

                str_ceros = ''.join(map(str, lista_ceros))

                respuesta = f'{codigo}{str_ceros}{id}'


            case 'M':
                codigo = 'M-1'
                cantidad_caracteres_genero = 3
                cantidad_ceros = 10 - cantidad_caracteres_genero - cantidad_caracteres_id

                lista_ceros = []

                for i in range(cantidad_ceros):
                    lista_ceros.append('0')

                str_ceros = ''.join(map(str, lista_ceros))

            

                respuesta = f'{codigo}{str_ceros}{id}'
            case 'NB':
                codigo = 'NB-0'
                cantidad_caracteres_genero = 4
                cantidad_ceros = 10 - cantidad_caracteres_genero - cantidad_caracteres_id

                lista_ceros = []

                for i in range(cantidad_ceros):
                    lista_ceros.append('0')

                str_ceros = ''.join(map(str, lista_ceros))

            

                respuesta = f'{codigo}{str_ceros}{id}'
    else:
        respuesta = 'N/A'
    return respuesta
        

# print(generar_codigo_heroe(heroe_prueba, 150))

#2.2
def stark_generar_codigos_heroes(lista_heroes: list): 
    id = 0
    for heroe in lista_heroes: 
        id += 1 

        codigo = generar_codigo_heroe(heroe, id)

        iniciales = extraer_iniciales(heroe)
        nombre_en_snake = obtener_dato_formato(heroe)

        respuesta = f'{nombre_en_snake} {iniciales} | {codigo}'  



'''
Brief:
    
Parametros:
    heroe: diccionario
Retorno:
    
'''

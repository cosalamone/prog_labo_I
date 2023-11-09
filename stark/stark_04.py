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
    '''
Brief:

Parametros:
    heroe: diccionario
Retorno:

'''
    if len(lista_heroes) > 0:

        id = 0
        respuesta = ''
        for heroe in lista_heroes:
            if type(heroe) == dict:
                id += 1

                codigo = generar_codigo_heroe(heroe, id)
                iniciales = extraer_iniciales(heroe['nombre'])
                nombre_en_snake = obtener_dato_formato(heroe['nombre'])

                respuesta += f'* {nombre_en_snake} {iniciales} | {codigo} \n'

            else:
                respuesta = False
    else:
        respuesta = False

    if respuesta != False:
        respuesta += f'''...........
Se asignaron  {id} códigos
        '''
    return respuesta


# lista_personajes = [
#     {
#     "nombre": "Howard the Duck",
#     "identidad": "Howard (Last name unrevealed)",
#     "empresa": "Marvel Comics",
#     "altura": "79.349999999999994",
#     "peso": "18.449999999999999",
#     "genero": "M",
#     "color_ojos": "Brown",
#     "color_pelo": "Yellow",
#     "fuerza": "2",
#     "inteligencia": ""
# },
# {
#     "nombre": "Rocket Raccoon",
#     "identidad": "Rocket Raccoon!",
#     "empresa": "Marvel Comics",
#     "altura": "122.77",
#     "peso": "25.73",
#     "genero": "NB",
#     "color_ojos": "Brown",
#     "color_pelo": "Brown",
#     "fuerza": "5",
#     "inteligencia": "average"
# },
#     [1,2,3]
# ]
# print(stark_generar_codigos_heroes(lista_personajes))


# 3.1

def sanitizar_entero(numero_str:str):
    numero_str = numero_str.strip() # ' 123 '
    numero_str_aux = numero_str  # '-123'
    respuesta = None
    try:
        if numero_str[0] == '-':
            numero_str_aux = numero_str[1:]

        if not numero_str_aux.isdigit():
            respuesta = -1

        if respuesta == None:
            if int(numero_str) >= 0:
                respuesta = int(numero_str)
            else:
                respuesta = -2

    except:
        respuesta = -3

    return respuesta



# print(sanitizar_entero('37o56s-4857sg6'))
# print(sanitizar_entero('-0293847239847'))
# print(sanitizar_entero('  '))
# print(sanitizar_entero(' 02358 '))

# 3.2

def sanitizar_flotante(numero_str:str): # '37o56s-4857sg6'
    numero_str = numero_str.strip()
    numero_str_aux = numero_str
    respuesta = None
    contador_puntos = 0 
    try:
        if (numero_str[0]) == '-': # verifico si inicia con un -. if True, no guardo el - en numero_str_aux 
            numero_str_aux = numero_str[1:] # 

        for caracter in numero_str_aux:
            if caracter == '.':
                contador_puntos += 1
        
        if contador_puntos == 1: # si contiene un . lo paso a flotante 
            if float(numero_str) >= 0:
                respuesta = float(numero_str) # si es positivo, 
            else:
                respuesta = -2 # y si es negativo devuelvo -2
        else: 
            contiene_caracteres_no_numerocos = re.search('[a-zA-Z]', numero_str_aux)
            if contiene_caracteres_no_numerocos != None:
                respuesta = -1

    except: #agarra cualquier tipo de error y devuelve -3
        respuesta = -3

    return respuesta

# print(sanitizar_flotante('37o56s4857sg6')) # -1
# print(sanitizar_flotante('-29.3333')) # -2
# print(sanitizar_flotante('  ')) # -3
# print(sanitizar_flotante(' 2.358 ')) # el numero 


# 3.3                     
def sanitizar_string(valor_str: str, valor_por_defecto = '-'):
    valor_str = valor_str.strip()
    valor_str = re.sub('/', ' ', valor_str)

    valor_con_numero = re.search('[0-9]', valor_str)
        
    if valor_con_numero != None:
        respuesta = 'N/A'
    else:
        valor_lista = re.findall('[a-zA-Z ]', valor_str)
        valor_str = ''.join(map(str, valor_lista))
        respuesta = valor_str.lower()

    if valor_str == '':
        respuesta = valor_por_defecto.lower()

    return respuesta


# print(sanitizar_string('', 'HOLA' ))

# 3.4

'''
Crear la función ‘sanitizar_dato’ la cual recibirá como parámetros:
● heroe: un diccionario con los datos del personaje
● clave: un string que representa el dato a sanitizar (la clave del
diccionario). Por ejemplo altura
● tipo_dato: un string que representa el tipo de dato a sanitizar. Puede
tomar los valores: ‘string’, ‘entero’ y ‘flotante’
La función deberá sanitizar el valor del diccionario correspondiente a la clave
y al tipo de dato recibido
Para sanitizar los valores se deberán utilizar las funciones creadas en los
puntos 3.1, 3.2, 3.3 y 3.4

Se deberá validar:
● Que tipo_dato se encuentre entre los valores esperados (‘string, ‘entero,
‘flotante)’ la validación debe soportar que nos lleguen mayúsculas o
minúsculas. En caso de encontrarse un valor no válido informar por
pantalla: ‘Tipo de dato no reconocido’

● Que clave exista como clave dentro del diccionario heroe. En caso de
no encontrarse, informar por pantalla: ‘La clave especificada no
existe en el héroe’. (en este caso la validación es sensible a
mayúsculas o minúsculas)
Ejemplo de llamada a la función válida:
sanitizar_dato(dict_personaje, “altura”, “Flotante”)
La función deberá devolver True en caso de haber sanitizado algún dato y
False en caso contrario.
'''

def sanitizar_dato(heroe: dict, clave:str, tipo_dato: str):
    tipo_dato = tipo_dato.lower() 
    respuesta = True

    if clave in heroe:
        if tipo_dato == 'string':
            sanitizar_string(heroe[clave])

        elif tipo_dato == 'flotante':
            sanitizar_flotante(heroe[clave])

        elif tipo_dato == 'entero':
            sanitizar_entero(heroe[clave])

        else: 
            print('Tipo de dato no reconocido')
            respuesta = False
    else:
        print('La clave especificada no existe en el héroe')
        respuesta = False

    return respuesta


# print(sanitizar_dato(lista_personajes[0], 'altura', 'flotante'))

# 3.5
def stark_normalizar_datos(lista_heroes: list):
    if len(lista_heroes) > 0:
        for heroe in lista_heroes:
            sanitizar_dato(heroe, 'altura', 'flotante')
            sanitizar_dato(heroe, 'peso', 'flotante')
            sanitizar_dato(heroe, 'color_ojos', 'string')
            sanitizar_dato(heroe, 'color_pelo', 'string')
            sanitizar_dato(heroe, 'fuerza', 'entero')
            sanitizar_dato(heroe, 'inteligencia', 'string')
        print('Datos normalizados')
    else:
        print('Error: Lista de héroes vacía')

# stark_normalizar_datos(lista_personajes)

# 4.1

def stark_imprimir_indice_nombre(lista_heroes):
    indice_nombres = ''
    for heroe in lista_heroes:
        nombre:str = heroe['nombre']
        nombre_sin_the = re.sub('the ', '', nombre)
        nombre_reemplazado = nombre_sin_the.replace(' ', '-')
        indice_nombres += f'{nombre_reemplazado}-'
    return indice_nombres

# print(stark_imprimir_indice_nombre(lista_personajes))


# 5.1

def generar_separador(patron:str, largo:int, imprimir=True):
    separador = ''
    if (len(patron) >= 1 and len(patron) <= 2) and (largo >= 1 and largo <= 235):
        
        for i in range(largo):
            separador += patron

        if imprimir == True:
            print(separador)
        
    else:
        separador = 'N/A'
    return separador

generar_separador('*',7,)
'''
Brief:

Parametros:
    heroe: diccionario
Retorno:

'''

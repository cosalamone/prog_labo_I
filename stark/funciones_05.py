from data_stark import lista_personajes
import re
import json
from funciones_04 import * 


# 1.1s
def leer_archivo(nombre_archivo:str):
    '''
Brief:
    Abre el archivo indicado por parametro sólo en modo lectura
Parametros:
    nombre_archivo: str --> Corresponde al nombre del archivo y a la extension del mismo
Retorno:
    Retorna un string con la informacion del archivo. En caso de ocurrir un error Retorna False
'''
    
    respuesta = ''
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            for linea in archivo:
                respuesta += f'{linea} /n'
            print(respuesta)
    except FileNotFoundError:
        respuesta = False
        errorMessage = f'No such file or directory: {nombre_archivo}'
        print(errorMessage)
        return respuesta 
    
# leer_archivo('./stark/data.json')

# 1.2
def guardar_archivo(path:str, contenido: str):
    '''
Brief:
    Abre el archivo indicado por parametro y sobreescribe la información con lo recibido en conetido. 
    En caso de no existir aún el archivo, lo crea y guarda la informacion
Parametros:
    path: str --> Corresponde al nombre del archivo y a la extension del mismo
    conteido: str -> string con la información a guardar en el archivo
Retorno:
    retorna True si no hubo errores, caso contrario False.
'''
    retorno = False
    try: 
        with open(path, 'w+', encoding='utf-8') as archivo:
            guardado = archivo.write(f'{contenido}')
            if guardado:
                retorno = True
                print(f'Se creó el archivo: {path}')
    
    except FileNotFoundError:
        errorMessage = f'No such file or directory: {path}'
        print(errorMessage)
        retorno = False
    finally:
        return retorno

info_a_guardar = '''nombre,identidad,empresa,altura,peso,genero,color_ojos,color_pelo,fuerza,inteligencia
Spider-Man,Peter Parker,Marvel,1.78,76.2,Hombre,Marrón,Castano,8,alta
Iron Man,Tony Stark,Marvel,1.85,88.5,Hombre,Azul,Negro,6,sobresaliente
Black Widow,Natasha Romanoff,Marvel,1.7,58.0,Mujer,Verde,Pelirrojo,7,alta
'''

# 1.3
def generar_csv(path, lista_heroe:list):
    '''
Brief:
    Genera un archivo csv en base a la lista recibida por parametro y la guarda en un archivo 
    Primero toma los encabezados y seguido de ellos en las lineas siguientes se guarda la información. 
Parametros:
    path: str --> Corresponde al nombre del archivo y a la extension del mismo donde guardará la información
    lista_heroe: list
Retorno:
    En caso de exito retorna True.
    De estar vacia la lista retorna False
'''    
    
    try: 
        contenido = ''
        heroe:dict
        encabezado = True
        if len(lista_heroe) > 0:
            
            for heroe in lista_heroe:
                # en la primer vuelta tomo los encabezados
                if encabezado == True:
                    lista = list(heroe.keys())
                    for key in lista:
                        contenido += f'{key},'
                    encabezado = False
                    contenido += '\n'
            
                # en toda iteracion tomo los valores que componen a cada heroe
                nombre = heroe['nombre']
                identidad = heroe['identidad']
                empresa = heroe['empresa']
                altura = heroe['altura']
                peso = heroe['peso']
                genero = heroe['genero']
                color_ojos = heroe['color_ojos']
                color_pelo = heroe['color_pelo']
                fuerza = heroe['fuerza']
                inteligencia = heroe['inteligencia']

                contenido += f'{nombre},{identidad},{empresa},{altura},{peso},{genero},{color_ojos},{color_pelo},{fuerza},{inteligencia}\n'

            respuesta = guardar_archivo(path, contenido)
        else:
            respuesta =  False
    except FileNotFoundError:
        errorMessage = f'No such file or directory: {path}'
        print(errorMessage)
    except TypeError:
        errorMessage = f'TypeError: {path}'
        print(errorMessage)
    
    finally:
        return respuesta


# 1.4
def leer_csv(path:str):
    '''
Brief:
    En base al nombre del archivo csv recibido por parametro, genera una lista de heroes. Cada heroe será un diccionario
Parametros:
    path:str
Retorno:
    Retorna la lista de diccionarios de los heroes en caso que exista el archivo. Caso contrario False. 
'''
    retorno = None
    encabezado = True
    try: 
        lista_completa = []
        with open(path, 'r', encoding='utf-8') as archivo:
            for linea in archivo:
                lista = linea.split(',')
                if encabezado == True:
                    encabezado = False
                else:
                    heroe = {}
                    heroe['nombre'] = lista[0]
                    heroe['identidad'] = lista[1]
                    heroe['empresa'] = lista[2]
                    heroe['altura'] = float(lista[3])
                    heroe['peso'] = float(lista[4])
                    heroe['genero']= lista[5]
                    heroe['color_ojos'] = lista[6]
                    heroe['color_pelo'] = lista[7]
                    heroe['fuerza'] = int(lista[8])
                    heroe['inteligencia'] = lista[9]
                    lista_completa.append(heroe)
            retorno = lista_completa
            print(retorno)
    except FileNotFoundError: 
        retorno = False
    finally:
        return retorno


# 1.5
def generar_json(path: str, lista_heroes: list, nombre_lista: str, sanitizado=False): 
    '''
Brief:
    guarda en un diccionario de una sóla clave la lista de superhéroes,el nombre de clave debería ser la del tercer parámetro que sería el nombre de la lista.
Parametros:
    path: str,
    lista_heroes: list, 
    nombre_lista: str
Retorno:
    No tiene retorno 
'''
    if len(lista_heroes) > 0:
        if sanitizado == False: # sanitiza los datos sólo si se llama puntualmente a la fx, 
                                # Si se llama desde el menú y se habia sanitizado, no vuelve a sanitizar
            stark_normalizar_datos(lista_heroes)

        data_stark = {nombre_lista: lista_heroes}

        data_json = json.dumps(data_stark, indent=4)

        with open(path, 'w+') as archivo:
            archivo.write(data_json)
        print(f"Se ha generado el archivo JSON en {path}")
        
    else:
        print("La lista de superhéroes está vacía. No se generará ningún archivo JSON.")


# 1..6
def leer_json(path: str, nombre_lista:str)->list:
    '''
Brief:
    Lee archivo json según la informacion recibida por parametro
Parametros:
    path: str,
    nombre_lista:str
Retorno:
    Retrona la lista si se leyó correctamente, sino False
'''
    retorno = None
    try:
        with open(path,'r') as archivo:
            dict_json = json.load(archivo)
            retorno = dict_json[nombre_lista]
            
    except FileNotFoundError:
        retorno = False
    finally:
        return retorno


# 2.1 Crear una función para ordenar héroes por alguna de las claves númericas (altura, peso y fuerza) de manera ascendente

def ordenar_ascendente(lista_heroes:list, clave: str):
    '''
Brief:
    Ordena la lista por alguna de las caracteristicas numericas del heroe de forma ascendente
Parametros:
    lista_heroe:list, 
    key: str
Retorno:
    La lista ordenada acendentemente
'''
    if clave == 'altura' or clave == 'peso' or clave == 'fuerza':
        if type(lista_heroes[0]['altura'])  != float:
            stark_normalizar_datos(lista_heroes)
            
            lista_heroes.sort(key = lambda heroe:heroe[clave])
        else:
            
            lista_heroes.sort(key = lambda heroe:heroe[clave])
    else: 
        lista_heroes = 'La caracteristica indicada no es numerica'
    return lista_heroes 


# ordenar_ascendente(lista_personajes, 'fuerza')


# 2.2 Crear una función para ordenar héroes por alguna de las claves númericas (altura, peso y fuerza) de manera descendente.

def ordenar_descendente(lista_heroes:list, clave: str):
    '''
Brief:
    Ordena la lista por alguna de las caracteristicas numericas del heroe de forma descendente
Parametros:
    lista_heroe:list, 
    key: str
Retorno:

'''

    if clave == 'altura' or clave == 'peso' or clave == 'fuerza':
        if type(lista_heroes[0]['altura'])  != float:
            stark_normalizar_datos(lista_heroes)
            
            lista_heroes.sort(key = lambda heroe:heroe[clave], reverse= True)
        else:
            
            lista_heroes.sort(key = lambda heroe:heroe[clave], reverse= True)
    else: 
        lista_heroes = 'La caracteristica indicada no es numerica'
    return lista_heroes 

print(ordenar_descendente(lista_personajes, 'peso'))


# 2.3 Crear una función para ordenar héroes por alguna de las claves númericas (altura, peso y fuerza). Preguntar al usuario si lo quiere ordenar de manera ascendente (‘asc’) o descendente (‘desc’) (reutilizar funciones anteriores dependiendo del caso)

def ordenar(lista_heroes: list,key:str):
    '''
Brief:

Parametros:
    heroe: diccionario
Retorno:

'''
    modo_ordenamiento = input('Por favor, indicar de que forma desea ordenar la lista según una característica numerica: asc o desc \n')
    
    while modo_ordenamiento.lower() != 'asc' and modo_ordenamiento.lower != 'desc':
        modo_ordenamiento = input('Las opciones son: asc o desc')

    if modo_ordenamiento == 'desc':
        lista_ordenada = ordenar_descendente(lista_heroes, key)
    elif modo_ordenamiento == 'asc':
        lista_ordenada =  ordenar_ascendente(lista_heroes, key)
    return lista_ordenada
    

def  obligatorio_normalizar(lista_heroes, sanitizado:bool = False): 
    '''
Brief:
    Solicita que el usuario normalice los datos ingresando opcion 1
Parametros:
    - Lista_heroes(list): Lista de diccionarios de los heroes
Retorno:
    Retorna True en caso que se hayan normalizado
    '''
    if sanitizado == True:
        print('La lista ya fue santitizada')
    else:

        opcion = input('Para ingresar al menú es necesario normalizar los datos, por favor ingrese 1:  ')
        while opcion != '1':
            opcion = input('La opcion a ingresar debe ser 1  ')
        stark_normalizar_datos(lista_heroes)
        return True

def stark_normalizar(normalizado):
    '''
Brief:
    Confirma si los datos fueron o no normalizados
Parametros:
    - Lista(list): Lista de diccionarios de los heroes
    - Key(str): es la característica que se desea buscar
Retorno:
    Imrpime mensaje según si los datos fueron o no normalizados
    '''
    if normalizado == True:
        print('Datos Normalizados')
    else:
        print('Hubo un error al normalizar los datos. Verifique que la lista no este vacía o que los datos ya no se hayan normalizado anteriormente')



def menu_generar_e_imprimir_csv(lista_heroes):
    generar_csv('./stark/nuevo_archivo.csv', lista_heroes)
    lista_generada = leer_csv('./stark/nuevo_archivo.csv')
    print(lista_generada) 


def menu_listar_heroes_orden_altura_asc(lista_heroes):
    
    return ordenar_ascendente(lista_heroes,'altura')


def menu_generar_e_imprimir_json(lista_heroes):
    generar_json('./stark/nuevo_archivo.json', lista_heroes, 'heroes', True)
    lista_generada = leer_json('./stark/nuevo_archivo.json', 'heroes')
    print(lista_generada)


def menu_listar_heroes_orden_peso_desc(lista_heroes):
    return ordenar_descendente(lista_heroes,'peso')

def menu_listar_heroes_orden_fuerza(lista_heroes):
    print(ordenar(lista_heroes, 'fuerza'))


# 3
def menu_stark_cinco(lista_heroes:list):
    '''
Brief:

Parametros:
    heroe: diccionario
Retorno:

'''
    menu_running = True

    sanitizado = obligatorio_normalizar(lista_heroes)

    opciones_menu = '''Elija una de las siguientes opciones:
1-Normalizar datos 
2-Generar CSV 
3-Listar heroes del archivo CSV ordenados por altura ASC 
4-Generar JSON
5-Listar heroes del archivo JSON ordenados por peso DESC 
6-Ordenar Lista por fuerza 
7-Salir
''' 
    opciones_repregunta_menu = 'Las opciones validas son del 1 al 7'


    while  menu_running:

        if sanitizado == True:

            opcion_seleccionada = int(input(opciones_menu))

            
            while opcion_seleccionada < 2 and  opcion_seleccionada > 7:
                opcion_seleccionada = int(input(opciones_repregunta_menu))
            
            match opcion_seleccionada:
                case 1:
                    obligatorio_normalizar(lista_heroes, True)
                case 2:
                    menu_generar_e_imprimir_csv(lista_heroes)

                case 3:
                    print(menu_listar_heroes_orden_altura_asc(lista_heroes))

                case 4:
                    menu_generar_e_imprimir_json(lista_heroes)

                case 5:
                    print(menu_listar_heroes_orden_peso_desc(lista_heroes))

                case 6:
                    menu_listar_heroes_orden_fuerza(lista_heroes)
                
                case 7:
                    menu_running = False


# menu_stark_cinco(lista_personajes)
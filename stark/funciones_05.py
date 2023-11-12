from data_stark import lista_personajes
import re
import json
from funciones_04 import * 


# 1.1
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
    retorno = None
    try: 
        with open(path, 'w+', encoding='utf-8') as archivo:
            retorno = archivo.write(f'{contenido}')
            if retorno:
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

# print(guardar_archivo('./stark/data_stark.csv', info_a_guardar))

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

            guardar_archivo(path, contenido)
        else:
            return False
    except FileNotFoundError:
        errorMessage = f'No such file or directory: {path}'
        print(errorMessage)
    except TypeError:
        errorMessage = f'TypeError: {path}'
        print(errorMessage)

# generar_csv('./stark/data_stark_prueba.csv',lista_personajes)


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
            # VER COMO ELIMINAR EL ÚLTIMO \N DEL FINAL
            for linea in archivo:
                lista = linea.split(',')
                # print(lista)
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

# print(leer_csv('./stark/data_stark_pruebaaaaa.csv'))


# 1.5
def generar_json(path: str, lista_heroes: list, nombre_lista: str): 
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
        stark_normalizar_datos(lista_heroes)
        data_stark = {nombre_lista: lista_heroes}

        data_json = json.dumps(data_stark, indent=4)

        with open(path, 'w+') as archivo:
            archivo.write(data_json)
        print(f"Se ha generado el archivo JSON en {path}")
        
    else:
        print("La lista de superhéroes está vacía. No se generará ningún archivo JSON.")

# generar_json('./stark/data_stark.json', lista_personajes, 'heroes')


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
    # para hacerlo con expresiones regulares + info en 1:38:00 video clase 8
    retorno = None
    try:
        with open(path,'r') as archivo:
            dict_json = json.load(archivo)
            retorno = dict_json[nombre_lista]
            
    except FileNotFoundError:
        retorno = False
    finally:
        return retorno

print(leer_json('./stark/data_stark.json', 'heroes'))
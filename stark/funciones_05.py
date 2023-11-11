from data_stark import lista_personajes
import re


# 1.1
def leer_archivo(nombre_archivo:str):
    '''
Brief:
    Abre el archivo indicado por parametro, según la extensión que sea. Lo hace sólo en modo lectura
Parametros:
    nombre_archivo: str --> Corresponde al nombre del archivo y a la extension del mismo
Retorno:
    Retorna un string con la informacion del archivo.
'''
    respuesta = ''
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            for linea in archivo:
                respuesta += f'{linea} /n'
            print(respuesta)
    except:
        respuesta = False
        return respuesta # VER COMO IMPRIMIR EL MENSAJE DEL ERROR Y VER VALIDA EXCEPCIONES
    

# leer_archivo('C:/Users/RodrigoVazquez/Documents/REPOSITORIOS/prog_labo_I/data_archivos.csv')


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
    with open(path, 'w+', encoding='utf-8') as archivo:
        retorno = archivo.write(f'{contenido}\n')
        if retorno:
            retorno = True
            print(f'Se creó el archivo: {path}')
        else:
            retorno = False
            print(f'Error al crear el archivo: {path}')
        return retorno
    # VER COMO VALIDAR EXCEPCIONES

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
    De estar vacia la lista retorna False
'''    
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
            else: 
                # luego tomo los valores que componen a cada heroe
                nombre = heroe['nombre']
                identidad = heroe['identidad']
                empresa = heroe['empresa']
                altura = heroe['altura']
                peso = heroe['peso']
                fuerza = heroe['fuerza']
                color_ojos = heroe['color_ojos']
                color_pelo = heroe['color_pelo']
                inteligencia = heroe['inteligencia']

                contenido += f'{nombre},{identidad},{empresa},{altura},{peso},{fuerza},{color_ojos},{color_pelo},{inteligencia}\n'

        guardar_archivo(path, contenido)
    else:
        return False


# generar_csv(lista_personajes)


# 1.4

'''
Brief:
Parametros:
Retorno:
'''
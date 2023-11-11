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

print(guardar_archivo('./stark/data_stark.csv', info_a_guardar))
# 1.3
def generar_csv(path:str, lista_heroe:list):
    '''
Brief:
Parametros:
    path: str --> Corresponde al nombre del archivo y a la extension del mismo
Retorno:
'''
    lista_completa = []
    retorno = None
    if len(lista_heroe) > 0:
        with open(path, 'w+', encoding='utf-8') as archivo:
            for linea in archivo:
                lista = linea.split(',')
                heroe = {}
                heroe['nombre'] = lista[0]
                heroe['identidad'] = lista[1]
                heroe['empresa'] = lista[2]
                heroe['altura'] = float(lista[3])
                heroe['peso'] = float(lista[4])
                heroe['genero'] = lista[5]
                heroe['color_ojos'] = lista[6]
                heroe['color_pelo'] = lista[7]
                heroe['fuerza_'] = int(lista[8])
                heroe['inteligencia'] = lista[9]

            lista_completa.append(heroe)
            retorno = archivo.write(f'{lista_heroe}')
            if retorno:
                print(f'Se generó el archivo csv: "{path}"')
                retorno = True
            else:
                print(f'Error al generar el archivo csv: "{path}"')
                retorno = False
    return retorno


# generar_csv('stark/data_stark.csv', lista_personajes)

'''
Brief:
Parametros:
Retorno:
'''
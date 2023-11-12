from data_stark import lista_personajes
from funciones import *


def stark_normalizar_datos(lista):
    '''
Brief:
    Funcion para normalizar los numeros enteros y flotantes de la lista

Parametros:
- Lista(lista)

Retorno:
    Valor booleano dependiendo si se normalizaron los datos(True) o no (False)
    '''
    flag = False
    for heroe in lista:
        if type(heroe['fuerza']) != int:
            heroe['fuerza'] = int(heroe['fuerza'])
            flag = True
        
        if type(heroe['altura']) != float:
            heroe['altura'] = float(heroe['altura'])
            flag = True

        
        if type(heroe['peso']) != float:
            heroe['peso'] = float(heroe['peso'])
            flag = True

    return flag


def obtener_dato(heroe:dict, key:str):
    '''
Brief:
    Obtener de un diccionario, el valor de la key buscada

Parametros:
- Lista(lista)
- key(str)


Retorno:
    El valor de key buscada o False en caso de no encontrarse la key en el diccionario
    '''
    for clave in heroe:
        if clave == key:
            dato = heroe[clave]
            break 
        else:
            dato = False
    return dato



def obtener_nombre(heroe:dict)-> str:
    '''
Brief:
    Obtener el nombre del heroe dentro del diccionario.

Parametros:
- Lista(lista)

Retorno:
    El valor de key 'nombre' o False en caso de no encontrarse la key en el diccionario
'''
    for clave in heroe:
        if clave == 'nombre':
            respuesta = f'Nombre: {heroe[clave]}'
            break
        else:
            respuesta = False
    return respuesta




# verifiqué que el dato bucado exista
def obtener_nombre_dato(heroe: dict, key:str)-> str:
    '''
Brief:
    Obtener la key buscada dentro del diccionario.

Parametros:
- Lista(lista)
- key(str)

Retorno:
    Un string: Nombre: {nombre} | {key}: 500.El valor de key 'nombre' o False en caso de no encontrarse el dato
'''

    nombre = obtener_nombre(heroe)
    dato = obtener_dato(heroe, key)
    
    if dato != False:
        dato = f'{nombre} | {key}: {dato}'
    
    return dato



def obtener_maximo(lista: list, key:str): 
    '''
Brief:
    Obtener el valor maximo key buscada dentro del diccionario. Verifica que el valor deseado sea de tipo int o float

Parametros:
- Lista(lista)
- key(str)

Retorno:
    El valor maximo de la key buscada o False en caso de no encontrarse el dato
'''
    stark_normalizar_datos(lista)
    maximo = lista[0][key]
    for hereo in lista:
        if type(hereo[key]) == float or type(hereo[key]) == int:
            if  hereo[key] > maximo:
                maximo = hereo[key]
        else:
            maximo = False

    return maximo




def obtener_minimo(lista:list, key: str):
    '''
Brief:
    Obtener el valor minimo de la key buscada dentro del diccionario. 
    Verifica que el valor deseado sea de tipo int o float

Parametros:
- Lista(lista)
- key(str)

Retorno:
    El valor minimo de la key buscada o False en caso de no encontrarse el dato
'''
    stark_normalizar_datos(lista)
    minimo = lista[0][key]
    for hereo in lista:
        if type(hereo[key]) == float or type(hereo[key]) == int:
            if  hereo[key] < minimo:
                minimo = hereo[key]
        else:
            minimo = False

    return minimo



def obtener_dato_cantidad(lista: list, numero,  key:str):
    '''
Brief:
    Obtener un nuevo listado de heroes que cumpla con el valor maximo/minimo en la key buscada.
    Verifica que el valor deseado sea de tipo int o float

Parametros:
- Lista(lista)
- numero(float/int): representa el valor maximo o minimo a buscar
- key(str)

Retorno:
    Todos los heroes que coincidan con el valor maximo/minimo en la key buscada
'''
    stark_normalizar_datos(lista) 
    lista_dato_según_cantidad = []
    for heroe in lista:
        if heroe[key] == numero:
            lista_dato_según_cantidad.append(heroe)
    return lista_dato_según_cantidad



def stark_imprimir_heroes(lista:list):
    '''
Brief:
    Imprime un listado de heroes

Parametros:
- Lista(lista)

Retorno:
    Todos los heroes que coincidan con el valor maximo/minimo en la key buscada
'''
    flag = False
    mensaje = ''
    for heroe in lista:
        flag = True
        nombre= heroe['nombre']
        identidad= heroe['identidad']
        empresa= heroe['empresa']
        altura= heroe['altura']
        peso= heroe['peso']
        genero= heroe['genero']
        color_ojos= heroe['color_ojos']
        color_pelo= heroe['color_pelo']
        fuerza= heroe['fuerza']
        inteligencia= heroe['inteligencia']

        mensaje += f'''Nombre: {nombre}
Identidad: {identidad} 
Empresa: {empresa}
Altura: {altura}
Peso: {peso}
Genero: {genero}
Color de ojos: {color_ojos}
Color de pelo: {color_pelo}
nFuerza: {fuerza} 
Inteligencia {inteligencia}
-----------------------------
'''
    print(mensaje)
    if flag == False:
        return flag



def sumar_dato_heroe(lista: list, key: str,): 
    '''
Brief:
    Recorre una lista y suma los valores de la key indicada

Parametros:
- Lista(lista)
- Key

Retorno:
    El valor de la suma
'''
    stark_normalizar_datos(lista)
    suma = 0
    for heroe in lista: 
        if type(heroe) == dict:
            suma += heroe[key]
    return suma




def dividir(dividiendo, divisor):
    '''
Brief:
    Divide los 2 numeros indicados como parametros

Parametros:
- Divisor
- Dividendo

Retorno:
    El valor de la division
'''
    if divisor == 0:
        respuesta = False
    else:
        respuesta = dividiendo/divisor
    return respuesta



def calcular_promedio(lista:list, key: str):
    '''
Brief:
    Calcula el promedio de los valores de la key indicada por parametro

Parametros:
- Lista(list)
- Key(str)

Retorno:
    El valor del promedio
'''
    stark_normalizar_datos(lista)
    acumulador = sumar_dato_heroe(lista, key)
    contador = len(lista)

    respuesta = dividir(acumulador,contador)
    return respuesta




def mostrar_promedio_dato(lista: list, key:str): 
    '''
Brief:
    Imrpime el valor del promedio  de los valores de la key indicada por parametro.

Parametros:
- Lista(list)
- Key(str)

Retorno:
    El valor del promedio. En caso que la key no sea de tipo int o float devuelve False. En caso que la lista esté vacía tambien retorna False
'''
    stark_normalizar_datos(lista)
    flag = False
    respuesta_promedio = calcular_promedio(lista, key)
    for heroe in lista:
        if type(heroe[key]) == float or type(heroe[key])== int:
            flag = True
    if flag == True:
        print(respuesta_promedio)
    else:
        return flag
        


def imprimir_menu(): 
    '''
Brief:
    Imrpime las opciones de menu

Parametros:
No recibe

Retorno:
    El mensaje con las opciones de menu
'''
    mensaje = '''
1- Normalizar datos (No se debe poder acceder a los otros puntos)
2- Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género NB
3- Recorrer la lista y determinar cuál es el superhéroe más alto de género F
4- Recorrer la lista y determinar cuál es el superhéroe más alto de género M
5- Recorrer la lista y determinar cuál es el superhéroe más débil de género M 
6- Recorrer la lista y determinar cuál es el superhéroe más débil de género NB
7- Recorrer la lista y determinar la fuerza promedio de los  superhéroes de género NB
8- Determinar cuántos superhéroes tienen cada tipo de color de ojos.
9- Determinar cuántos superhéroes tienen cada tipo de color de pelo.
10- Listar todos los superhéroes agrupados por color de ojos.
11- Listar todos los superhéroes agrupados por tipo de inteligencia
12- Salir

'''
    print(mensaje)



def validar_enteros(string: str):
    '''
Brief:
    Recibe por parametro un string y verifica que sólo esté confirmado por digitos

Parametros:
- string(str)

Retorno:
    Retornara True en caso de ser sólo digitos y False caso contrario
'''
    if string.isdigit():
        valido = True
    else:
        valido = False
    return valido



def stark_menu_principal(): 
    '''
Brief:
    Imrpime las opciones de menu, solicita al usuario una opcion y verifica que sea un string de numeros. 

Parametros:
- string(str)

Retorno:
    Si el numero ingresado es una de la opciones validas devuelve el número, sino retorna False
'''
    imprimir_menu()
    opcion = input('Ingrese una de las opciones: ')
    validacion = validar_enteros(opcion)
    if validacion == True:
        opcion = int(opcion)
        if opcion < 1 or  opcion > 12:
            opcion = False
    return opcion 





def menu_obtener_nombre_nb(lista:list, key:str):
    '''
Brief:
    Obtiene los nombres de los heroes de genero NB
Parametros:
- Lista(list): Lista de diccionarios de los heroes
- Key(str): es la característica que se desea buscar
Retorno:
    Lista de heroes NB
    '''
    stark_normalizar_datos(lista_personajes)
    mensaje = ""
    for heroe in lista:
        if heroe[key] == 'NB': 
            nombre = obtener_nombre(heroe)
            mensaje += f"{nombre}  \n"

    return mensaje


def menu_por_genero_mas_alto(lista, keyGenero: str, keyAltura: str, gen):
    '''
Brief:
    Según el genero de parametro indicado, devuelve una lista del mas alto
Parametros:
- Lista(list): Lista de diccionarios de los heroes
- Key(str): es la característica que se desea buscar
Retorno:
    Lista de heroes
    '''
    lista_filtrada = []
    for heroe in lista:
        if heroe[keyGenero] == gen:
            lista_filtrada.append(heroe)

    maximo = obtener_maximo(lista_filtrada, keyAltura)
    lista_maximos = obtener_dato_cantidad(lista_filtrada, maximo, keyAltura)
    for f in lista_maximos:
        print(f['nombre'])

def menu_por_genero_min_fuerza(lista, keyGenero: str, keyAltura: str, gen):
    '''
Brief:
    Imprime el promedio de una característica buscada en un genero en particular
Parametros:
    - Lista(list): Lista de diccionarios de los heroes
    - Key(str): es la característica que se desea buscar
Retorno:
    no retorna
    '''
    lista_filtrada = []
    for heroe in lista:
        if heroe[keyGenero] == gen:
            lista_filtrada.append(heroe)

    minimo = obtener_minimo(lista_filtrada, keyAltura)
    lista_minimo = obtener_dato_cantidad(lista_filtrada, minimo, keyAltura)
    for f in lista_minimo:
        print(f['nombre'])

def menu_promedio_por_genero(lista, keyGenero: str, keyfuerza: str, gen):
    '''
Brief:
    Imprime el promedio de una característica buscada en un genero en particular
Parametros:
    - Lista(list): Lista de diccionarios de los heroes
    - Key(str): es la característica que se desea buscar
Retorno:
    no retorna
    '''
    lista_filtrada = []
    for heroe in lista:
        if heroe[keyGenero] == gen:
            lista_filtrada.append(heroe)
    
    mostrar_promedio_dato(lista_filtrada, keyfuerza)

def menu_mostrar_cantidad_por_caracteristica(lista:list, key:str):
    '''
Brief:
    Imprime la cantidad de heroes que coinciden con la característica buscada
Parametros:
    - Lista(list): Lista de diccionarios de los heroes
    - Key(str): es la característica que se desea buscar
Retorno:
    No retorna
    '''
    for heroe in lista:
        obtener_dato(heroe, key)
        dicrionario_keys = crear_contadores_para_cada_key(lista, key)
        cantidad_coincidencias = contador_de_coincidencias(lista, dicrionario_keys, key )
    print(cantidad_coincidencias)

# menu_mostrar_cantidad_por_caracteristica(lista_personajes, 'color_ojos')

def  obligatorio_normalizar(lista): 
    '''
Brief:
    Solicita que el usuario normalice los datos ingresando opcion 1
Parametros:
    - Lista(list): Lista de diccionarios de los heroes
Retorno:
    Retorna True en caso que se hayan normalizado
    '''
    
    opcion = input('Para ingresar al menú es necesario normalizar los datos, por favor ingrese 1:  ')
    while opcion != '1':
        opcion = input('La opcion a ingresar debe ser 1  ')
    stark_normalizar_datos(lista)
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
    
def stark_marvel_app(lista:list):
    flag = True
    #flag_dos = False
    sanitizado = obligatorio_normalizar(lista)

    while flag:

        if sanitizado == True:
            
            respuesta = stark_menu_principal()

            match respuesta:
                case 1:
                    stark_normalizar(stark_normalizar_datos(lista))
                case 2:
                    print(menu_obtener_nombre_nb(lista, 'genero'))
                case 3:
                    menu_por_genero_mas_alto(lista,'genero','altura', 'F' )
                case 4:
                    menu_por_genero_mas_alto(lista,'genero','altura', 'M')
                case 5:
                    menu_por_genero_min_fuerza(lista,'genero','fuerza', 'M')
                case 6:
                    menu_por_genero_min_fuerza(lista,'genero','fuerza', 'NB')
                case 7:
                    menu_promedio_por_genero(lista,'genero','fuerza', 'NB')
                case 8:
                    menu_mostrar_cantidad_por_caracteristica(lista, 'color_ojos')
                case 9:
                    menu_mostrar_cantidad_por_caracteristica(lista, 'color_pelo')
                case 10:
                    mostrar_nombre_heroes_por_cada_característica(lista,'color_ojos')
                case 11:
                    mostrar_nombre_heroes_por_cada_característica(lista,'inteligencia')
                case 12:
                    flag = False
                

stark_marvel_app(lista_personajes)




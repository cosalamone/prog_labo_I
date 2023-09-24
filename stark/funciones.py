#from data_stark import lista_personajes


def agrupar_segun_genero(lista:list, genero_por_buscar:str)-> list:
    '''
Brief: Crea una lista discriminada según genero. 

Parametros:
- Lista(list): Lista sobre la cual buscará los generos indicados
- Genero_por_buscar(str): Genero por el cual se quiere filtrar

Retorno:
Lista de heroes filtrada según el genero indicado
    
    '''
    sh_genero = []

    for i in lista:
        genero = i['genero']

        if genero == genero_por_buscar:
            sh_genero.append(i)
    
    return sh_genero



def mostrar_nombre_segun_genero(lista:list, genero_por_buscar:str):
    '''
    Brief:
        Muestra el nombre de los heroes según su genero.
    
    Parametros:
    - Lista(list): Lista de diccionarios de los heroes
    - Genero(str): 'F', 'M', 'NB'
    
    Retorno:
        Sin retorno. Imprime en consola los nombres de los heroes según su genero.
    '''
    lista_segun_genero = agrupar_segun_genero(lista, genero_por_buscar)
    mensaje = f'Los superheroes {genero_por_buscar} son:'        
    print(mensaje)

    for heroe in lista_segun_genero:
        nombre = heroe['nombre']

        print(nombre)



def parsear_datos(lista):
    '''
Brief:
    Funcion para paresear los numeros enteros y flotantes de la lista

Parametros:
- Lista(lista)

Retorno:
    Lista con los datos numericos parseados a enteros o flotantes según corresponda
    '''
    for heroe in lista:
        heroe['fuerza'] = int(heroe['fuerza'])
        heroe['altura'] = float(heroe['altura'])
        heroe['peso'] = float(heroe['peso'])
    return lista


def encontrar_mayor_o_menor_caracteristica(lista:list, key: str, operador: str):
    '''
Brief: 
    Encuentra el valor flotante más alto o mas bajo según una determinada característica.

Parametros:
- Lista(list): sobre la cual trabajará
- Key(str): es la característica que se desea buscar, debe inticarse en string
- Operador(str): mayor o menor, tambien en string

Retorno:
    Valor encontrado, ya sea el mayor o el menor según esa caracteristica
    '''
    lista = parsear_datos(lista)
    contador = None

    for heroe in lista:
        caracteristica_buscada = heroe[key]

        if operador == 'mayor': 
            if contador == None or caracteristica_buscada > contador:
                contador = caracteristica_buscada
        else:
            if operador == 'menor':
                if contador == None or caracteristica_buscada < contador:
                    contador = caracteristica_buscada
        
    return(contador)


def agrupar_personajes_segun_mayor_o_menor_caracteristica(lista: list, contador, key)->list:
    '''
Brief:
    Agrupa los heroes con la mayor o menor caracteristica buscada. Ej: los heros con mayor altura
Parametros:
- Lista(list): sobre la cual trabajará
- Contador(numero): valor que mayor o menor que tiene la caracteristica
- Key(str): es la característica que se desea buscar

Retorno:
    Lista de heroes filtrada según el valor de la caracteristica buscada
    '''
    lista = parsear_datos(lista)

    lista_agrupada = []

    for heroe in lista:
        caracteristica_buscada = heroe[key]
        if contador == caracteristica_buscada:
            lista_agrupada.append(heroe)
    return lista_agrupada


def crear_contadores_para_cada_key(lista:list, key):
    '''
Brief:
    Crea un diccionario, donde cada key se inicializa como un contador en 0.

Parametros:
- Lista(list): sobre la cual trabajará
- Key(str): es la característica que se desea buscar
Retorno:
    Devuelva un diccionario con cada caracteristica iniciada en 0, que funcionará como contador
'''
    diccionario = {}

    for elemento in lista:
        key_a_buscar = (elemento[key]).lower()
        if key_a_buscar not in diccionario:
            diccionario[key_a_buscar] = 0  

    return diccionario


def contador_de_coincidencias(lista, diccionario, key): 
    '''
Brief:
    Hace un conteo en el diccionario recibido según la cantidad de coincidencias que encuentre por cada hereo de la lista

Parametros:
- Lista(list): sobre la cual trabajará
- Diccionario: Sobre el cual realizará el conteo
- Key(str): es la característica que se desea buscar
Retorno:
    Devuelve un diccionario el cual tiene la cantidad correspondiente a cada característica buscada

    '''

    for elemento in lista:
        coincidencias = (elemento[key]).lower()
        diccionario[coincidencias] += 1

    return diccionario

        

def mostrar_cantidad_heroes_segun_caracteristica(lista:list, key:str):
    '''
Brief:
    Recorre una lista finalmente para mosterar la cantidad de heroes que hay según una determinada caracteristica

Parametros:
- Lista(list): sobre la cual trabajará
- Key(str): es la característica que se desea buscar
Retorno:
    Devuelve un diccionario el cual tiene cada característica con su correspondiente cantidad
    '''
    diccionario_contador = crear_contadores_para_cada_key(lista, key)
    diccionario = contador_de_coincidencias(lista, diccionario_contador, key)

    print(diccionario)


def mostrar_heroe_segun_caracteristica(lista:list, genero: str, key:str, operador:str):
    '''
Brief:
    Recorre una lista para mostrar el nombre de los heroes buscados según su genero y la característica deseada, ya sea en su valor más alto o mas bajo.
    
Parametros:
    - Lista(list): Lista de diccionarios de los heroes
    - Genero(str): 'F', 'M', 'NB'
    - Key(str): es la característica que se desea buscar
    - Operador(str): mayor o menor, tambien en string
    
Retorno:
    Sin retorno. Imprime en consola los nombres de los heroes buscados.
    '''
    heroe_por_genero = agrupar_segun_genero(lista, genero)
    heroe_mas_alto = encontrar_mayor_o_menor_caracteristica(heroe_por_genero, key, operador)
    lista_heroes= agrupar_personajes_segun_mayor_o_menor_caracteristica(heroe_por_genero, heroe_mas_alto, key)

    if len(lista_heroes) == 1:
        mensaje = f'''El superheroe {genero} de {operador} {key} es:
{lista_heroes[0]['nombre']}
''' 
        print(mensaje)

    else:
        if len(lista_heroes) > 1:
            mensaje = f'Los superheroes {genero} de {operador} {key} son:'        
            print(mensaje)

            for heroe_femenino in lista_heroes:
                print(heroe_femenino['nombre'])


def calcular_fuerza_promedio_segun_genero(lista:list, genero):
    '''
Brief:
    Recorre una lista y calcula la fuerza promedio de un genero determinado
Parametros:
    - Lista(list): Lista de diccionarios de los heroes
    - Genero(str): 'F', 'M', 'NB'
Retorno:
    Devuelve el promedio buscado
'''
    contador = 0
    acumulador = 0 
    
    heroes = agrupar_segun_genero(lista, genero)

    heroes = parsear_datos(heroes)
    for heroe in heroes:        
        contador += 1
        acumulador += heroe['fuerza']

    if contador != 0:
        promedio = acumulador/contador
        return promedio


def imprimir_promedio(promedio):
    '''
Brief:
    Imprime un mensaje con el valor del promedio recibido
Parametros:
    - Promedio(numero)
Retorno:
    No tiene.
'''
    mensaje = f'El promedio es {promedio}'
    print(mensaje)


def crear_diccionario_string_para_cada_key(lista:list,  key:str):
    '''
Brief:
    Crea un diccionario, donde cada key(caracterítica) encontrada se inicializa en un string vacío (''), con el objetivo de luego poder ir agregando datos a esa característica.
Parametros:
    - Lista(list): Lista de diccionarios de los heroes
    - Key(str): es la característica que se desea buscar
Retorno:
    Devuelve un diccionario con todas las características encontradas inicializadas en ''
    '''
    diccionario = {}

    for elemento in lista:
        key_a_buscar =elemento[key]
        if key_a_buscar not in diccionario:
            diccionario[key_a_buscar] = ''  

    return diccionario

def mostrar_nombre_heroes_por_cada_característica(lista:list, key_caracteristica:str):
    '''
Brief:
    Imprime un diccionario que contiene todos los heroes agrupados por una característica buscada
Parametros:
    - Lista(list): Lista de diccionarios de los heroes
    - Key(str): es la característica que se desea buscar
Retorno:
    Devuelve un diccionario con todos los heroes agrupados por la key
    '''
    diccionario = crear_diccionario_string_para_cada_key(lista, key_caracteristica) 
    for heroe in lista:
        for color in diccionario:
            if color == heroe[key_caracteristica] and heroe[key_caracteristica] != '':
                diccionario[color] += heroe['nombre']
    print(diccionario)

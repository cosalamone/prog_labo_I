from data_stark import lista_personajes

def mostrar_menu():
    opciones= f'''A- Mostrar todo los heroes de genero NB
    B- Mostrar el superhéroe más alto de género F
    C- Mostrar el superhéroe más alto de género M
    D- Mostrar el superhéroe más débil de género M
    E- Mostrar el superhéroe más débil de género NB
    F- Mostrar la fuerza promedio de los superhéroes de género NB
    G- Mostrar cuántos superhéroes tienen cada tipo de color de ojos.
    H- Mostrar cuántos superhéroes tienen cada tipo de color de pelo.
    I- Mostrar todos los superhéroes agrupados por color de ojos
    J- Mostrar todos los superhéroes agrupados por tipo de inteligencia
    '''
    print(opciones)

    respuesta = input('Ingrese la opcion deseada: ')

def agrupar_segun_genero(lista:list, genero_por_buscar:str)-> list:
    '''
    Crea una sublista, discriminada según genero. 
    Es necesario ingresar por parametro la lista en la que se buscará y el genero de interes.
    '''
    sh_genero = []

    for i in lista:
        genero = i['genero']

        if genero == genero_por_buscar:
            sh_genero.append(i)
    
    return sh_genero

# print(mostrar_segun_genero(lista_personajes, 'F'))


def mostrar_nombre_segun_genero(lista:list, genero_por_buscar:str):
    '''
    Muestra el nombre de los heroes según su genero.
    
    Parametros:
    - Lista(list): Lista de diccionarios de los heroes
    - Genero(str): 'F', 'M', 'NB'
    
    Retorno:
    Sin retorno. Imprime en consola los nombres de los heroes según su genero.
    '''
    lista_segun_genero = agrupar_segun_genero(lista, genero_por_buscar)

    for heroe in lista_segun_genero:
        nombre = heroe['nombre']

        mensaje = f'Los superheroes {genero_por_buscar} son:'        
        print(mensaje)
        print(nombre)



def parsear_datos(lista):
    '''
    Funcion para paresear los numeros enteros y flotantes de la lista
    '''
    for heroe in lista:
        heroe['fuerza'] = int(heroe['fuerza'])
        heroe['altura'] = float(heroe['altura'])
        heroe['peso'] = float(heroe['peso'])
    return lista


def encontrar_mayor_o_menor_caracteristica(lista:list, key: str, operador: str):
    '''
    Encuentra el valor flotante más alto o mas bajo según una determinada característica.
    Debe indicarse la lista sobre la cual trabajará, la característica en string y el operador: mayor o menor, tambien en string
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

#print(encontrar_mayor_o_menor_caracteristica(lista_personajes, 'altura', 'menor'))

def agrupar_personajes_segun_mayor_o_menor_caracteristica(lista: list, contador, key)->list:
    '''
    '''
    lista = parsear_datos(lista)

    lista_agrupada = []

    for heroe in lista:
        caracteristica_buscada = heroe[key]
        if contador == caracteristica_buscada:
            lista_agrupada.append(heroe)
    return lista_agrupada

#print(agrupar_personajes_segun_mayor_o_menor_caracteristica(lista_personajes, encontrar_mayor_o_menor_caracteristica(lista_personajes, 'altura', 'menor'), 'altura' ))

def crear_contadores_para_cada_key(lista:list, key):
    '''
    Crea y retorna un diccionario, donde cada key se inicializa como un contador en 0.
    Por parametro debe indicarse la lista sobre la cual se obtendrá la key.
    '''
    diccionario = {}

    for elemento in lista:
        key_a_buscar = (elemento[key]).lower()
        #key_a_buscar = key_a_buscar.lower()
        if key_a_buscar not in diccionario:
            diccionario[key_a_buscar] = 0  # agrego key color_ojos y la inicializo en 0  (valor)

    return diccionario


#print(crear_contadores_para_cada_key(lista_personajes, 'color_pelo'))


def contador_de_coincidencias(lista, diccionario, key): 
    '''
    En base  al diccionario recibido y a la key, recorre una lista para buscar coincidencias y sumar 1 en dicha key
    '''

    for elemento in lista:
        coincidencias = (elemento[key]).lower()
        diccionario[coincidencias] += 1

    return diccionario

#print(contador_de_coincidencias(lista_personajes, crear_contadores_para_cada_key(lista_personajes, 'color_pelo'), 'color_pelo'))
        

# para color de pelo, no contemplar pelados ni sin especificar 


def mostrar_heroe_mas_alto(lista:list, genero: str):
    '''
    Muestra el nombre de los heroes de mayor altura según su genero.
    
    Parametros:
    - Lista(list): Lista de diccionarios de los heroes
    - Genero(str): 'F', 'M', 'NB'
    
    Retorno:
    Sin retorno. Imprime en consola los nombres de los heroes más altos según su genero.
    '''
    heroe_femenino = agrupar_segun_genero(lista, genero)
    heroe_mas_alto = encontrar_mayor_o_menor_caracteristica(heroe_femenino, 'altura', 'mayor')
    lista_heroes= agrupar_personajes_segun_mayor_o_menor_caracteristica(heroe_femenino, heroe_mas_alto, 'altura')

    if len(lista_heroes) == 1:
        mensaje = f'''El superheroe {genero} de mayor altura es:
{lista_heroes[0]['nombre']}
''' 
        print(mensaje)

    else:
        if len(lista_heroes) > 1:
            mensaje = f'Los superheroes {genero} de mayor altura son:'        
            print(mensaje)

            for heroe_femenino in lista_heroes:
                print(heroe_femenino['nombre'])
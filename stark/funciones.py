from data_stark import lista_personajes

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
    Imprime en consola una lista de nombres de personajes según en genero.
    Tanto la lista como el genero deben indicarse por parametro
    '''
    lista_segun_genero = agrupar_segun_genero(lista, genero_por_buscar)

    for heroe in lista_segun_genero:
        nombre = heroe['nombre']
        print(nombre)

def encontrar_mayor_o_menor_caracteristica_flotante(lista:list, key: str, operador: str)-> list:
    '''
    Encuentra el valor flotante más alto o mas bajo según una determinada característica.
    Debe indicarse la lista sobre la cual trabajará, la característica en string y el operador: mayor o menor, tambien en string
    '''
    contador = None

    for heroe in lista:
        caracteristica_buscada = float(heroe[key])

        if operador == 'mayor': 
            if contador == None or caracteristica_buscada > contador:
                contador = caracteristica_buscada
        else:
            if operador == 'menor':
                if contador == None or caracteristica_buscada < contador:
                    contador = caracteristica_buscada
        
    return(contador)

print(encontrar_mayor_o_menor_caracteristica_flotante(lista_personajes, 'altura', 'menor'))

def agrupar_personajes_segun_mayor_o_menor_caracteristica_flotante(lista: list, contador:float, key):
    lista_agrupada = []

    for heroe in lista:
        caracteristica_buscada = float(heroe[key])
        if contador == caracteristica_buscada:
            lista_agrupada.append(heroe)
    return lista_agrupada

print(agrupar_personajes_segun_mayor_o_menor_caracteristica_flotante(lista_personajes, encontrar_mayor_o_menor_caracteristica_flotante(lista_personajes, 'altura', 'menor'), 'altura' ))

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
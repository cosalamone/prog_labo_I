from data_stark import lista_personajes
import re

# 1.1
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

    nombre = re.sub('the', '', nombre)

    filtrado = re.findall('[a-zA-Z]+', nombre)

    iniciales = ''.join([inicial[0].upper() + '.' for inicial in filtrado])

    return iniciales


#1.2
def obtener_dato_formato(dato:str):
    '''
Brief:
    Recibe un dato por parametro, lo pasa a minuscula y tranforma en formato snake_case.
    Valida que el dato recibido sea en str. De no serlo y ocurrir un error retorna Falso

Parametros:
    dato: str

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

def stark_imprimir_nombre_con_iniciales(heroe: dict):
    '''
Brief:
    Imprime el nombre de un heroe en formato snake_case. Iniciando con un asterisco '*', luego de un espacio le sigue el nombre, con un espacio al final. Por último, entre parentesis se encuentan  las iniciales en mayusculas, cada una seguida de un punto '.'.

Parametros:
    heroe: diccionario

Retorno:
    Devolverá True en caso de haber finalizado con éxito o False en caso de que haya ocurrido un error

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


# 1.4
def stark_imprimir_nombres_con_iniciales(lista_heroes: list):
    '''
Brief:
    Recorre una lista e imprime los nombres en formato snake_case. 
    Inicia con un asterisco '*', luego de un espacio le sigue el nombre, con un espacio al final. Por último, entre parentesis se encuentan  las iniciales en mayusculas, cada una seguida de un punto '.'.

Parametros:
    lista_heroe: lista

Retorno:
    Retornara True si salió todo bien y False si ocurrió algún error
    '''

    if type(lista_heroes) == list and len(lista_heroes) > 0:
        for heroe in lista_heroes:
            stark_imprimir_nombre_con_iniciales(heroe)
            boleano = True
    else:
        boleano = False
    return boleano


#2.1
def generar_codigo_heroe(heroe: dict, id: int):
    '''
Brief:
Genera un codigo para un heroe. Tendrá el formato GENERO-X00…000ID
En caso  que sea un heroe de género M el código comenzará en 1, si es F en 2 y si es NB en 0.
Validará que el género no se encuentre vacío y este dentro de los valores esperados (F NB M)
Parametros:
    diccionario de un héroe
    id (int)
Retorno:
    De no pasar las validaciones retornar N/A. En caso de verificarse
correctamente retornar el código generado.
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


#2.2
def stark_generar_codigos_heroes(lista_heroes: list):
    '''
Brief:
    Iterar la lista de personajes e imprime iniciando con un * el nombre del heroe en snake_case, las iniciales entre parentesis, una | y luego el código del heroe. 
    Ej: nombre_heroe (N.H.) | F-20000004
    Finaliza indicando la cantidad de códigos que se asignaron
Parametros:
    lista_heroes: lista
Retorno:
    Retorna la lista de nombres de heroes con codigos y el total de codigos generados, si salió todo correctamente o  False sihubo algun error
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

# 3.1
def sanitizar_entero(numero_str:str):
    '''
Brief:
    Analiza el string recibido y determinar si es un número entero positivo. 

Parametros:
    numero_str: string
Retorno:
    Si es un entero positivo, lo retorna convertido en entero
    Si contiene carácteres no numéricos retornar -1
    Si el número es negativo se deberá retornar un -2
    Si ocurren otros errores que no permiten convertirlo a entero entonces se deberá retornar -3
'''
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


# 3.2

def sanitizar_flotante(numero_str:str): 
    '''
Brief:
    Analiza el string recibido y determinar si es un número flotante positivo. 

Parametros:
    numero_str: string

Retorno:
    Si es un flotante positivo, lo retorna convertido en flotante
    Si contiene carácteres no numéricos retornar -1
    Si el número es negativo se deberá retornar un -2
    Si ocurren otros errores que no permiten convertirlo a entero entonces se deberá retornar -3
'''
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

# 3.3                     
def sanitizar_string(valor_str: str, valor_por_defecto = '-'):
    '''
Brief:
    Analiza el string recibido y determinar si es un número entero positivo. 

Parametros:
valor_str: string -> representa el texto a validar
●valor_por_defecto: string | es opcional

Retorno:
    En caso de encontra números: “N/A”
    Si es un string, lo retorna convertido en minusculas
    
'''
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

# 3.4
def sanitizar_dato(heroe: dict, clave:str, tipo_dato: str):
    '''
Brief:

Parametros:
    heroe: diccionario
    clave: string del dato a sanitizar. Ej: peso
    tipo_dato: string del tipo de dato a sanitizar: 'string', 'entero' y 'flotante'
Retorno:
    True en caso de haber sanitizado algún dato. False en caso contrario.
'''
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


# 3.5
def stark_normalizar_datos(lista_heroes: list):
    '''
Brief:
    Recorrer la lista de héroes y sanitizar los valores de las claves: altura, peso, color_ojos, color_pelo, fuerza e inteligencia
Parametros:
    lista_heroes: list
Retorno:
    No retorna
'''
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


# 4.1
def stark_imprimir_indice_nombre(lista_heroes):
    '''
Brief:

Parametros:
    heroe: diccionario
Retorno:

'''
    indice_nombres = ''
    for heroe in lista_heroes:
        nombre:str = heroe['nombre']
        nombre_sin_the = re.sub('the ', '', nombre)
        nombre_reemplazado = nombre_sin_the.replace(' ', '-')
        indice_nombres += f'{nombre_reemplazado}-'
    print(indice_nombres) 

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

# generar_separador('*',7)


# 5.2

def generar_encabezado(titulo: str):
    titulo_mayus = titulo.upper()
    separador = generar_separador('*', 50, False)

    respuesta = f'{separador}\n{titulo_mayus} \n{separador}'

    return respuesta

# print(generar_encabezado('Tituli'))

# 5.3 

def imprimir_ficha_heroe(heroe: dict, indice:int):
    nombre = heroe['nombre']
    identidad = heroe['identidad']
    consultora = heroe['empresa']
    # codigo heroe
    altura = heroe['altura']
    peso = heroe['peso']
    fuerza = heroe['fuerza']
    color_ojos = heroe['color_ojos']
    color_pelo = heroe['color_pelo']

    # encabezado_principal = generar_encabezado('Principal')
    # encabezado_fisico = generar_encabezado('Fisico')
    # encabezado_señas = generar_encabezado('señas particulares')

    respuesta = f'''{generar_encabezado('Principal')}
NOMBRE DEL HÉROE: {obtener_dato_formato(nombre)} ({extraer_iniciales(nombre)})
IDENTIDAD SECRETA: {obtener_dato_formato(identidad)}
CONSULTORA: {obtener_dato_formato(consultora)}
CÓDIGO DE HÉROE: {generar_codigo_heroe(heroe, indice)}

{generar_encabezado('Fisico')}
ALTURA: {altura} cm.
PESO: {peso} kg.
FUERZA: {fuerza} N

{generar_encabezado('señas particulares')}
COLOR DE OJOS: {color_ojos}
COLOR DE PELO: {color_pelo}

'''
    

    print(respuesta)

# imprimir_ficha_heroe(lista_personajes[0])


# 5.5

def stark_navegar_fichas(lista_heroes:list):
    menu_fichas = True
    indice_inicial = 0
    indice = 0 
    imprimir_ficha_heroe(lista_heroes[indice_inicial],indice_inicial)
    opciones_menu = '''Por favor, ingrese una de las siguientes opciones:
[ 1 ] Ir a la izquierda 
[ 2 ] Ir a la derecha 
[ 3 ] Salir
'''
    opciones_repregunta_menu = '''Las opciones validas son:
[ 1 ] Ir a la izquierda 
[ 2 ] Ir a la derecha 
[ 3 ] Salir

'''
    
    while menu_fichas:
        opcion_seleccionada = input(opciones_menu)
        while int(opcion_seleccionada) != 1 and int(opcion_seleccionada) != 2 and int(opcion_seleccionada) != 3:
            opcion_seleccionada = input(opciones_repregunta_menu)
            
        if int(opcion_seleccionada) == 1:
            if indice_inicial == 0: 
                indice_inicial = None
                indice = len(lista_heroes) -1
                imprimir_ficha_heroe(lista_heroes[indice],indice)
            else:
                indice -= 1
                imprimir_ficha_heroe(lista_heroes[indice],indice)

        elif int(opcion_seleccionada) == 2:
            if indice == (len(lista_heroes)-1):
                indice = 0 
                imprimir_ficha_heroe(lista_heroes[indice], indice)
            else:
                indice = indice + 1
                imprimir_ficha_heroe(lista_heroes[indice], indice)

        elif int(opcion_seleccionada) == 3:
            menu_fichas = False

        
# stark_navegar_fichas(lista_personajes)

def imprimir_stark_generar_nombres_con_codigo(lista_heroe:list):

    indice = 0 
    respuesta = ''
    for heroe in lista_heroe:
        nombre = heroe['nombre']
        
        respuesta += f'{nombre} | {generar_codigo_heroe(heroe,indice)}\n'
        indice += 1
    print(respuesta) 
# 6

def stark_marvel_menu(lista_heroes:list):
    menu_running = True
    opciones_menu = '''Indique la seccion deseada:
1 - Imprimir la lista de nombres junto con sus iniciales
2 - Imprimir la lista de nombres y el código del mismo
3 - Normalizar datos
4 - Imprimir índice de nombres
5 - Navegar fichas
6 - Salir
'''
    opciones_repregunta_menu = 'Las opciones validas son del 1 al 6'

    while menu_running:
        opcion_seleccionada = int(input(opciones_menu))
        while opcion_seleccionada < 1 and opcion_seleccionada > 6:
            opcion_seleccionada = int(input(opciones_repregunta_menu))

        match opcion_seleccionada:
            case 1:
                stark_imprimir_nombres_con_iniciales(lista_personajes)

            case 2:
                imprimir_stark_generar_nombres_con_codigo(lista_personajes)

            case 3:
                stark_normalizar_datos(lista_personajes)

            case 4:
                stark_imprimir_indice_nombre(lista_personajes)

            case 5:
                stark_navegar_fichas(lista_personajes)

            case 6:
                menu_running = False







'''
Brief:

Parametros:
    heroe: diccionario
Retorno:

'''

from data_stark import lista_personajes


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
# print('Lista', lista_personajes, '\n')

# print('Lista normalizada ', stark_normalizar_datos(lista_personajes))

'''
1.1 Crear la función ”obtener_dato()” la cual recibirá por parámetro un diccionario el cual representara a un héroe y también recibirá un string que hace referencia a una “clave” del mismo
Validar siempre que el diccionario no esté vacío y que el mismo tenga una key llamada “nombre”.
Caso contrario la función retornara un False

'''

def obtener_dato(heroe:dict, key:str):
    for clave in heroe:
        if clave == key:
            dato = heroe[clave]
            break 
        else:
            dato = False
    return dato

#print (obtener_dato(lista_personajes[0], 'nombre'))

'''
1.2 Crear la función 'obtener_nombre' la cual recibirá por parámetro un diccionario el cual representara a un héroe y devolverá un string el cual contenga su nombre formateado de la siguiente manera:
Nombre: Howard the Duck
Validar siempre que el diccionario no este vacío y verificar 'nombre' . Caso contrario la función retornara un False
NOTA: Reutilizar la función creada en el punto anterior
'''

def obtener_nombre(heroe:dict)-> str:
    for clave in heroe:
        if clave == 'nombre':
            respuesta = f'Nombre: {heroe[clave]}'
    return respuesta

# print(obtener_nombre(lista_personajes[0]))


'''
2. Crear la función 'obtener_nombre_y_dato' la misma recibirá por parámetro un diccionario el cual representara a un héroe y una key (string) la cual representará el dato que se desea obtener.


La función deberá devolver un string el cual contenga el nombre y dato (key) del héroe a imprimir. El dato puede ser 'altura', 'fuerza', 'peso' O CUALQUIER OTRO DATO.


El string resultante debe estar formateado de la siguiente manera: (suponiendo que la key es fuerza)
Nombre: Venom | fuerza: 500
Validar siempre que la lista no este vacía. Caso contrario la función retornara un False
NOTA: Reutilizar las funciones del punto anterior
'''
# verifiqué que el dato bucado exista
def obtener_nombre_dato(heroe: dict, key:str)-> str:

    nombre = obtener_nombre(heroe)
    dato = obtener_dato(heroe, key)
    
    if dato != False:
        dato = f'{nombre} | {key}: {dato}'

    return dato

# print(obtener_nombre_dato(lista_personajes[0], 'fuerza'))

'''
3.1 Crear la función “obtener_maximo()” la cual recibirá como parámetro una lista y una key (string) la cual representará el dato al cual se le debe calcular su cantidad MÁXIMA.
Validar siempre que la lista no esté vacía y que el dato que está buscando sea un int o un float. Caso contrario la función retornara un False
En caso de que el dato que se está buscando en el diccionario es de tipo int o float retornar el mayor que haya encontrado en la búsqueda.

'''
def obtener_maximo(lista: list, key:str): 
    stark_normalizar_datos(lista)
    maximo = lista[0][key]
    for hereo in lista:
        if type(hereo[key]) == float or type(hereo[key]) == int:
            if  hereo[key] > maximo:
                maximo = hereo[key]
        else:
            maximo = False

    return maximo

# print(obtener_maximo(lista_personajes, 'nombre'))

'''
3.2 Crear la función “obtener_minimo()” la cual recibirá como parámetro una lista y una key (string) la cual representará el dato al cual se le debe calcular su cantidad MÍNIMA.
Validar siempre que la lista no esté vacía y que el dato que está buscando sea un int o un float. Caso contrario la función retornara un False
En caso de que el dato que se está buscando en el diccionario es de tipo int o float retornar el menor que haya encontrado en la búsqueda.
'''

def obtener_minimo(lista:list, key: str):
    stark_normalizar_datos(lista)
    minimo = lista[0][key]
    for hereo in lista:
        if type(hereo[key]) == float or type(hereo[key]) == int:
            if  hereo[key] < minimo:
                minimo = hereo[key]
        else:
            minimo = False

    return minimo

# print(obtener_minimo(lista_personajes, 'altura'))

'''

3.3 Crear la función 'obtener_dato_cantidad()' la cual recibira tres parámetros:
-La lista de héroes
-Un número que me indique el valor a buscar (puede ser la altura máxima, la altura mínima o cualquier otro dato)
-Un string que representa la key del dato a calcular, por ejemplo: ‘altura’, ‘peso’, ‘edad’, etc.
La función deberá retornar una lista con el héroe o los heroes que cumplan  con la condición pedida. Reutilizar las funciones hechas en los puntos 3.1 y 3.2
Ejemplo de llamada:
mayor_altura = obtener_maximo(lista_heroes,”altura”)
lista_heroes_max_altura = 'obtener_dato_cantidad(lista_heroes,mayor_altura,”altura”)
El objetivo de estás llamadas es obtener todos los superhéroes que tengan la altura correspondiente a la altura máxima, y la misma función me podria servir tanto como para altura menor, como la mayor o alguna altura que yo le especifique también.
'''
def obtener_dato_cantidad(lista: list, numero,  key:str):
    stark_normalizar_datos(lista) 
    lista_dato_según_cantidad = []
    for heroe in lista:
        if heroe[key] == numero:
            lista_dato_según_cantidad.append(heroe)
    return lista_dato_según_cantidad

# print(obtener_dato_cantidad(lista_personajes, obtener_minimo(lista_personajes, 'fuerza'),  'fuerza'))

'''
3.4 Crear la función 'stark_imprimir_heroes'  la cual recibirá un parametro:

La lista de héroes

Validar que la lista de héroes no esté vacía para realizar sus acciones, caso contrario no hará nada y retornara False
En caso de que la lista no este vacia imprimir la información completa de todos los heroes de la lista que se le pase
Ejemplo de llamada:
mas_pesado = obtener_maximo(lista_heroes,”peso”)
lista_mas_pesados = 'obtener_dato_cantidad(lista_heroes,mas_pesado ,”peso”)
stark_imprimir_heroes(lista_mas_pesados) -> Imprimo sólo los héroes más pesados
stark_imprimir_heroes(lista_heroes) -> Imprimo todos los héroes
'''
def stark_imprimir_heroes(lista:list):
    flag = False
    for hereo in lista:
        flag = True
        print(hereo)
    if flag == False:
        return flag

# stark_imprimir_heroes(obtener_dato_cantidad(lista_personajes, obtener_minimo(lista_personajes, 'fuerza'),  'fuerza'))
'''
4.1 Crear la función 'sumar_dato_heroe' la cual recibirá como parámetro una lista de héroes y un string que representara el dato/key de los héroes que se requiere sumar. Validar que cada héroe sea tipo diccionario y que no sea un diccionario vacío antes de hacer la suma. La función deberá retorna la suma de todos los datos según la key pasada por parámetro
'''
def sumar_dato_heroe(lista: list, key: str,): 
    stark_normalizar_datos(lista)
    suma = 0
    for heroe in lista: 
        if type(heroe) == dict:
            suma += heroe[key]
    return suma

print(sumar_dato_heroe(lista_personajes, 'peso'))

'''
4.2 Crear la función  ‘dividir’ la cual recibirá como parámetro dos números (dividendo y divisor). Se debe verificar si el divisor es 0,  en caso de serlo, retornar False, caso contrario realizar la división entre los parámetros y retornar el resultado
'''
def dividir(dividiendo, divisor):
    if divisor == 0:
        respuesta = False
    else:
        respuesta = dividiendo/divisor
    return respuesta

# print(dividir(10,0))
'''
4.3 Crear la función ‘calcular_promedio’ la cual recibirá como parámetro una lista de héroes y un string que representa el dato del héroe que se requiere calcular el promedio. La función debe retornar el promedio del dato pasado por parámetro

IMPORTANTE: hacer uso de las las funciones creadas en los puntos 4.1 y 4.2
'''
def calcular_promedio(lista:list, key: str):
    stark_normalizar_datos(lista)
    acumulador = sumar_dato_heroe(lista, key)
    contador = len(lista)

    respuesta = dividir(acumulador,contador)
    return respuesta

# print(calcular_promedio(lista_personajes, 'fuerza'))



'''
4.4 Crear la función ‘mostrar_promedio_dato’ la cual recibirá como parámetro una lista de héroes y un string que representa la clave del dato
Se debe validar que el dato que se encuentra en esa clave sea de tipo int o float. Caso contrario retornaria False
Se debe validar que la lista a manipular no esté vacía , en caso de que esté vacía se retornaria también False
'''

def mostrar_promedio_dato(lista: list, key:str): 
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
        

# mostrar_promedio_dato(lista_personajes, 'altura')


'''5.1 Crear la función "imprimir_menu" que imprima el menú de opciones por pantalla, el cual permite utilizar toda la funcionalidad ya programada.
'''
def imprimir_menu(): 
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

'''
    print(mensaje)

# imprimir_menu()
'''
5.2 Crear la función “validar_entero” la cual recibirá por parámetro un string de número el cual deberá verificar que sea sea un string conformado únicamente por dígitos. Retornara True en caso de serlo, False caso contrario
'''
def validar_enteros(string: str):
    if string.isdigit():
        valido = True
    else:
        valido = False
    return valido

# print(validar_enteros('123'))

'''
5.3 Crear la función 'stark_menu_principal' la cual se encargará de imprimir el menú de opciones y le pedirá al usuario que ingrese el número de una de las opciones elegidas y deberá validarlo. En caso de ser correcto dicho número, lo retornara casteado a int , caso contrario retorna False. Reutilizar las funciones del ejercicio 5.1 y 5.2
'''
def stark_menu_principal(): 
    imprimir_menu()
    opcion = input('Ingrese una de las opciones: ')
    validacion = validar_enteros(opcion)
    if validacion == True:
        opcion = int(opcion)
        if opcion < 1 or  opcion > 11:
            opcion = False
    return opcion 

# print(stark_menu_principal())


'''6.Crear la función 'stark_marvel_app' la cual recibirá por parámetro la lista de héroes y se encargará de la ejecución principal de nuestro programa.
Utilizar if/elif o match según prefiera. Debe informar por consola en caso de seleccionar una opción incorrecta y volver a pedir el dato al usuario. Reutilizar las funciones con prefijo 'stark_' donde crea correspondiente.
'''
def menu_obtener_nombre_nb(lista:list, key:str):
    stark_normalizar_datos(lista_personajes)
    mensaje = ""
    for heroe in lista:
        if heroe[key] == 'NB': 
            nombre = obtener_nombre(heroe)
            mensaje += f"{nombre}  \n"

    return mensaje
# print(menu_obtener_nombre_nb(lista_personajes, 'genero'))

def menu_por_genero_mas_alto(lista, keyGenero: str, keyAltura: str, gen):

    lista_filtrada = []
    for heroe in lista:
        if heroe[keyGenero] == gen:
            lista_filtrada.append(heroe)

    maximo = obtener_maximo(lista_filtrada, keyAltura)
    lista_maximos = obtener_dato_cantidad(lista_filtrada, maximo, keyAltura)
    for f in lista_maximos:
        print(f['nombre'])

def menu_por_genero_min_fuerza(lista, keyGenero: str, keyAltura: str, gen):
    lista_filtrada = []
    for heroe in lista:
        if heroe[keyGenero] == gen:
            lista_filtrada.append(heroe)

    minimo = obtener_minimo(lista_filtrada, keyAltura)
    lista_minimo = obtener_dato_cantidad(lista_filtrada, minimo, keyAltura)
    for f in lista_minimo:
        print(f['nombre'])

def menu_promedio_por_genero(lista, keyGenero: str, keyfuerza: str, gen):
    lista_filtrada = []
    for heroe in lista:
        if heroe[keyGenero] == gen:
            lista_filtrada.append(heroe)
    
    mostrar_promedio_dato(lista_filtrada, keyfuerza)
    
def stark_marvel_app(lista:list):
    opcion = stark_menu_principal()
    match opcion:
        case 1:
            stark_normalizar_datos(lista)
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
            pass
        case 9:
            pass
        case 10:
            pass
        case 11:
            pass

stark_marvel_app(lista_personajes)

'''7. Una vez realizadas y probadas las funciones resolver en un menú los siguientes puntos del desafio anterior.
A Normalizar datos (No se debe poder acceder a los otros puntos)
B Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género NB
C Recorrer la lista y determinar cuál es el superhéroe más alto de género F
D Recorrer la lista y determinar cuál es el superhéroe más alto de género M
E Recorrer la lista y determinar cuál es el superhéroe más débil de género M
F Recorrer la lista y determinar cuál es el superhéroe más débil de género NB
G Recorrer la lista y determinar la fuerza promedio de los  superhéroes de género NB
H Determinar cuántos superhéroes tienen cada tipo de color de ojos.
I Determinar cuántos superhéroes tienen cada tipo de color de pelo.
J Listar todos los superhéroes agrupados por color de ojos.
K Listar todos los superhéroes agrupados por tipo de inteligencia
'''


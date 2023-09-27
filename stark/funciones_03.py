from data_stark import lista_personajes


def stark_normalizar_datos(lista):
    '''
Brief:
    Funcion para normalizar los numeros enteros y flotantes de la lista

Parametros:
- Lista(lista)

Retorno:
    Lista con los datos numericos parseados a enteros o flotantes según corresponda
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

print(obtener_nombre(lista_personajes[0]))


'''
2. Crear la función 'obtener_nombre_y_dato' la misma recibirá por parámetro un diccionario el cual representara a un héroe y una key (string) la cual representará el dato que se desea obtener.


La función deberá devolver un string el cual contenga el nombre y dato (key) del héroe a imprimir. El dato puede ser 'altura', 'fuerza', 'peso' O CUALQUIER OTRO DATO.


El string resultante debe estar formateado de la siguiente manera: (suponiendo que la key es fuerza)
Nombre: Venom | fuerza: 500
Validar siempre que la lista no este vacía. Caso contrario la función retornara un False
NOTA: Reutilizar las funciones del punto anterior
'''
def obtener_nombre_dato(heroe: dict, key:str)-> str:
    nombre = obtener_nombre(heroe)
    dato = obtener_dato(heroe, key)

    respuesta = f'{nombre} | {key}: {dato}'

    return respuesta

print(obtener_nombre_dato(lista_personajes[0], 'fuerza'))

'''
3.1 Crear la función “obtener_maximo()” la cual recibirá como parámetro una lista y una key (string) la cual representará el dato al cual se le debe calcular su cantidad MÁXIMA.
Validar siempre que la lista no esté vacía y que el dato que está buscando sea un int o un float. Caso contrario la función retornara un False
En caso de que el dato que se está buscando en el diccionario es de tipo int o float retornar el mayor que haya encontrado en la búsqueda.




3.2 Crear la función “obtener_minimo()” la cual recibirá como parámetro una lista y una key (string) la cual representará el dato al cual se le debe calcular su cantidad MÍNIMA.
Validar siempre que la lista no esté vacía y que el dato que está buscando sea un int o un float. Caso contrario la función retornara un False
En caso de que el dato que se está buscando en el diccionario es de tipo int o float retornar el menor que haya encontrado en la búsqueda.

3.3 Crear la función 'obtener_dato_cantidad()' la cual recibira tres parámetros:


La lista de héroes
Un número que me indique el valor a buscar (puede ser la altura máxima, la altura mínima o cualquier otro dato)
Un string que representa la key del dato a calcular, por ejemplo: ‘altura’, ‘peso’, ‘edad’, etc.
La función deberá retornar una lista con el héroe o los heroes que cumplan  con la condición pedida. Reutilizar las funciones hechas en los puntos 3.1 y 3.2
Ejemplo de llamada:
mayor_altura = obtener_maximo(lista_heroes,”altura”)
lista_heroes_max_altura = 'obtener_dato_cantidad(lista_heroes,mayor_altura,”altura”)
El objetivo de estás llamadas es obtener todos los superhéroes que tengan la altura correspondiente a la altura máxima, y la misma función me podria servir tanto como para altura menor, como la mayor o alguna altura que yo le especifique también.

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


'''
4.1 Crear la función 'sumar_dato_heroe' la cual recibirá como parámetro una lista de héroes y un string que representara el dato/key de los héroes que se requiere sumar. Validar que cada héroe sea tipo diccionario y que no sea un diccionario vacío antes de hacer la suma. La función deberá retorna la suma de todos los datos según la key pasada por parámetro


4.2 Crear la función  ‘dividir’ la cual recibirá como parámetro dos números (dividendo y divisor). Se debe verificar si el divisor es 0,  en caso de serlo, retornar False, caso contrario realizar la división entre los parámetros y retornar el resultado


4.3 Crear la función ‘calcular_promedio’ la cual recibirá como parámetro una lista de héroes y un string que representa el dato del héroe que se requiere calcular el promedio. La función debe retornar el promedio del dato pasado por parámetro

IMPORTANTE: hacer uso de las las funciones creadas en los puntos 4.1 y 4.2

4.4 Crear la función ‘mostrar_promedio_dato’ la cual recibirá como parámetro una lista de héroes y un string que representa la clave del dato
Se debe validar que el dato que se encuentra en esa clave sea de tipo int o float. Caso contrario retornaria False
Se debe validar que la lista a manipular no esté vacía , en caso de que esté vacía se retornaria también False
'''


'''5.1 Crear la función "imprimir_menu" que imprima el menú de opciones por pantalla, el cual permite utilizar toda la funcionalidad ya programada.
5.2 Crear la función “validar_entero” la cual recibirá por parámetro un string de número el cual deberá verificar que sea sea un string conformado únicamente por dígitos. Retornara True en caso de serlo, False caso contrario


5.3 Crear la función 'stark_menu_principal' la cual se encargará de imprimir el menú de opciones y le pedirá al usuario que ingrese el número de una de las opciones elegidas y deberá validarlo. En caso de ser correcto dicho número, lo retornara casteado a int , caso contrario retorna False. Reutilizar las funciones del ejercicio 5.1 y 5.2


'''


'''6.Crear la función 'stark_marvel_app' la cual recibirá por parámetro la lista de héroes y se encargará de la ejecución principal de nuestro programa.
Utilizar if/elif o match según prefiera. Debe informar por consola en caso de seleccionar una opción incorrecta y volver a pedir el dato al usuario. Reutilizar las funciones con prefijo 'stark_' donde crea correspondiente.
'''


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


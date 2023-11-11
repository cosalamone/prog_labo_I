'''
########### ABRIR UN ARCHIVO ###########

archivo = open(path_archivo, modo)

######## MODOS DE APERTURA #############
Los mas usados e importarntes para la cursada son:
* r:solo lectura
* w:solo escritura - sobreescribe lo que estaba
* a:anexa informacion al archivo

la fx open devuelve un archivo, un objeto file, que se usa para 
llamar a otros metodos asociados con el archivo

luego se debe cerrar el archivo
archivo.close()

###### leer el archivo #######
texto = archivo.read()

luego si o si hay que cerrarlo. 

###### READLINES: genera una lista, separando x cada linea ######
archivo = open(path_archivo, modo)
lista_archivo = archivo.readlines()
for linea in lista_archivos: // tambien se puede hacer el for directo desde el archivo
    print(linea, end="")
archivo.close()


####### ESCRIBIR: el archivo debe ser abierto en formato para escribir  ######

* OPCION A: WRITE
archivo = open('archivo.txt', 'w') // Sobreescribiendo
archivo.write('Primer linea de texto/n')
archivo.write('segunda linea/n')
archivo.write('tercera linea/n')
archivo.close()


* OPCION B: WROTELINES
archivo = open('archivo.txt', 'w') // Sobreescribiendo
lineas_texto = ['Primer linea de texto/n',

'segunda linea/n',
'tercera linea/n']
archivo.writelines(lineas_texto)
archivo.close()


####### ADMINISTRADOR DE CONTEXTO: WITH ############
La sentencia with para abrir archivos en Python y dejar que el intérprete se
encargue de cerrar el mismo.

with open('archivo.txt', 'r+') as archivo:
    for linea in archivo:
        print(linea, end="")


        

##########################################################
                ESCRIBIR EN JSON
##########################################################

###### DUMP ######
import json

data = {}
data['clientes'] = []
data['clientes'].append({ 'nombre': 'Juan', 'edad':
27})
data['clientes'].append({ 'nombre': 'Ana', 'edad': 26})

with open('data.json', 'w') as file:
    json.dump(data, file, indent=4, ensure_ascii=False )


    
##########################################################
                LEER EN JSON
##########################################################

##### LOAD #### 
import json

with open('data.json') as file:
    data = json.load(file)


'''


def parsear_csv(nombre_archivo:str, ):
    '''
Brief:
    Abre el archivo indicado por parametro. Lo hace sólo en modo lectura
Parametros:
    nombre_archivo: str
Retorno:
    Retorna un string con la informacion del archivo.
'''
    lista_completa = []
    # archivo = open(nombre_archivo, 'r')
    with  open(nombre_archivo, 'r') as archivo:
        for linea in archivo:
            lista = linea.split(',')
            video = {}
            video['titulo'] = lista[0]
            video['views'] = int(lista[1])
            video['length'] = int(lista[2])
            video['img_url'] = lista[3]
            video['url'] = lista[4]
            video['date'] = lista[5]

            lista_completa.append(video)

    # archivo.close()
    return lista_completa
    

parsear_csv('C:/Users/RodrigoVazquez/Documents/REPOSITORIOS/prog_labo_I/data_archivos.csv')



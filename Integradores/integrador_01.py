'''
Salamone Constanza

Ejercicio Integrador 01
La división de higiene está trabajando en un control de stock para productos sanitarios.
Debemos realizar la carga de 5 (cinco) productos de prevención de contagio, de cada una debe
obtener los siguientes datos:
1. El tipo (validar "barbijo", "jabón" o "alcohol")
2. El precio: (validar entre 100 y 300)
3. La cantidad de unidades ( no puede ser 0 ni negativo y no debe superar las 1000
unidades)
4. La marca y el Fabricante.

Se debe informar lo siguiente:
A. Del más caro de los barbijos, la cantidad de unidades y el fabricante.
B. Del ítem con más unidades, el fabricante.
C. Cuántas unidades de jabones hay en total.

'''
listado = []
contador = 0
acumulador = 0

for i in range(5):

    tipo = input('Por favor, ingrese el tipo de producto ("barbijo", "jabón" o "alcohol"): ')
    while tipo != "barbijo" and tipo != "jabón"  and tipo != "alcohol":
        tipo = input('Por favor, verificar que el producto ingresado sea: "barbijo", "jabón" o "alcohol"  ')
    
    precio = int(input('Por favor, ingrese el precio: '))
    while precio < 100 or precio > 300:
        precio = int(input('Por favor, el precio debe ser entre 100 y 300: '))

    cantidad = int(input('Ingrese la cantidad de unidades: '))
    while cantidad < 0 or cantidad > 100:
        cantidad = int(input('Sólo se pueden ingresar entre 0 y 100 unidades: '))

    marca = input('Por favor, ingrese la marca: ')

    fabricante = input('Por favor, ingrese el fabricante del producto: ')

    listado.append({'tipo': tipo, 'precio': precio, 'cantidad': cantidad, 'marca':marca, 'fabricante':fabricante})

mensaje = ""


#######A. Del más caro de los barbijos, la cantidad de unidades y el fabricante. ########
mayor_precio = 0
cantidad_unidades = ""
lista_fabricantes =  ""

for i in range(len(listado)):
    if listado[i]['tipo'] == 'barbijo':
        if listado[i]['precio'] > mayor_precio:
            mayor_precio = listado[i]['precio']


for i in range(len(listado)):
    if listado[i]['precio'] == mayor_precio:
        cantidad_unidades += f"{listado[i]['cantidad']} "
        lista_fabricantes += f"{listado[i]['fabricante']} "

mensaje += f'El barbijo más caro tiene {cantidad_unidades} unidades y su fabricante es {lista_fabricantes} '
print(mensaje)

######## B. Del ítem (tipo) con más unidades, el fabricante. #########
mayor_cantidad_unidades = 0
tipo_mayor_cant_unid = ''
fabricantes_mayor_unidades = ""
mensaje_dos = ''

for i in range(len(listado)):   
    if listado[i]['cantidad'] > mayor_cantidad_unidades:
        mayor_cantidad_unidades = listado[i]['cantidad']
        tipo_mayor_cant_unid = listado[i]['tipo']

for i in range(len(listado)):   
    if listado[i]['cantidad'] == mayor_cantidad_unidades:
        fabricantes_mayor_unidades += f"{listado[i]['fabricante']} "

mensaje_dos = f"El fabricante del item con más unidades es: {fabricantes_mayor_unidades}"

print(mensaje_dos)

######### C. Cuántas unidades de jabones hay en total. ########
cantidad_jabones = 0
for i in range(len(listado)):
    if listado[i]['tipo'] == 'jabón':
        cantidad_jabones += listado[i]['cantidad']

mensaje = f"La cantidad de jabones totales que hay es de {cantidad_jabones}" 
print(mensaje)
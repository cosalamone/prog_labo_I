'''
################################ PROGRAMACION ORIENTADA A OBJETOS ##########################################

### CLASES ###
* CREAR LA CLASE: la plantilla/molde
class Personaje: (Se escruben en CapitalizedWord)
        tipo = "Personajes"
    def __init__(self,id,nombre,apellido,edad) -> None:
    self.id = id
    self.nombre = nombre
    self.apellido = apellido
    self.edad = edad


* INSTANCIAR LA CLASE: DARLE VIDA A LA CLASE

personaje_A = Personaje(0, 'Marta', 'Stuart', 18)
personaje_b = Personaje(1, 'Juan', 'Perez', 33)

CADA CLASE TIENE SU ARCHIVO


El objeto es la instancia de la clase


### ATRIBUTOS PRIVADOS __ ###
Doble guión bajo antes del nombre indica que es un
atributo privado. Lo cual establece que solo puede
ser accedido por esa clase y sus herederas.

### ATRUBUTOS PROTEGIDOS _ ###
Un guión bajo antes del nombre indica que es un
atributo protegido. Lo cual establece que solo
puede ser accedido por esa clase y sus herederas.

### PROPERTY ###
La función integrada que permitirá interceptar 
la escritura, lectura, borrado de los
atributos y además nos permitirá incorporar una
documentación sobre los mismos.

Getter: Se encargará de interceptar la lectura del
atributo.

Setter : Se encarga de interceptar cuando se
escribe. Para el Setter tiene que estar el Getter


### METODOS DUNDER ###
son los métodos de una clase que tienen
dos subrayados de prefijo y sufijo en el nombre.

Hay muchos y se pueden usar para personalizar el
comportamiento de los objetos en Python


### __str__ ###
Crea una representación del objeto que
tenga significado para las personas

### __len__ ###
En el caso de que el objeto tenga una número de
elementos, como es el caso, podríamos usar la
función len para obtener este.

class Personaje:
    def __init__(self,id,nombre,apellido,edad) -> None:
        self.id = id # crea un atributo id y le asigna el valor id.
        self.nombre = nombre
        self._cantidad = 1
        def __len__(self) -> str:
        return self._cantidad


### __getitem__ ###
Si se desea que los usuarios puedan leer los
elementos mediante el uso de corchetes es necesario
implementar el método __getitem__ en la clase.



### __setitem__ ###
es el complemento del método anterior.
En este caso es necesario pasar dos parámetros
adicionales, la posición y el valor a reemplazar.

### __contains__ ###
sobrecarga el operador in retornando un
booleano.


### __delitem__ ###
__delitem__ sobrecarga el operador del
__delitem__

class Personaje:
    def __init__(self,id,nombre,apellido,edad) -> None:
        self.id = id # crea un atributo id y le asigna el valor id.
        self.nombre = nombre
        self._lista= [id,nombre,apellido,edad]
        def __delitem__(self,index):
        return self._lista.pop(index)

    personaje_A = Personaje(0,'Marty','McFly', 18)
    del personaje_A[1]
    print(personaje_A[1]) # McFly


### __iter__ ###
__iter__ permite que el objeto sea iterable, lo que
habilita a usarlo por ejemplo en bucles tipo for.


class Personaje:
    def __init__(self,id,nombre,apellido,edad) -> None:
        self.id = id # crea un atributo id y le asigna el valor id.
        self.nombre = nombre
        self._lista= [id,nombre,apellido,edad]
        def __iter__(self):
        for index in range(len(self._lista)):
        yield self._lista[index]

personaje_A = Personaje(0,'Marty','McFly', 18)
for i in personaje_A:
print(i)


### OPERADORES DE COMPARACION ###
Método Operador Método Operador
__lt__ <            __ne__ !=
__le__ <=           __gt__ >
__eq__ ==           __ge__ >=


### HEREDAR DE OTRA CLASE ###
La herencia es el proceso por el cual una clase
adquiere los atributos y métodos de otra.
Para heredar solo se requiere colocar el nombre de la
clase padre entre paréntesis.


'''
class Persona:
    def __init__(self,dni,nombre,apellido, edad) -> None:
        self.dni: int = dni
        self.__nombre:str = nombre
        self.apellido:str  = apellido
        self.edad:int = edad

    @property
    def nombre(self): #Getter
        return self.__nombre # privado
    
    @nombre.setter #Setter
    def nombre(self, nombre):
        self.__nombre = nombre

    def descripcion(self) -> str:
        return '{0}-{1}'.format(self.nombre,self.apellido)  
    
    def __str__(self) -> str:
        return '{0}-{1}'.format(self.nombre,self.apellido)
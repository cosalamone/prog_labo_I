from persona import Persona

persona_1 = Persona(123,'maria','fernandez', 44)

print(persona_1.nombre)
print(persona_1.descripcion())

'''
def iniciales(nombre_heroe):
    if not nombre_heroe:         
        return 'N/A'          
    palabras = nombre_heroe      
    if 'the' in palabras:         
        palabras.remove('the')      

    inicial = ''.split(palabras[0])
    
    iniciales = ''.join([palabras[0].upper() for palabra[0] in palabras])     
    return inicial  

print(iniciales('maria'))
'''
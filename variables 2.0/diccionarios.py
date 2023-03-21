#las listas no pueden ser claves y usamos frozenset para meter conjuntos 
diccionario ={frozenset(['flor', 'sol']):'ajaja'}

#creando diccionarios con fromkeys() valor por defecto:none
diccionario = dict.fromkeys(['nombre', 'apellido'])

#creando diccionarios con fromkeys() cambinado el valor por defecto a "no se "
diccionario = dict.fromkeys(['nombre','apellido'], 'no se')


print(diccionario)
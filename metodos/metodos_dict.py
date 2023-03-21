diccionario = {
    'nombre':'flor',
    'apellido':'ibanez',
    'subs': 500000
}

#nos devielve un objeto dict_item
claves = diccionario.keys()

#obtenindo un elemnto con get() (si no encuentra nada el programa continua )
valor_de_jjojoj = diccionario.get('jjojoj')
print('todo ok')

#elimando todo del diccionario
#diccionario.clear()

#elimando un elemento del deiccionario
diccionario.pop('nombre',"subs")
                
#obteniendo un elemnto dict_items iterable
diccionario_iterble = diccionario.items()

print(diccionario_iterble)

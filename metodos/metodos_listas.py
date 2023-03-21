
#creando una lista con list()
lista = list([65,68,868,True,26,False])

#devuelve la cantidad de elementos de la lista 
cantidad_elementos = len(lista)

#agregando un elemneto a la lista 
lista.append(65)

#agregando un elemento a la lista en un indice especifico
lista.insert(2,'bla bla')

#agregando varios elementos a la lista
lista.extend([False,2030])

#eliminando un elemento de la lista (por su indice)
lista.pop(3) # -1 para eliminar el ultimo, -2 para eliminar el anteultimo, y asi sucesivamente

#removiendo un elemento de la lista por su valor
lista.remove(68)

#eliminando todos los elementos
#lista.clear()

#ordenando la lista de forma acendente (si usamos el parametro reverse=True lo ordena en reversa)
lista.sort()

#invirtiendo los elemntos de una lista 
lista.reverse()

#verificamos si un elementose encuentra en la lista
elemento_encontrado = lista.index(68)
                                
print(elemento_encontrado)
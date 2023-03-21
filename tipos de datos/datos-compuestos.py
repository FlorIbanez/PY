#creando una lista (se pueden modificar)
lista = ['flor','pablo',True,1.68]

#creando una tupla (no se pueden modificar)
tupla = ('flor','pablo',True,1.68)

#esto es valido 
lista[3]='m&m'

#esto no es valido 
tupla[3]='m&m'

#creando un conjuto (set) (no se accede a elementos por indice, no almacena datos duplicados)
conjunto = {'flor','pablo',True,1.68}
#print(conjunto[3]-> no se puede aceder al elemnto

#creando un diccionario(dict)(la estructura es key : value y separamos por comas)
diccionario ={
    "nombre":"flor",
    "canal":"florfi",
    "todo_ok":True,
    "altura":1.68,
    "dato_duplicado":"flor"
    
}
print(diccionario['altura'])




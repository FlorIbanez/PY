animales = {'gatp','perro','loro','cocodrilo'}
numeros ={52,16,14,72}

#recorriendo la conjuto animales
for animal in animales:
    print(f'Ahora la variable animal es igual a: {animal}')
    
#recorriendo la conjuto de numeros y multiplicando cada valor por 10
for numero in numeros:
    resultado = numero * 10
    print(resultado)

#iterando dos conjutos del mismo tama;o al mismo tiempo
for numero,animal in zip(animales,numeros):
    print(f'recorriendo conjuto1: {numero}')
    print(f'recorriendo conjuto2: {animal}')
    


#forma correcta de recorrer una conjuto con su indice 
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1] 
    print(f'el indice es: {indice} y el valor es: {valor}')

#usando el for/else
for numero in numeros:
    print(f'ejecutando el ultimo bucle, valor actual: {numero}')
else:
    print('el bucle termino') 
      
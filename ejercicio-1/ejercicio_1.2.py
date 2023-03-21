#le pedimos al usuario que diga una frase (o varias )
frase = input("decime un frase y te calculo cuanto tardarias si tuvieras que decirlas: ")

#creamos una lista con todas las palabras de la frase (se separan cada vez que haya un espacio en blanco )
palabras_separadas = frase.split(' ')

#usamos len() para ver la cantidad de elementos que hay en una lista 
cantidad_de_palabras = len(palabras_separadas)

#en caso que tarde mas de un minuto en decirlo, le decimos que pare un poco
if cantidad_de_palabras > 120:
    print("Para flaco tampoco te pedi un testamento ")

#calculamos cuanto tendria en decir las palabras y se lo decimos 
print(f'Dijiste {cantidad_de_palabras} palabras, y tardarias {cantidad_de_palabras/2} segundos en decirlo')
print(f'Dalto lo diria en {cantidad_de_palabras *100 // 2/1.3 /100} segundos')    
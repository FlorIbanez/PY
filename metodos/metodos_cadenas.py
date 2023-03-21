cadena1 = 'hola Flor, como estas?'
cadena2 = 'Bienvenida'

#convierte a mayusculas
mayusc = cadena1.upper()

#convierte a minusculas
minusc = cadena1.lower()

#primer letra en mayuscula 
primer_letra_mayusc = cadena1.capitalize()

#buscamos una cadena en otra cadena, si no hay coincidencia devuelve -1 
busqueda_find = cadena1.find("a")

#buscamos una cadena en otra cadena, si no hay conicidencia lanza una exepcion 
busqueda_index = cadena1.index("F")

#si es numerico, devolvemos true, sino devolvemos false
es_numerico = cadena1.isnumeric()

#si es alfa numerico devolvemos true, sino devolvemos false (el espacio no va, asi devuelve true)
es_alfanumerico = cadena1.isalpha()

#contamos las coincidencias de una cadena dentro de otra cadena, devuelve la cantidad de coincidencias 
contar_coincidencia = cadena1.count("o")

#contamos cuantos caracteres tiene una cadena (len NO es un metodo es una funcion)
contar_caracteres = len(cadena1)

#verificamos si una cadena empieza con otra cadena dada, si es esa devuelve true
empieza_con = cadena1.startswith("H")

#verificamos si una cadena termina con otra cadena dada, si es esa devuelve true
termina_con = cadena1.endswith("H")

#remplaza un pedazo de la cadena dada, por otra dada
cadena_nueva = cadena1.replace(','," ")

#separar cadenas con la cadena que le pasemos 
cadena_separada = cadena1.split(',')

print(cadena_separada[0])

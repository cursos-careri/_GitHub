#-------------------------------------------------------------------------------
# DICCIONARIOS
#
# Notas creadas y editadas por: Sergio Fco. Hernández Machuca
# Xalapa, Veracruz, México
# 2023 - Julio
#
# La información proviene de diversas fuentes de internet, principalmente los 
# sitios oficiales del lenguaje Python (https://www.python.org) y Micropython 
# (https://micropython.org).
#-------------------------------------------------------------------------------

'''
Otro tipo de dato útil integrado en Python es el diccionario. A veces se 
encuentran diccionarios en otros idiomas. como "memorias asociativas" o 
"arreglos asociativos". A diferencia de las secuencias, que son
indexados por un rango de números, los diccionarios están indexados por claves, 
que pueden ser cualquier tipo inmutable; cadenas y números siempre pueden ser 
claves. Se pueden usar tuplas como claves si contienen solo cadenas, números o 
tuplas; si la tupla contiene cualquier objeto mutable, ya sea directa o 
indirectamente, no se puede usar como clave.
No se puede usar listas como claves, ya que las listas se pueden modificar, en 
su lugar usando asignacioones al índice, asignaciones de 'slicing'' o métodos 
como 'append()' y 'extend()'.

Es mejor pensar en un diccionario como un conjunto de claves: pares de valores, 
con el requisito de que las claves sean únicas (dentro de un diccionario). 
Un par de llaves crea un diccionario vacío: {}.

Colocando una lista separada por comas de clave:valor entre llaves agrega pares 
iniciales de clave:valor al diccionario; esta es también la forma en que se 
escriben los diccionarios en la salida.

Las operaciones principales en un diccionario son almacenar un valor con alguna 
clave y extraer el valor dada una clave. También es posible eliminar una pareja
clave:valor con el estatuto 'del'. Si almacena elementos usando una clave que 
ya está en uso, el valor anterior asociado con esa clave se olvida. Es un error
extraer un valor usando una clave inexistente.

Ejecutar 'list(d)' en un diccionario devuelve una lista de todas las claves 
utilizadas en el diccionario, en orden de inserción (si desea ordenarlo, 
simplemente use 'sorted(d)' en cambio). Para verificar si una clave está en el
diccionario, use el estatuto 'in' con la palabra clave.

Aquí hay un pequeño ejemplo usando un diccionario:
'''
print ("-----------------------------------------------------------")
# Definición de diccionario
tel = {'jack': 4098, 'sape': 4139}
print(tel)
# --> {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print(tel)
# --> {'jack': 4098, 'sape': 4139, 'guido': 4127}
print(tel['jack'])
#--> 4098
del tel['sape']
tel['irv'] = 4127
print(tel)
# --> {'jack': 4098, 'guido': 4127, 'irv': 4127}
print(list(tel))
# --> ['jack', 'guido', 'irv']
print(sorted(tel))
# --> ['guido', 'irv', 'jack']
print('guido' in tel)
# --> True
print('jack' not in tel)
# --> False
print()

# El constructor 'dict()' crea diccionarios directamente a partir de secuencias 
# de pares clave-valor:

print(dict([('sape', 4139), ('guido', 4127), ('jack', 4098)]))
# --> {'sape': 4139, 'guido': 4127, 'jack': 4098}

# Además, la construcción por comprensión a partir de 'dic' se pueden usar 
# para crear diccionarios a partir de expresiones arbitrarias de clave y valor:

print({x: x**2 for x in (2, 4, 6)})
# --> {2: 4, 4: 16, 6: 36}

# When the keys are simple strings, it is sometimes easier to specify pairs 
# using keyword arguments:

# Cuando las claves son cadenas simples, a veces es más fácil especificar 
# pares usando argumentos de palabras clave:

print(dict(sape=4139, guido=4127, jack=4098))
# --> {'sape': 4139, 'guido': 4127, 'jack': 4098}
print()

# ------------------------------
# Técnicas de Lazos o Ciclos

# Al recorrer los diccionarios, la clave y el valor correspondiente se 
# pueden recuperar al mismo tiempo usando el método 'items()'.
# Un ejemplo:

# Creación del diccionario:
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)
# --> gallahad the pure
# --> robin the brave

# Al recorrer una secuencia, el índice de posición y el valor correspondiente
# se puede recuperar al mismo tiempo usando la función 'enumerate()'.

for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

# --> 0 tic
# -->  tac
# --> 2 toe
print()

# Para recorrer dos o más secuencias al mismo tiempo, las entradas pueden 
# ser emparejadas con la función 'zip()'.

# Diccionarios:
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
# Recorrido:
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))

# --> What is your name?  It is lancelot.
# --> What is your quest?  It is the holy grail.
# --> What is your favorite color?  It is blue.
print()

# To loop over a sequence in reverse, first specify the sequence in a forward 
# direction and then call the reversed() function.

# Para recorrer una secuencia en reversa, primero especifique la secuencia en 
# avance hacia adelante y luego llame a la función 'reversed()' .

for i in reversed(range(1, 10, 2)):
    print(i)

# --> 9
# --> 7
# --> 5
# --> 3
print()

# Para recorrer una secuencia en orden, se usa la función 'sorted()' que
# devuelve una nueva lista ordenada sin modificar la fuente.

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for i in sorted(basket):
    print(i)

# --> apple
# --> apple
# --> banana
# --> orange
# --> orange
# --> pear
print()

# El uso del estatuto 'set()' en una secuencia elimina los elementos duplicados.
# El uso de 'sorted()' en combinación con 'set()' sobre una secuencia es una 
# forma idiomática de pasar por elementos únicos de la secuencia en orden.

# Diccionario:
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']

for f in sorted(set(basket)):
    print(f)

# --> apple
# --> banana
# --> orange
# --> pear
print()

# A veces es tentador cambiar una lista mientras la recorre; sin embargo, 
# a menudo es más simple y seguro crear una nueva lista.

import math

# Diccionario
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
# Diccionario que se creará:
filtered_data = []

for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)

print(filtered_data)
# --> [56.2, 51.7, 55.3, 52.5, 47.8]
print()

#******************************************************************************
'''
Más sobre Condiciones

Las condiciones utilizadas en las declaraciones 'while' e 'if' pueden contener 
cualquier operador, no solo comparaciones.

Los operadores de comparación 'in' y 'not in' son pruebas de pertenencia que 
determinan si un valor está en (o no en) un contenedor. Los operadores 'is' y 
'not is' compararan si dos objetos son realmente el mismo objeto. Todas los 
operadores de comparación tienen la misma prioridad, que es inferior a la de 
todos los operadores numéricos.

Las comparaciones se pueden encadenar. Por ejemplo, a < b == c comprueba si a 
es menor que b y además b es igual a c.

Las comparaciones pueden combinarse usando los operadores booleanos 'and' y 
'or', y el resultado de una comparación (o de cualquier otra expresión booleana) 
puede ser negado con 'not'. Estos tienen prioridades más bajas que los operadores 
de comparación; entre ellos entre ellos, 'not' tiene la prioridad más alta y 
'or' la más baja, de modo que iF A and not B o C es equivalente a 
(A and (not B)) or C. Como siempre, los paréntesis se pueden usar para expresar 
la composición deseada.

Los operadores booleanos 'and' y 'or' son los llamados operadores de
cortocircuito: (short-circuit) sus argumentos se evalúan de izquierda a derecha, 
y la evaluación se detiene tan pronto como se determina el resultado. Por 
ejemplo, si A and C son verdaderas pero B es falsa, A and B and C no evalúa la
expresión C. Cuando se usa como un valor general y no como un valor booleano, 
el valor de retorno de un operador de cortocircuito es el último argumento 
evaluado.

Es posible asignar el resultado de una comparación u otro booleano
expresión a una variable. Por ejemplo,
'''
# Aignación de cadenas
string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
# Operación
non_null = string1 or string2 or string3
print(non_null)
# --> 'Trondheim'
print()

# Tenga en cuenta que en Python, a diferencia de C, la asignación dentro de las 
# expresiones debe hacerse explícitamente con el operador morsa :=. Esto evita 
# una clase común de problemas encontrado en programas C: escribir = en una 
# expresión cuando se pretendía ==.

#------------------------------------------------------------------------------

'''
Comparación de secuencias y otros tipos

Los objetos de secuencia normalmente se pueden comparar con otros objetos 
con el mismo tipo de secuencia. La comparación utiliza el ordenamiento 
lexicográfico: primero los primeros dos elementos se comparan, y si difieren,
esto determina el resultado de la comparación; si son iguales, se comparan los 
dos elementos siguientes, y así sucesivamente, hasta que se agote cualquiera 
de las secuencias. Si dos elementos a compararse son en si mismos
secuencias del mismo tipo, la comparación lexicográfica se realiza
recursivamente. Si todos los elementos de dos secuencias son iguales, las 
secuencias son consideradas iguales. Si una secuencia es una subsecuencia 
inicial de la otra, la secuencia más corta es la más pequeña (menor). La 
ordenación lexicográfica para cadenas utiliza el número de punto de código
Unicode para ordenar caracteres individuales.

Algunos ejemplos de comparaciones entre secuencias del mismo tipo:
'''
# Todas las comparaciones son verdaderas.
print((1, 2, 3)              < (1, 2, 4))
print([1, 2, 3]              < [1, 2, 4])
print('ABC' < 'C' < 'Pascal' < 'Python')
print((1, 2, 3, 4)           < (1, 2, 4))
print((1, 2)                 < (1, 2, -1))
print((1, 2, 3)             == (1.0, 2.0, 3.0))
print((1, 2, ('aa', 'ab'))   < (1, 2, ('abc', 'a'), 4))

print()
'''
Tenga en cuenta que comparar objetos de diferentes tipos con < o > es legal 
siempre que los objetos tengan métodos de comparación apropiados. Por ejemplo,
los tipos numéricos mixtos se comparan según su valor numérico, por lo que
0 es igual a 0.0, Etc. De lo contrario, en lugar de proporcionar un orden 
arbitrario, el intérprete generará una excepción 'TypeError'.
'''
#-------------------------------------------------------------------------------
# Loops. Recorrido de elementos de un Diccionario
#
# Notas creadas y editadas por: Sergio Fco. Hernández Machuca
# Xalapa, Veracruz, México
# 2023 - Julio
#
# La información proviene de diversas fuentes de internet, principalmente los 
# sitios oficiales del lenguaje Python (https://www.python.org) y Micropython 
# (https://micropython.org).
#-------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# Es esta sección se revisa el recorrido con lazos ('loops') de un Diccionario.
#------------------------------------------------------------------------------
# --------------------------
# Técnicas de Lazos o Ciclos
# --------------------------
# Al recorrer los diccionarios, la clave y el valor correspondiente se pueden
# recuperar al mismo tiempo usando el método 'items()'.  Un ejemplo:

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
# --> 1 tac
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
print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.")
print()
#******************************************************************************
#------------------------
# Ejercicio con 'range()'
#------------------------

# Creamos un rango de números
range_0_a_50_5_etapas = range(0,50,5)
# Esto nada más imprimiría el estatuto, el objeto, no la secuencia requerida
print(range_0_a_50_5_etapas)
# --> range(0, 50, 5)
print("---------------")

# Para imprimir los elementos individuales requeriríamos un 'loop'
# Aquí definimos una variable arbitraria, 'numero', que servirá como índice,
# que servirá para identificar los elementos del rango.

for numero in range_0_a_50_5_etapas:
    print(numero)
'''
0
5
10
15
20
25
30
35
40
45
'''
print()

#-------------------------------------------------
# Para listas, ya revisamos, se hace algo similar.
#-------------------------------------------------

# Se define una lista
lista_de_letras = ["a", "b", "c", "d", "e", "f", "g"]
# se despliegan las letra
for letra in lista_de_letras:
    print(letra)
'''
a
b
c
d
e
f
g
'''
print()

# -----------------------------------------------------
# Para tuplas también se vió anteriormente, esto es así
# -----------------------------------------------------

# Definimos la tupla
tupla = { "a", 21, "casa", 23.5, "e", 2, "g" }

for item in tupla:
    print(item)
'''
2
g
21
23.5
casa
a
e
'''
print()
# -------------------------
# Para diccionarios, es así
# -------------------------
esp32_datos = {"Creador": "espressif", "Tipo": "uC", "CPU": "Tensilica",
               "RAM": "520K", "Potencia": "3.3 Volts", "Núcleos": "2"}

# Para solo ver las 'claves'
for llave, valor in esp32_datos.items():
    print (llave)
'''
Creador
Tipo
CPU
RAM
Potencia
Núcleos
'''
print()

# Para ver la información solamente
for llave, valor in esp32_datos.items():
    print (valor)
'''
espressif
uC
Tensilica
520K
3.3 Volts
2
'''
print()

# Para ver todo
for llave, valor in esp32_datos.items():
    print (llave, valor)
'''
Creador espressif
Tipo uC
CPU Tensilica
RAM 520K
Potencia 3.3 Volts
Núcleos 2
'''
print()
print("---[FIN de esta SECCIÓN]---")
print()
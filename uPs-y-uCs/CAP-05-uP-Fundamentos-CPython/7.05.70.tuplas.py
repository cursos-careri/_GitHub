#-------------------------------------------------------------------------------
# Tuplas.
#
# Notas creadas y editadas por: Sergio Fco. Hernández Machuca
# Xalapa, Veracruz, México
# 2023 - Julio
#
# La información proviene de diversas fuentes de internet, principalmente los 
# sitios oficiales del lenguaje Python (https://www.python.org) y Micropython 
# (https://micropython.org).
#-------------------------------------------------------------------------------

# Se revisó que las listas y las cadenas tienen muchas propiedades comunes, 
# como la indexación y operaciones de rebanado ('slicing'). Los anteriores 
# son dos ejemplos de tipos de datos que operan con secuencias. 
# Dado que Python es un lenguaje en evolución, se pueden agregar otros tipos de
# datos de secuencia. También hay otro estándar. 
# Tipo de datos de secuencia: la tupla.

# Una tupla consta de una serie de valores separados por comas, por ejemplo

t = 12345, 54321, 'hello!'
print(t[0])
print()
# --> 12345
print(t)
print()
# --> (12345, 54321, 'hello!')

# Las tuplas pueden estar anidadas: 
u = t, (1, 2, 3, 4, 5)
print(u)
print()
# --> ((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))

# Las Tuplas son inmutables:
'''
t[0] = 88888
# genera lo siguiente:
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
'''
# Pero las Tuplas pueden contener objetos mutables:
v = ([1, 2, 3], [3, 2, 1])
print(v)
# --> ([1, 2, 3], [3, 2, 1])

# En la salida las tuplas siempre se encierran entre paréntesis, para que las
# tuplas anidadas se interpreten correctamente; formalmente se pueden ingresar 
# con o sin paréntesis, aunque a menudo los paréntesis son necesarios de todos
# modos (si la tupla es parte de una expresión más grande). No es posible 
# asignar algún valor a los elementos individuales de una tupla, sin embargo,
# es posible crear tuplas que contengan objetos mutables, como listas.

# Aunque las tuplas pueden parecer similares a las listas, a menudo se usan en 
# diferentes situaciones y para diferentes propósitos. Las tuplas son 
# inmutables y, por lo general, contienen una secuencia heterogénea de 
# elementos a los que se accede mediante desempaquetado o indexación 
# (o incluso por atributo en el caso de tuplas con nombre). 
# Las listas son mutables y sus elementos suelen ser homogéneos y 
# habitualmente se accede a ellos iterando sobre la lista.

# Un problema especial es la construcción de tuplas que contienen 0 o 1 
# elemento: la sintaxis tiene algunas peculiaridades adicionales para 
# acomodarlos. Las tuplas vacías se construyen con un par de paréntesis 
# vacíos; una tupla con un elemento se construye siguiendo un valor con una 
# coma (no es suficiente encerrar un solo valor entre paréntesis). 
# Esto es feo, pero efectivo. Por ejemplo:

print("------------------------------")
empty = ()
singleton = 'hello',    # <-- Nótese la coma al final
print(len(empty))
# --> 0
print(len(singleton))
# --> 1
print(singleton)
# --> ('hello',)
print()

# La declaración t = 12345, 54321, '¡hola!' es un ejemplo de empaquetado de 
# tuplas: los valores 12345, 54321 y '¡hola!' se empaquetan en una tupla. 
# La operación inversa también es posible:

t = 12345, 54321, '¡hola!'
x, y, z = t
# Ahora las variables individuales tienen los elementos de la tupla:
print(x)
print(y)
print(z)
print()

#------------------------------------------------------------------------------
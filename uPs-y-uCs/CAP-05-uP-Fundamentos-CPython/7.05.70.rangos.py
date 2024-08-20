#-------------------------------------------------------------------------------
# Rangos [función range()]
#
# Notas creadas y editadas por: Sergio Fco. Hernández Machuca
# Xalapa, Veracruz, México
# 2023 - Julio
#
# La información proviene de diversas fuentes de internet, principalmente los 
# sitios oficiales del lenguaje Python (https://www.python.org) y Micropython 
# (https://micropython.org).
#-------------------------------------------------------------------------------

# La función 'range()' es útil para iterar (contar, secuenciar, rastrear)
# a través de una secuencia de números algo, una lista, una tupla, una
# cadena, por ejemplo. Genera una progresión aritmética

for i in range(5):
    print(i)

print()
'''
# El resultado es:
0
1
2
3
4
'''

# El punto final dado nunca forma parte de la secuencia generada.
# Por ejemplo, range(10) genera diez valores, los índices normales
# para recorrer una secuencia de longitud 10.
# Es posible iniciar la secuencia con un valor distinto a cero, o
# usar un incremento diferente a uno, incluso puede ser negativo.
# Al incremento se le llama a veces las etapas del conteo.

a = list(range(5, 10))
print(a)
# --> [5, 6, 7, 8, 9]
b = list(range(0, 10, 3))
print(b)
# --> [0, 3, 6, 9]
c = list(range(-10, -100, -30))
print(c)
# --> [-10, -40, -70]
print()

# Para iterar sobre los índices de una secuencia, se puede combinar la
# secuencia ('range(a)') y la longitud ('len(a)'):

a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])
# --> Genera lo siguiente:
'''
0 Mary
1 had
2 a
3 little
4 lamb
'''
print()

# En muchos casos el objeto regresado por 'range()' se comporta como una
# lista, pero no lo es, es un objeto que regresa los elementos sucesivos
# de una secuencia deseada cuando se itera sobre ella.
# No crea una lista, esto ahorra espacio de memoria.

# Establecemos que un objeto es iterable, es decir, adecuado para funciones
# y constructores que esperan algo de lo cual puedan obtener elementos
# sucesivos hasta agotarlos.
# Anteriormente se ejercitó el uso del constructor 'for' para iterar una
# secuencia, ootro ejemplo, ahora de una función que puede usar elementos
# iterables, es lo siguiente: 

a = sum(range(4))  # 0 + 1 + 2 + 3
print(a)
# --> 6
print()

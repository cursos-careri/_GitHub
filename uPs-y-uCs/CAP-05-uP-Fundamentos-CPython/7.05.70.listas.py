#-------------------------------------------------------------------------------
# Listas
#
# Notas creadas y editadas por: Sergio Fco. Hernández Machuca
# Xalapa, Veracruz, México
# 2023 - Julio
#
# La información proviene de diversas fuentes de internet, principalmente los 
# sitios oficiales del lenguaje Python (https://www.python.org) y Micropython 
# (https://micropython.org).
#-------------------------------------------------------------------------------

# Definición:
squares = [1, 4, 9, 16, 25]
print(squares)
print("-----------------")

# El indexamiento regresa el item (artículo), señalado
print(squares[0])
print(squares[-1])       # Apunta al final
print(squares[-2:])      # El "rebanado", 'slicing', regresa una nueva lista
print(squares[-3:])
print(squares[-4:])      # ¿Cuántos elementos desde el final?

print()
# Todas las operaciones de 'slice' regresan una nueva lista conteniendo
# los elementos requeridos. Esto significa que la siguiente rebanada regresa una
# copia de la misma lista
print(squares[:])
print()

# Las listas también soportan operaciones como concatenación:
print(squares + [36, 49, 64, 81, 100])

# A diferencia de las cadenas ('strings'), las cuales son inmutables, las listas
# son un tipo mutable, pueden cambiar los valores de sus elementos.
# Es posible cambiar su contenido.

cubes = [1, 8, 27, 65, 125]   
print(cubes)                 # ¡Algo está mal aquí!
print(4 ** 3)                # El cubo de 4 es 64, no 65
cubes[3] = 64                # Se reemplaza el valor erróneo
print(cubes)                 # Listo
print()

# También se pueden agregar nuevos elementos al final de la lista empleando el 
# método 'append()':

cubes.append(216)     # Se agrega el cubo de 6 
cubes.append(7 ** 3)  # y de 7
print(cubes)

# También es posible asignar elementos a rebanadas ('slices'), y esto puede 
# hasta cambiar el tamaño de la lista o incluso limpiarla por completo.
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters)
# --> ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# Reemplazar algunos valores:
letters[2:5] = ['C', 'D', 'E']
print(letters)
# --> ['a', 'b', 'C', 'D', 'E', 'f', 'g']
# Ahora removerlos:
letters[2:5] = []
print(letters)
# --> ['a', 'b', 'f', 'g']
# Limpiar la lista reemplazando todos los elementos por una lista vacía:
letters[:] = []
print(letters)
# --> []
print()

# La función interconstruida 'len()' también se aplica a listas:
letters = ['a', 'b', 'c', 'd']
print(len(letters))
# --> 4
print()

# Es posible anidar (crear listas que contengan otras listas), por ejemplo:
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x)
# --> [['a', 'b', 'c'], [1, 2, 3]]
print(x[0])
# --> ['a', 'b', 'c']
print(x[0][1])
# --> 'b'
print()

# Más cuestiones sobre Listas

#========================================================================
''' 
El tipo de datos de lista tiene algunos métodos más. 
Aquí están todos los métodos de objetos de lista:

--> list.append(x)
Agregua un elemento al final de la lista.
Equivalente a lo siguiente: a[len(a):] = [x].

--> list.extend(iterable)
Amplía la lista agregando los elementos del iterable (algo con 'range()').
Equivale a lo siguiente: a[len(a):] = iterable.

--> list.insert(i, x)
Inserta un elemento en una posición determinada. El primer argumento es el 
índice del elemento antes del cual insertar, por lo que a.insert(0, x) 
inserta la 'x' al principio de la lista, y a.insert(len(a), x) es equivalente 
a: a.append( X).

--> list.remove(x)
Elimina el primer elemento de la lista cuyo valor es igual a x.
Genera un 'ValueError' si no existe tal elemento.

--> list.pop([i])
Remueve el artículo en la posición dada en la lista (por el índice 'i') y 
lo devuelve. Si no se especifica un índice, a.pop() elimina y devuelve el 
último elemento en la lista. Los corchetes alrededor de la 'i' en la firma del
método denotan que el parámetro es opcional, no que deba escribir corchetes en
esa posición. Esta notación con frecuencia se utiliza en las bibliotecas de
Python.

--> list.clear()
Elimina todos los elementos de la lista. Equivalente a esto: del a[:].

--> list.index(x[, start[, end]])
Devuelve el índice (basado en cero) en la lista del primer elemento cuyo valor 
es igual a 'x'. Genera un 'ValueError' si no existe tal elemento.
Los argumentos opcionales 'start' y 'end' se interpretan como en la notación 
de cortes ('slicing') y se utilizan para limitar la búsqueda a una subsecuencia
particular de la lista. El índice devuelto se calcula en relación con el 
comienzo de la secuencia completa en lugar del argumento de inicio.

--> list.count(x)
Devuelve el número de veces que 'x' aparece en la lista.

--> list.sort(*, key=None, reverse=False)
Ordena los elementos de la lista en su lugar (los argumentos se pueden usar para
#  ordenar una personalización, vea la función 'sorted()' para su explicación).

--> list.reverse()
Invierte los elementos de la lista en su lugar.

--> list.copy()
Devuelve una copia superficial de la lista. Equivalente a: a[:].
'''

#  Un ejemplo que utiliza la mayoría de los métodos antes descritos es el 
# siguiente:

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print(fruits.count('apple'))
# --> 2
print(fruits.count('tangerine'))
# --> 0
print(fruits.index('banana'))
# --> 3
print(fruits.index('banana', 4))  # Encuentra el siguiente nombre 'banana' 
                                  # comenzando en la posición 4
# --> 6
fruits.reverse()
print(fruits)
# --> ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']
fruits.append('grape')
print(fruits)
# --> ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']
fruits.sort()
print(fruits)
# --> ['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']
print(fruits.pop())
# --> 'pear'
print(fruits)       # Verifique que se extrajo lo que se emergió (POP)
print()
# --> ['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange']

'''
Es posible que haya notado que métodos como 'insert', 'remove' o 'sort' que 
solo modifican la lista, no tienen valor de retorno impreso; devuelven el 
valor predeterminado Ninguno ('None'). Este es un principio de diseño para 
todas las estructuras de datos mutables en Python.

Otra cosa que puede notar es que no todos los datos se pueden ordenar o 
comparar. Por ejemplo, [Ninguno, 'hola', 10] no se ordena porque los enteros 
no se pueden comparar con cadenas y Ninguno no se puede comparar con otros tipos. 
También, hay algunos tipos que no tienen una relación de orden definida.
Por ejemplo, 3+4j < 5+7j no es una comparación válida
'''

'''
Uso de listas como Pilas ('Stacks')
Los métodos de lista facilitan mucho el uso de una lista como una pila 
('stack'), donde el último elemento agregado es el primer elemento recuperado 
("último en entrar, primero en salir"). A esta estructura se le denominan LIFO:
(“last-in, first-out”).
Para agregar un elemento a la parte superior de la pila, se emplea 'append()'. 
Para recuperar un elemento desde la parte superior de la pila, se usa 'pop()'
sin un índice explícito. Por ejemplo:
'''

stack = [3, 4, 5]
stack.append(6)
stack.append(7)
print(stack)
# --> [3, 4, 5, 6, 7]
print(stack.pop())
# --> 7
print(stack)
# --> [3, 4, 5, 6]
print(stack.pop())
# --> 6
print(stack.pop())
# --> 5
print(stack)
# --> [3, 4]
print()

'''
Uso de listas como Colas ('Queues')
También es posible usar una lista como una cola ('queues'), donde el primer 
elemento agregado es el primer elemento recuperado ("primero en entrar, 
primero en salir"). A esta estructura se le denomina FIFO (“first-in, 
first-out”). Aun cuando es posible emplear este esquema para implementar colas, 
las listas son eficientes para este propósito. Mientras se agrega y aparece
desde el final de la lista los resultados son rápidos, hacer inserciones o 
'pops' desde el principio de una lista es lento (porque todos los demás 
elementos tienen que ser desplazados por uno).

Para implementar una cola (queue), use 'collections.deque', que fue diseñado 
para tener agregados ('push') y retribuciones rápidas ('pop') desde ambos 
extremos. Por ejemplo:
'''

from collections import deque          # Biblioteca usada
queue = deque(["Eric", "John", "Michael"])
print(queue)
# -->
queue.append("Terry")
print(queue)                  # Terry llega
# --> deque(['Eric', 'John', 'Michael', 'Terry'])
queue.append("Graham")
print(queue)                  # Graham se agrega
# --> deque(['Eric', 'John', 'Michael', 'Terry', 'Graham'])
print(queue.popleft())        # El primero en arribar ahora se va
# --> 'Eric'
print(queue.popleft())        # El segundo en arribar ahora se va
# --> 'John'
print(queue)                  # El resto de la cola en el orden que llegaron
# --> (deque(['Michael', 'Terry', 'Graham']))
print()

'''
Lista creadas por comprensión
La comprensión de listas proporciona una forma concisa de crear listas. 
Aplicaciones comunes se pueden usar para crear nuevas listas, donde cada 
elemento es el resultado de operaciones aplicadas a cada miembro de otra 
secuencia o iterable, o para crear un subsecuencia de aquellos elementos que 
satisfacen una determinada condición.

Por ejemplo, supongamos que queremos crear una lista de cuadrados, como:
'''

squares = []
for x in range(10):
    squares.append(x**2)

print(squares)
# --> [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

'''
Tenga en cuenta que esto crea (o sobrescribe) una variable llamada 'x' que aún
existe después de que se completa el bucle. Podemos calcular la lista de 
cuadrados sin ningún efectos secundarios usando:
'''
squares = list(map(lambda x: x**2, range(10)))
print(squares)
# --> [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# lo que es lo mismo de: 
squares = [x**2 for x in range(10)]
print(squares)
# --> [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print("-----------------------------------")
print()
# --> 
# lo cual es más conciso .

'''
Una lista por comprensión consta de corchetes que contienen una expresión 
seguida por una cláusula 'for', seguida de cero o más cláusulas 'for' o 'if'.
El resultado será un nuevo lista resultante de evaluar la expresión en el 
contexto de cláusulas 'for' e 'if' que le siguen. Por ejemplo, esta lista 
'listcomp' combina los elementos de dos listas si no son iguales:
'''

print([(x, y) for x in [1,2,3] for y in [3,1,4] if x != y])
# -- [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

# Que es equivalente a:

combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs.append((x, y))

print(combs)
# --> [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

# Observe cómo el orden de las declaraciones 'for' e 'if' es el mismo en ambos
# fragmentos.
# Si la expresión es una tupla (por ejemplo, la (x, y) en el ejemplo anterior),
# ésta debe estar entre paréntesis.

vec = [-4, -2, 0, 2, 4]
# Crea una nueva lista con los valores doblados
print([x*2 for x in vec])
# --> [-8, -4, 0, 4, 8]
# Filtra la lista para excluir números negativos
print([x for x in vec if x >= 0])
# --> [0, 2, 4]
# Aplica una función a todos los elementos
print([abs(x) for x in vec])
# --> [4, 2, 0, 2, 4]
# Llama un método para cada elemento
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
print([weapon.strip() for weapon in freshfruit])
# --> ['banana', 'loganberry', 'passion fruit']
# Crea una lista de tuplas-2 como (número, cuadrado)
print([(x, x**2) for x in range(6)])
# --> [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]
# La tupla debe estar entre paréntesis, de lo contrario se genera un error como:

'''
[x, x**2 for x in range(6)]
  File "<stdin>", line 1
    [x, x**2 for x in range(6)]
     ^^^^^^^
SyntaxError: did you forget parentheses around the comprehension target?
'''

# flatten a list using a listcomp with two 'for'
# Aplana ('flatten') una lista usando un listcomp con dos 'for'
vec = [[1,2,3], [4,5,6], [7,8,9]]
print([num for elem in vec for num in elem])
# --> [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Las comprensiones de lista pueden contener expresiones complejas y funciones 
# anidadas:

from math import pi
print([str(round(pi, i)) for i in range(1, 6)])
# --> ['3.1', '3.14', '3.142', '3.1416', '3.14159']

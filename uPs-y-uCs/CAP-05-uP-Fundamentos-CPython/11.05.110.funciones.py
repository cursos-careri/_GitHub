#-------------------------------------------------------------------------------
# Definición de Funciones
#
# Notas creadas y editadas por: Sergio Fco. Hernández Machuca
# Xalapa, Veracruz, México
# 2023 - Julio
#
# La información proviene de diversas fuentes de internet, principalmente los 
# sitios oficiales del lenguaje Python (https://www.python.org) y Micropython 
# (https://micropython.org).
#-------------------------------------------------------------------------------

# Podemos crear una función que escriba la serie de Fibonacci en un límite 
# arbitrario:

def fib(n):    # Escribe la serie de Fibonacci hasta un número arbitrario 'n'
    """Imprime una serie de Fibonacci hasta el 'n'"""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

# Una llamada a la función recientemente definida:
print(fib(2000))
# --> 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597
print()

# La palabra clave 'def' introduce una definición de función. Debe ir seguido 
# del nombre de la función y la lista entre paréntesis de parámetros formales. 
# Las declaraciones que forman el cuerpo de La función comienza en la siguiente 
# línea y debe estar indentada.

# La primera declaración del cuerpo de la función puede ser opcionalmente una 
# literal de cadena; esta cadena literal es la cadena de documentación de la 
# función, o 'docstring'. (Más sobre 'docstrings' puede ser encontrado en la 
# sección Cadenas de Documentación). Hay herramientas que usan cadenas de 
# documentación para producir automáticamente documentación en línea o 
# impresa, o permitir que el usuario interactúe para navegar a través del 
# código; es una buena práctica incluir docstrings en el código que escribe, 
# trate de hacerlo un hábito.

# La ejecución de una función introduce una nueva tabla de símbolos utilizada
# para las variables locales de la función. Más precisamente, todas las 
# asignaciones de variables en una función almacenan el valor en el tabla de 
# símbolos locales; mientras que las referencias a variables primero buscan en
# la tabla de símbolos local, luego en las tablas de símbolos locales de las 
# funciones envolventes, luego en la tabla de símbolos globales y finalmente 
# en la tabla de nombres integrados. 
# 
# Así, variables globales y variables de las funciones envolventes no se les 
# puede asignar directamente un valor dentro de una función (a menos que, 
# para las variables globales, nombrada en una instrucción global o, para 
# variables de funciones envolventes, nombrada en una declaración no local
# declaración), aunque pueden ser referenciados.

# Los parámetros reales (argumentos) para una llamada de función se introducen
# en la tabla de símbolos local de la función llamada cuando ésta es invocada; 
# por lo tanto, los argumentos se pasan usando 'llamada por valor' (donde el 
# valor es siempre una referencia de objeto, no el valor del objeto). Cuando 
# un función llama a otra función, o se llama a sí misma recursivamente, se 
# crea una nueva tabla de símbolos local creada para esa llamada.

# Una definición de función, asocia el nombre de la función con el objeto de la
# función en la tabla de símbolos actual. El intérprete reconoce el objeto al 
# que apunta por el nombre definido por la función definida por el usuario.
# Otros nombres también pueden apuntar a ese mismo objeto de función y también 
# se pueden usar para acceder a la función:

print(fib)
# --> <function fib at 10042ed0>
print()
f = fib
print(f(100))
# --> 0 1 1 2 3 5 8 13 21 34 55 89
print()

# Viniendo de otros idiomas, se puede objetar que 'fib' no es una función sino
# un procedimiento ya que no devuelve un valor. De hecho, incluso las funciones 
# sin declaración de retorno no devuelve un valor, aunque sea bastante aburrido. 
# Este valor se llama 'None'' (es un nombre integrado). Escribir el valor 
# 'None' normalmente es suprimido por el intérprete si fuera el único valor 
# escrito. Puede verlo si realmente se quiere usar print():

fib(0)
print(fib(0))
# --> None

# Es sencillo escribir una función que devuelva una lista de los números de la
# serie de Fibonacci, en lugar de imprimirlo:

def fib2(n):  # Regresa una serie de Fibonacci hasta el número 'n'
    """Devuelve una lista que contiene la serie de Fibonacci hasta 'n'"""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)    # Revisar abajo
        a, b = b, a+b
    return result

f100 = fib2(100)    # Llamada 
print(f100)         # Escritura del resultado 
# --> [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# Este ejemplo, como de costumbre, demuestra algunas características nuevas de
# Python:

# La declaración de devolución (retorno, 'return') regresa con un valor de una 
# función. Regresar de una función sin expresión argumento devuelve 'None'. 
# Si se cae durante la ejecución hasta al final de una función, también se 
# devuelve 'None'.
# La declaración 'result.append(a)' llama a un método de la lista del 
# resultado del objeto.
# Un método es una función que ‘pertenece’ a un objeto y es llamada 
# 'obj.methodname', donde 'obj' es algún objeto (este puede ser una expresión),
# y 'methodname' es el nombre de un método que está definido por el tipo de 
# objeto. 
# Diferentes tipos definen diferentes métodos. Los métodos de diferentes tipos 
# pueden tener el mismo nombre sin causar ambigüedad.
# (Es posible definir su propios tipos de objetos y métodos, utilizando clases, 
# consulte Clases) El método 'append()' que se muestra en el ejemplo está
# definido para objetos de lista; agrega un nuevo elemento al final de la lista.
# En este ejemplo es equivalente a resultado = resultado + [a], pero más 
# eficiente.

#-------------------------------------
# Más sobre la definición de funciones
#-------------------------------------

# También es posible definir funciones con un número variable de argumentos. 
# Hay tres formas, las cuales se pueden combinar.

# Valores de argumento predeterminados
# ------------------------------------

# La forma más útil es especificar un valor predeterminado para uno o más 
# argumentos. Esto crea un función que se puede llamar con menos argumentos de 
# los que está definido para permitir. Por ejemplo:

def ask_ok(prompt, retries=4, reminder='Por favor trate de nuevo'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('Respuesta de usuario inválida')
        print(reminder)

# Esta función se puede llamar de varias maneras:

# Dando solo el argumento obligatorio, por ejemplo:
#   ask_ok('¿De verdad quieres salir?')

# Dando uno de los argumentos opcionales, por ejemplo:
#   ask_ok('¿Está bien sobrescribir el archivo?', 2)

# o incluso dando todos los argumentos:
#   ask_ok('¿Está bien sobrescribir el archivo?', 2, 'Vamos, ¡solo sí o no!')

# Este ejemplo también presenta la palabra clave 'in'. Esto prueba si un 
# secuencia contiene un cierto valor.

# Los valores predeterminados se evalúan en el punto de definición de la 
# función en el alcance o ámbito ('scope') de la función, de modo que:

i = 5

def f(arg=i):
    print(arg)

i = 6
print(f())
# --> 5
print()

# Advertencia importante: el valor predeterminado se evalúa solo una vez. Esto 
# marca la diferencia cuando el valor predeterminado es un objeto mutable, 
# como una lista, un diccionario o instancias de la mayoría de las clases.
# Por ejemplo, la siguiente función acumula los argumentos que se le pasan en 
# posteriores llamadas:

def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))
# Esto imprimirá: 
# --> [1]
# --> [1, 2]
# --> [1, 2, 3]
print()

# Si no desea que el valor predeterminado se comparta entre llamadas 
# posteriores, puede escribir la función de esta manera:

def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

#-----------------------------
# Argumentos de palabras clave
#-----------------------------

# Las funciones también se pueden llamar usando argumentos de palabras clave de
# la forma 'kwarg=valor'. Por ejemplo, la siguiente función:

def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")

# Acepta un argumento requerido (voltaje) y tres argumentos opcionales (estado,
# acción y tipo). Esta función se puede llamar de cualquiera de las siguientes 
# maneras:

parrot(1000)                                          # 1 argumento posicional 
parrot(voltage=1000)                                  # 1 argumento 'keyword'
parrot(voltage=1000000, action='VOOOOOM')             # 2 argumentos 'keyword'
parrot(action='VOOOOOM', voltage=1000000)             # 2 argumentos 'keyword'
parrot('a million', 'bereft of life', 'jump')         # 3 argumentos posicionales 
parrot('a thousand', state='pushing up the daisies')  # 1 posicional, 1 'keyword'
print(" ")

# Pero todas las siguientes llamadas no serían válidas:
'''
parrot()                     # Falta argumento requerido
parrot(voltage=5.0, 'dead')  # Argumento 'non-keyword' después de argumento 'keyword'
parrot(110, voltage=220)     # Valores duplicados para el mismo argumento 
parrot(actor='John Cleese')  # Argumento 'keyword' desconocido
'''

# En una llamada de función, los argumentos de 'palabras clave' ('keyword') 
# deben seguir a  los argumentos posicionales.
# Todos los argumentos de 'palabra clave' pasados ​​deben coincidir con uno de
# los argumentos aceptados por la función (por ejemplo, actor no es un 
# argumento válido para la función 'parrot'), y su orden no es importante. 
# Esto también incluye argumentos no opcionales (por ejemplo, 
# parrot(voltaje = 1000) también es válido). Ningún argumento puede recibir
# un valor mas de una vez. Aquí hay un ejemplo que falla debido a esta 
# restricción:

def function(a):
    pass

# print(function(0, a=0))
# --> Generará el error:
'''
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: function() got multiple values for argument 'a'
'''

# Cuando un parámetro formal final de la forma **name está presente, recibe un 
# diccionario (consulte Tipos de mapeo — dict) que contiene todos los 
# argumentos de palabras clave excepto los correspondientes a un parámetro 
# formal. Esto se puede combinar con un parámetro formal de la forma *name
# (descrito en la siguiente subsección) que recibe una tupla que contiene los
# argumentos posicionales más allá de la lista de parámetros formales. 
# (*name debe aparecer antes de **name). Por ejemplo, si definimos una función 
# como esta:

def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

# Podría llamarse así:

cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")

# y por supuesto imprimiría:

'''
-- Do you have any Limburger ?
-- I'm sorry, we're all out of Limburger
It's very runny, sir.
It's really very, VERY runny, sir.
----------------------------------------
shopkeeper : Michael Palin
client : John Cleese
sketch : Cheese Shop Sketch
'''
print()
# Tenga en cuenta que el orden en que se imprimen los argumentos de 'palabras 
# clave' está garantizado para que coincida con el orden en que se 
# proporcionaron en la llamada de la función.

#----------------------
# Parámetros especiales
#----------------------

# De forma predeterminada, los argumentos se pueden pasar a una función de 
# Python ya sea por posición o explícitamente por 'palabra clave'. Para mejorar 
# la legibilidad y el rendimiento, tiene sentido restringir la forma en que se
# pueden pasar los argumentos para que un desarrollador solo tenga que mirar en
# la definición de la función para determinar si los elementos se pasan por 
# posición, por posición o 'palabra clave', o por 'palabra clave'.

# La definición de una función puede verse así:

'''
def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
      -----------    ----------     ----------
        |             |                  |
        |        Posicional o 'keyword'  |
        |                                - sólo 'Keyword'
        -- sólo Posicional
      
'''

# Donde '/' y '*' son opcionales. Si se utilizan, estos símbolos indican el tipo de
# parámetro por cómo se pueden pasar los argumentos a la función: solo posicional,
# posicional-o-palabra clave y solo palabra clave. También se hace referencia a 
# los parámetros de 'palabras clave' a como 'parámetros nombrados'.

#--------------------------------------------
# Argumentos posicionales o de palabras clave
#--------------------------------------------

# Si '/' y '*' no están presentes en la definición de la función, los argumentos
# pueden ser pasado a una función por posición o por 'palabra clave'.

#-----------------------------
# Parámetros solo posicionales
#-----------------------------

# Mirando esto con un poco más de detalle, es posible marcar ciertos parámetros
# solo como posicionales. Si solo es posicional, el orden de los parámetros
# importa, y los parámetros no se pueden pasar por 'palabra clave'. Los 
# parámetros que solo son  posicionales se colocan antes de '/' 
# (barra inclinada). El símbolo '/' se usa para separar lógicamente los 
# parámetros solo posicionales del resto de los parámetros.
# Si no hay '/' en la definición de la función, no hay parámetros solo 
# posicionales.

# Los parámetros que siguen a '/' pueden ser posicionales o de 'palabra clave'
# o solo de 'palabra clave'.

#-----------------------------------
# Argumentos de solo 'palabra clave'
#-----------------------------------

# Para marcar parámetros como solo 'palabras clave', indicando que se deben 
# pasar los parámetros por argumento de palabra clave, coloque un '*' en la 
# lista de argumentos justo antes del primer parámetro solo de 'palabra clave'.

#----------------------
# Ejemplos de funciones
#----------------------

# Considere las siguientes definiciones de funciones de ejemplo prestando
# mucha atención a los marcadores / y *:

def standard_arg(arg):
    print(arg)

def pos_only_arg(arg, /):
    print(arg)

def kwd_only_arg(*, arg):
    print(arg)

def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)

# La primera definición de función, 'standard_arg', la forma más familiar, no
# impone restricciones sobre la convención de llamada y los argumentos se 
# pueden pasar por posición o palabra clave:

print(standard_arg(2))
# --> 2

print(standard_arg(arg=2))
# --> 2

# La segunda función, pos_only_arg, está restringida a usar solo parámetros
# posicionales ya que hay un '/' en la definición de la función:

print(pos_only_arg(1))
# --> 1

# print(pos_only_arg(arg=1))
# --> Genera el error:
'''
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: pos_only_arg() got some positional-only arguments passed as keyword arguments: 'arg'
'''

# La tercera función, kwd_only_args, solo permite argumentos de 'palabras clave '
# como se indica con un '* 'en el definición de función:

# print(kwd_only_arg(3))
# --> Generará el error
'''
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: kwd_only_arg() takes 0 positional arguments but 1 was given
'''

print(kwd_only_arg(arg=3))
# --> 3

# Y en el últimocaso se usan las tres convenciones de llamada en la misma 
# definición de función:

# print(combined_example(1, 2, 3))
# --> Generará el error:
'''
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: combined_example() takes 2 positional arguments but 3 were given
'''

print(combined_example(1, 2, kwd_only=3))
# --> 1 2 3

print(combined_example(1, standard=2, kwd_only=3))
# --> 1 2 3
print(" ")
# print(combined_example(pos_only=1, standard=2, kwd_only=3))
# --> Generará el siguiente error:
'''
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: combined_example() got some positional-only arguments passed as keyword arguments: 'pos_only'
'''

# Finalmente, considere esta definición de función que tiene una colisión 
# potencial entre el nombre del argumento posicional y **kwds que tiene nombre 
# como clave:

def foo(name, **kwds):
    return 'name' in kwds

# No hay ninguna llamada posible que lo haga devolver 'Verdadero' ya que la 
# palabra clave 'name' siempre estará vinculada al primer parámetro. 
# Por ejemplo:

# print(foo(1, **{'name': 2}))
# --> Generará el error:
'''
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: foo() got multiple values for argument 'name'
'''

# Pero usando '/' (solo argumentos posicionales), es posible, ya que permite 
# el nombre como un argumento posicional argumento y 'name' como 'clave
# en los argumentos de 'palabras clave':

def foo(name, /, **kwds):
    return 'name' in kwds

print(foo(1, **{'name': 2}))
# --> True

# En otras palabras, los nombres de los parámetros solo posicionales se pueden 
# usar en **kwds sin ambigüedad.

#---------------
# Recapitulación
#---------------

# El caso de uso determinará qué parámetros usar en la definición de la función:

def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
    pass

# Como guía:

# Use solo posicional si desea que el nombre de los parámetros no esté 
# disponible para el usuario. Esto es útil cuando los nombres de los parámetros
# no tienen un significado real, si desea hacer cumplir el orden de los 
# argumentos cuando se llama a la función o si necesita tomar algunos 
# parámetros posicionales y 'palabras clave' arbitrarias.

# Use solo 'palabras clave' cuando los nombres tengan significado y la 
# definición de la función sea más comprensible siendo explícito con los 
# nombres, o quiere evitar que los usuarios confíen en la posición del
# argumento que se pasa.

# Para construir una una API, use solo posicional para evitar romper los
# cambios de la API si el nombre del parámetro es modificado en el futuro.

#---------------------------------
# Listas de argumentos arbitrarios
#---------------------------------

# Finalmente, la opción que se usa con menos frecuencia es especificar que una 
# función se puede llamar con un número arbitrario de argumentos. Estos 
# argumentos estarán envueltos en una tupla (ver Tuplas y Secuencias). 
# Antes del número variable de argumentos, cero o más argumentos normales
# pueden ocurrir.

def write_multiple_items(file, separator, *args):
    file.write(separator.join(args))

# Normalmente, estos argumentos variados serán los últimos en la lista de 
# parámetros formales, porque recogen todos los argumentos de entrada restantes
# que se pasan a la función. Cualquier parámetro formal que ocurra después
# del parámetro '*args' son argumentos de 'solo palabra clave', lo que 
# significa que solo se puede usar como 'palabras clave en lugar de 
# argumentos posicionales.

def concat(*args, sep="/"):
    return sep.join(args)

print(concat("earth", "mars", "venus"))
# --> 'earth/mars/venus'
print(concat("earth", "mars", "venus", sep="."))
# --> 'earth.mars.venus'
print(" ")

#---------------------------------------
# Desempaquetado de listas de argumentos
#---------------------------------------

# La situación inversa ocurre cuando los argumentos ya están en una lista o 
# tupla pero necesitan ser desempaquetado para una llamada de función que 
# requiere argumentos posicionales separados. por ejemplo, la función 'range()'
# incorporada espera argumentos de inicio y finalización separados. Si no 
# están disponibles por separado, escriba la llamada de función con el 
# operador '*' para desempaquetar los argumentos de una lista o tupla:

print(list(range(3, 6)))      # Llamada normal con argumento separados
# --> [3, 4, 5]
args = [3, 6]
print(list(range(*args)))     # Llamada con argumentos empacados en una lista
# --> [3, 4, 5]
print(" ")

# De la misma manera, los diccionarios pueden entregar argumentos de 'palabras
# clave' con el operador '**':

def parrot(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")

d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
print(parrot(**d))
# --> -- This parrot wouldn't VOOM if you put four million volts through it. E's bleedin' demised !
print(" ")

#-------------------
# Expresiones Lambda
#-------------------

# Se pueden crear pequeñas funciones anónimas con la palabra clave 'lambda'. 
# Esta función devuelve suma de sus dos argumentos: lambda a, b: a+b. 
# Las funciones lambda se pueden usar dondequiera que que un objeto función sea
# requerido. Están restringidas sintácticamente a una sola expresión. 
# Semánticamente, son solo agregado sintáctico para una definición de función 
# normal. Como las definicones de las funciones anidadas, las funciones lambda
# pueden hacer referencia a variables del ámbito contenedor:

def make_incrementor(n):
    return lambda x: x + n

f = make_incrementor(42)

print(f(0))
# --> 42
print(f(1))
# --> 43
print(" ")

# El ejemplo anterior usa una expresión lambda para devolver una función. Otro 
# uso es pasar una pequeña función como argumento:

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
print(pairs)
# --> [(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]
print(" ")

#-------------------------
# Cadenas de documentación
#-------------------------

# Aquí hay algunas convenciones sobre el contenido y el formato de las cadenas 
# de documentación.

# La primera línea siempre debe ser un resumen breve y conciso del propósito 
# del objeto. Para ser breve, no debe indicar explícitamente el nombre o el 
# tipo del objeto, ya que estos están disponibles por otros medios (excepto
# si el nombre resulta ser un verbo que describe la operación de una función).
# Esta línea debe comenzar con una letra mayúscula y terminar con un punto.

# Si hay más líneas en la cadena de documentación, la segunda línea debe estar 
# en blanco, separando visualmente el resumen del resto de la descripción. las 
# siguientes lineas deben ser uno o más párrafos que describan las convenciones 
# de llamada del objeto, su efectos laterales, Etc.

# El analizador de Python no elimina la sangría de los literales de cadena de 
# varias líneas en Python, así que las herramientas que procesan la 
# documentación tienen que eliminar la sangría si se desea. Esto se hace usando
# la siguiente convención. La primera línea que no está en blanco después de la
# primera línea de la cadena determina la cantidad de sangría para toda la 
# cadena de documentación. (No podemos usar la primera línea, ya que 
# generalmente se encuentra junto a las comillas de apertura de la cadena, por 
# lo que la sangría no es aparente en el literal de la cadena.) Espacio en 
# blanco "equivalente" se quita de la sangría desde el principio de todas las
# líneas de la cadena. lineas que son sangría menor no debería ocurrir, pero
# si ocurre, todos sus espacios en blanco iniciales deben ser despojado.
# La equivalencia de los espacios en blanco debe probarse después de la 
# expansión de las pestañas (a 8 espacios, normalmente).

# Aquí hay un ejemplo de una cadena de documentos de varias líneas:

def my_function():
    """Do nothing, but document it.

    No, really, it doesn't do anything.
    """
    pass

print(my_function.__doc__)

# Do nothing, but document it.

#    No, really, it doesn't do anything.
print(" ")

#-------------------------
# Anotaciones de funciones
#-------------------------

# Las anotaciones de funciones son información de metadatos completamente 
# opcional sobre los tipos utilizados por funciones definidas por el usuario 
# (consulte PEP 3107 y PEP 484 para obtener más información).

# Las anotaciones se almacenan en el atributo __annotations__ de la función 
# como un diccionario y no tienen efecto en ninguna otra parte de la función. 
# Las anotaciones de parámetros se definen mediante unsímbolo 'dos puntos' 
# después del nombre del parámetro, seguido de una expresión que evalúa el 
# valor de la anotación. Las anotaciones de retorno se definen mediante una
# literal '->', seguida de una expresión, entre la lista de parámetros y los 
# 'dos puntos' que indican el final de la instrucción 'def'. El siguiente
# ejemplo tiene un argumento obligatorio, un argumento opcional y el valor
#  de retorno anotado:

def f(ham: str, eggs: str = 'eggs') -> str:
    print("Annotations:", f.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + ' and ' + eggs

print(f('spam'))
# --> Annotations: {'ham': <class 'str'>, 'return': <class 'str'>, 'eggs': <class 'str'>}
# --> Arguments: spam eggs
# --> 'spam and eggs'
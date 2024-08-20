#-------------------------------------------------------------------------------
# Estatutos de Control de Flujo
#
# Notas creadas y editadas por: Sergio Fco. Hernández Machuca
# Xalapa, Veracruz, México
# 2023 - Julio
#
# La información proviene de diversas fuentes de internet, principalmente los 
# sitios oficiales del lenguaje Python (https://www.python.org) y Micropython 
# (https://micropython.org).
#-------------------------------------------------------------------------------

# -----------------
# Declaraciones if
# -----------------

# Quizás el tipo de sentencia más conocido es la sentencia 'if'
# Por ejemplo:

print()
x = int(input("Por favor introduzca un número entero: "))
# --> Por favor introduzca un número entero:: 42
if x < 0:
    x = 0
    print("Negativo cambiado a Cero")
elif x == 0:
    print("Cero")
elif x == 1:
    print("Simple")
else:
    print("Más")
# --> Más
print()

# Puede haber cero o más partes 'elif', y la parte 'else' es opcional.
# La palabra clave 'elif' es la abreviatura de 'else if' y es útil para evitar
# sangría. Una secuencia 'if... elif... elif...' es un sustituto del 'switch'
# o declaraciones de 'case' encontradas en otros idiomas.

# Si está comparando el mismo valor con varias constantes, o verificando
# tipos o atributos específicos, también puede encontrar útil la declaración
# de coincidencia ('match').

# ---------------
# Esatutos 'for'
# ---------------

# La declaración 'for' en Python difiere un poco de lo que puede estar
# acostumbrado en lenguaje C o Pascal. En lugar de iterar siempre sobre una
# progresión aritmética de números (como en Pascal), o dando al usuario la
# capacidad de definir tanto el paso de iteración y condición de detención
# (como en el lenguaje C), la instrucción 'for' de Python itera sobre los
# elementos de cualquier secuencia (una lista o una cadena), en el orden en
# que aparecen en la secuencia. Por ejemplo:

# Medida de la longitud de algunas cadenas:
words = ["cat", "window", "defenestrate", "cadena algo larga y aburrida"]
for w in words:
    print(w, len(w))
"""
cat 3
wcat 3
window 6
defenestrate 12
cadena algo larga y aburrida 28
"""
print()

# Crear un código que modifica una colección mientras itera sobre ella puede
# ser algo complicado. En cambio, por lo general es más simple recorrer una
# copia de la colección o crear una nueva colección:

# Crear una colección de muestra:
users = {"Hans": "active", "Éléonore": "inactive", "景太郎": "active"}
print("Colección Original")
print(users)
print()
# Estrategia:  Iterar sobre una copia
for user, status in users.copy().items():
    if status == "inactive":
        del users[user]
print(users)
print()

# Estrategia:  Crear una colección nueva
active_users = {}
for user, status in users.items():
    if status == "active":
        active_users[user] = "ACTIVO"
print(active_users)
print()

# ---------------------
# La función 'range()'
# ---------------------

# Si se necesita iterar sobre una secuencia de números, la función incorporada
# 'range()' es útil. Genera progresiones aritméticas:

for i in range(5):
    print(i)
"""
0
1
2
3
4
"""
print()

# El punto final dado en la función 'range()' nunca es parte de la secuencia
# generada; rango(10) genera 10 valores, desde 0 hasta 9 que son los índices
# legales para elementos de una secuencia de longitud 10.
# Es posible dejar que el rango comience en otro número, o especificar un
# incremento diferente (incluso negativo; a veces esto se llama el 'paso',
# ('step')):

list(range(5, 10))
# --> [5, 6, 7, 8, 9]

list(range(0, 10, 3))
# --> [0, 3, 6, 9]

list(range(-10, -100, -30))
# --> [-10, -40, -70]
print()

# Para iterar sobre los índices de una secuencia, puede combinar 'range()' y
# 'len()' de la siguiente manera:

a = ["Mary", "had", "a", "little", "lamb"]
for i in range(len(a)):
    print(i, a[i])
"""
0 Mary
1 had
2 a
3 little
4 lamb
"""
print()

# En la mayoría de estos casos, sin embargo, es conveniente usar la función
# 'enumerate()', ver Técnicas de lazos.

# Ocurre algo extraño si solo se imprime el rango:

print(range(10))
# --> range(0, 10)
print(range(0, 10))
# -->range(0, 10)
print()

# En muchos sentidos, el objeto devuelto por 'range()' se comporta como si
# fuera una lista, pero en realidad no lo es. Es un objeto que devuelve los
# elementos sucesivos de la secuencia deseada cuando itera sobre ella, pero en
# realidad no hace la lista, ahorrando así espacio.

# Decimos que algún objeto es iterable, es decir, adecuado como destino para
# funciones y construcciones que esperan algo de lo que pueden obtener sucesivas
# artículos hasta que se agote el suministro. Hemos visto que la sentencia 'for'
# es una de estas construcciones, mientras que otro ejemplo de una función que
# toma un iterable es suma():

print(sum(range(4)))  # 0 + 1 + 2 + 3
# --> 6
print()

# ---------------------------------------------------------------
# Declaraciones 'break' y 'continue' y otras Cláusulas en Bucles
# ---------------------------------------------------------------

# La instrucción 'break', como en el lenguaje C, permite salir de la sección
# más interna mientras se está ejecutando un lazo.

# Las declaraciones de bucle pueden tener una cláusula 'else'; ésta sección se
# ejecuta cuando el bucle termina por agotamiento del iterable (con 'for') o
# cuando la condición se vuelve falsa ('False') (con 'while'), pero no cuando
# el bucle termina con un estatuto 'break'. Esto se ejemplifica con el siguiente
# bucle, que busca números primos:

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, "igual a", x, "*", n // x)
            break
    else:
        # Aquí se llega sin encontrar algún factor
        print(n, "es un número primo")
print()
"""
2 es un número primo
3 es un número primo
4 igual a 2 * 2
5 es un número primo
6 igual a 2 * 3
7 es un número primo
8 igual a 2 * 4
9 igual a 3 * 3
"""

# (Sí, este es el código correcto. Fíjese bien: la cláusula 'else' pertenece al
# bucle 'for', no la instrucción 'if').

# Cuando se usa con un bucle, la cláusula 'else' tiene más en común con la
# cláusula 'else' de una sentencia 'try' que con las sentencias 'if':
# la segmento 'else' de una sentencia 'try' se ejecuta cuando no ocurren
# excepciones, y la cláusula 'else' de un bucle se ejecuta cuando no se produce
# ningún estatuto 'break'. Para obtener más información sobre la declaración
# 'try' y excepciones, consulte la sección de Manejo de Excepciones.

# La sentencia 'continue', también prestada del lenguaje C, continúa con la
# siguiente iteración del ciclo:

for num in range(2, 10):
    if num % 2 == 0:
        print("Se encontró número par", num)
        continue
    print("Se encontró un número impar", num)
"""
Se encontró número par 2
Se encontró un número impar 3
Se encontró número par 4
Se encontró un número impar 5
Se encontró número par 6
Se encontró un número impar 7
Se encontró número par 8
Se encontró un número impar 9
"""
print()

# --------------------
# El estatuto 'pass'
# --------------------

# La sentencia 'pass' no hace nada. Se puede utilizar cuando se requiere una
# declaración sintácticamente, pero el programa no requiere ninguna acción.
# Por ejemplo:
"""
while True:
    pass  # Ocupado, esperando una interrupción del teclado (Ctrl+C)
"""

# Esto se usa comúnmente para crear clases mínimas:
"""
class MyEmptyClass:
    pass
"""
# Another place pass can be used is as a place-holder for a function or
# conditional body when you are working on new code, allowing you to keep
# thinking at a more abstract level. The pass is silently ignored:


# Otro lugar en donde el estatuto 'pass' se puede usar es como marcador de
# posición para una función o cuerpo condicional cuando está trabajando en
# un nuevo código, lo que le permite pensar en un nivel más abstracto.
# El estatuto 'pass'  se ignora en silencio

"""
def initlog(*args):
    pass   # Habrá que implementar esto después
"""
# 00000000000000000000000000000000000000000000000000000000000000000000000000

# -------------------------------
# Estatuto 'match', coincidencia
# -------------------------------

# Una instrucción 'match' toma una expresión y compara su valor con valores
# sucesivos de patrones dados como uno o más bloques de casos. Esto es
# superficialmente similar a una declaración 'switch' como en el lenguake C,
# Java o JavaScript (y muchos otros lenguajes), pero es más similar a la
# coincidencia de patrones en lenguajes como Rust o Haskell. Sólo se ejecuta
# la igualdad con el primer patrón que coincide y también se puede extraer
# componentes (elementos de secuencia o atributos de objeto) desde el valor
# hasta variables.

# La forma más simple de comparar un valor dado con una o más literales:


def http_error(status):
    match status:
        case 400:
            return "Mala llamada - error"
        case 404:
            return "No sa encuentra - rectificar"
        case 418:
            return "Ya estoy aquí"
        case _:
            return "Algo está bastante mal"


print(http_error(400))
# --> Mala llamada - error
print(http_error(404))
# --> No sa encuentra - rectificar
print(http_error(418))
# --> Ya estoy aquí
print(http_error(466))
# --> Algo está bastante mal
print(http_error(4))
# --> Algo está bastante mal
print()

# Tenga en cuenta que el último bloque: donde  "nombre de la variable" se
# compara con '_', actúa como  un comodín y de esta forma no puede fallar la
# búsqueda de coincidencia nunca. Si ningún caso coincide, ninguna de las ramas
# se ejecuta.

# Se pueden combinar varias literales en un solo patrón usando '|' ("o"):

"""
case 401 | 403 | 404:
    return "No Permitido"
"""

# Los patrones pueden verse como asignaciones de desempaquetado y se pueden
# usar para enlazar variables:


# El punto está en una tupla (x, y)
def busqueda(punto):
    match punto:
        case (0, 0):
            print("Origen")
        case (0, y):
            print(f"Y={y}")
        case (x, 0):
            print(f"X={x}")
        case (x, y):
            print(f"X={x}, Y={y}")
        case _:
            raise ValueError("No es un punto")


print(busqueda((8, 28)))
# --> X=8, Y=28
print(busqueda((0, 0)))
# --> Origen
print(busqueda(("w", "z")))
# --> X=w, Y=z

print()

# ¡Estudie esto con cuidado! El primer patrón tiene dos literales, y se puede
# pensar que es una extensión del patrón literal que se muestra arriba. pero
# los siguientes dos patrones combinan un literal y una variable, y la variable
# vincula un valor del sujeto (la tupla punto). El cuarto patrón captura dos
# valores, lo que le hace conceptualmente similar a la asignación de
# desempaquetado (x, y) = punto.

# If you are using classes to structure your data you can use the class name
# followed by an argument list resembling a constructor, but with the ability
# to capture attributes into variables:

# Si está usando clases para estructurar sus datos, puede usar el nombre de la
# clase seguido de una lista de argumentos que se asemeja a un constructor,
# pero con la capacidad para capturar atributos en variables:


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def where_is(point):
    match point:
        case Point(x=0, y=0):
            print("Origen")
        case Point(x=0, y=y):
            print(f"Y={y}")
        case Point(x=x, y=0):
            print(f"X={x}")
        case Point():
            print("Alguna otra cosa")
        case _:
            print("No es un punto")


# Ensayar aquí o pasar a otro segmento de código

# Puede usar parámetros posicionales con algunas clases integradas que
# proporcionan un ordenanamiento por sus atributos (por ejemplo, 'dataclasses').
# También puede definir una determinada posición de los atributos en patrones
# configurando el atributo especial '__match_args__'  en las clases.
# Si está configurado en ("x", "y"), los siguientes patrones son todos
# equivalentes (y todos vinculan el atributo y a la variable 'var)':

"""
Point(1, var)
Point(1, y=var)
Point(x=1, y=var)
Point(y=var, x=1)
"""

# Una forma recomendada de leer los patrones es verlos como una forma extendida
# de lo que se pondría a la izquierda de una asignación, para entender cuáles
# variables tendrían cuál valor. Solo se asignan los nombres independientes
# (como 'var' anteriormente) a través de una declaración de coincidencia
# ('match'). Nombres punteados (como 'foo.bar)', nombres de atributos
# (el 'x=' e 'y=', anteriormente) o nombres de clases (reconocidos por
# el “(…)” junto a ellos como el 'Point' anteriormente) nunca son asignados.

# Los patrones se pueden anidar arbitrariamente. Por ejemplo, si tenemos una
# lista corta de Puntos, con __match_args__ agregado, podríamos emparejarlo
# ('match') así:

"""
class Point:
    __match_args__ = ('x', 'y')
    def __init__(self, x, y):
        self.x = x
        self.y = y

match points:
    case []:
        print("No points")
    case [Point(0, 0)]:
        print("The origin")
    case [Point(x, y)]:
        print(f"Single point {x}, {y}")
    case [Point(0, y1), Point(0, y2)]:
        print(f"Two on the Y axis at {y1}, {y2}")
    case _:
        print("Something else")
"""

# Podemos agregar una cláusula 'if' a un patrón, conocida como "guarda". 
# Si el guarda es 'False', la coincidencia continúa para probar el siguiente 
# bloque de casos. Tenga en cuenta que la captura de valor sucede antes de que 
# se evalúe el guarda:

match point:
    case Point(x, y) if x == y:
        print(f"Y=X at {x}")
    case Point(x, y):
        print(f"Not on the diagonal")

# Varias otras características clave de esta declaración:

# Al igual que desempaquetar asignaciones, los patrones de tupla y lista tienen
# exactamente el mismo significado y en realidad coincide con secuencias 
# arbitrarias. Una excepción importante es que no coinciden con iteradores o 
# cadenas.

# Los patrones de secuencia admiten el desempaquetado extendido: [x, y, *rest]
# y (x, y, *rest) funciona de manera similar a desempaquetar asignaciones. 
# El nombre después de '*' también puede ser '_', por lo que (x, y, *_) 
# coincide con una secuencia de al menos dos elementos sin vincular los
# elementos restantes.

# Patrones de mapeo: {"bandwidth": b, "latency": l} capturan el "ancho de banda" 
# y valores de "latencia" de un diccionario. A diferencia de los patrones de 
# secuencia, las claves adicionales son ignoradas. También se admite un 
# desembalaje como '** rest'. (Pero '**_' sería redundante, por lo que no está 
# permitido).

# Los subpatrones se pueden capturar usando la palabra clave 'as':

"""
case (Point(x1, y1), Point(x2, y2) as p2): ...
"""

# capturará el segundo elemento de la entrada como 'p2' (siempre y cuando la
# entrada sea una secuencia de dos puntos)

# La mayoría de los literales se comparan por igualdad, sin embargo, los 
# singletons 'True', 'False' y 'None' se comparan por identidad.

# Los patrones pueden usar constantes con nombre. Estos deben ser nombres con 
# puntos para evitar que sean interpretados como variable de captura:

from enum import Enum


class Color(Enum):
    RED = "red"
    GREEN = "green"
    BLUE = "blue"


color = Color(input("Enter your choice of 'red', 'blue' or 'green': "))

match color:
    case Color.RED:
        print("I see red!")
    case Color.GREEN:
        print("Grass is green")
    case Color.BLUE:
        print("I'm feeling the blues :(")

# Para obtener una explicación más detallada y ejemplos adicionales, 
# puede consultar PEP 636 que está escrito en formato tutorial.

print()
print("***[FIN de esta SECCIÓN]***")
print()

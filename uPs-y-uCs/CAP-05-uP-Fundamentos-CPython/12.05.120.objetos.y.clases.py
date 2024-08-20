#-------------------------------------------------------------------------------
# Clases y Objetos
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
======
Clases
======

Las clases proporcionan un medio para agrupar datos y funcionalidad. 
La creación de una nueva clase crea un nuevo tipo de objeto, lo que permite 
crear nuevas instancias de ese tipo. Cada instancia de clase puede tener 
atributos adjuntos para mantener su estado. Las instancias de clase también 
pueden tener métodos (definidos por su clase) para modificar su estado.

En comparación con otros lenguajes de programación, el mecanismo de clases 
de Python agrega clases con un mínimo de sintaxis y semántica nuevas. Es una 
mezcla de los mecanismos de clase que se encuentran en los lenguajes C++ y 
Modula-3. Las clases de Python brindan todas las características estándar de 
la Programación Orientada a Objetos: el mecanismo de herencia de clases permite
múltiples clases base, una clase derivada puede anular cualquier método de su 
clase o clases base, y un método puede llamar al método de una clase base con 
el mismo nombre. Los objetos pueden contener cantidades y tipos de datos 
arbitrarios. Como ocurre con los módulos, las clases participan de la 
naturaleza dinámica de Python: se crean en tiempo de ejecución y se pueden 
modificar aún más después de la creación.

En la terminología del lenguaje C++, normalmente los miembros de la clase 
(incluidos los miembros de datos) son públicos (excepto las Variables privadas
que se muestran a continuación) y todas las funciones de los miembros son 
virtuales. Como en el lenguaje Modula-3, no hay abreviaturas para hacer 
referencia a los miembros del objeto desde sus métodos: la función del método 
se declara con un primer argumento explícito que representa el objeto, que la 
llamada proporciona implícitamente. Como en el lenguaje Smalltalk, las clases 
mismas son objetos. Esto proporciona semántica para importar y renombrar. 
A diferencia de C++ y Modula-3, los tipos incorporados se pueden usar como 
clases base para que el usuario las extienda. Además, como en C++, la mayoría 
de los operadores integrados con sintaxis especial (operadores aritméticos, 
subíndices, etc.) se pueden redefinir para instancias de clase.

'''
#
'''
----------------------------------
Cuestiones sobre nombres y objetos
----------------------------------

Los objetos tienen individualidad y varios nombres (en varios ámbitos), se 
pueden vincular al mismo objeto. Esto se conoce como 'aliasing' en otros 
idiomas. Por lo general, esto no se aprecia a primera vista en Python, y se
puede ignorar con seguridad cuando se trata de tipos básicos inmutables 
(números, cadenas, tuplas). Sin embargo, el alias tiene un efecto posiblemente 
sorprendente en la semántica del código de Python que involucra objetos 
mutables como listas, diccionarios y la mayoría de los otros tipos. 
Esto generalmente se usa en beneficio del programa, ya que los alias se 
comportan como punteros en algunos aspectos. Por ejemplo, pasar un objeto es 
barato ya que la implementación solo pasa un puntero; y si una función 
modifica un objeto pasado como argumento, la persona que llama verá el 
cambio; esto elimina la necesidad de dos mecanismos diferentes de paso de 
argumentos como en Pascal.

'''
#
'''
---------------------------------------
Ámbitos y espacios de nombres de Python
---------------------------------------

Antes de presentar las clases, un comentario sobre las reglas de alcance de 
Python. Las definiciones de clase juegan algunos trucos ingeniosos con los 
espacios de nombres, y necesita saber cómo funcionan los ámbitos y los espacios
de nombres para comprender completamente lo que está sucediendo. Por cierto, 
el conocimiento sobre este tema es útil para cualquier programador avanzado 
de Python.

Algunas definiciones.

Un espacio de nombres es una asignación de nombres a objetos. La mayoría de 
los espacios de nombres se implementan actualmente como diccionarios de
Python, pero eso normalmente no se nota de ninguna manera (excepto por el 
rendimiento) y puede cambiar en el futuro. Ejemplos de espacios de nombres 
son: el conjunto de nombres integrados (que contienen funciones como abs() 
y nombres de excepción integrados); los nombres globales en un módulo; y los
nombres locales en una invocación de función. En cierto sentido, el conjunto 
de atributos de un objeto también forman un espacio de nombres. Lo importante
que debe saber acerca de los espacios de nombres es que no existe 
absolutamente ninguna relación entre los nombres en diferentes espacios de 
nombres; por ejemplo, dos módulos diferentes pueden definir una función
maximizar sin confusión: los usuarios de los módulos deben prefijarlo con el
nombre del módulo.

Por cierto, se emplea la palabra atributo para cualquier nombre que sigue a un 
caracter punto ('.'); por ejemplo, en la expresión z.real, real es un atributo 
del objeto z. Estrictamente hablando, las referencias a nombres en módulos son 
referencias a atributos: en la expresión 'modname.funcname', 'modname' es un o
bjeto de módulo y 'funcname' es un atributo del mismo. En este caso, resulta 
que hay un mapeo directo entre los atributos del módulo y los nombres 
globales definidos en el módulo: ¡comparten el mismo espacio de nombres!

Los atributos pueden ser de solo lectura o de escritura. En este último caso,
es posible la asignación a atributos. Los atributos del módulo se pueden 
escribir: puede escribir 'modname.the_answer = 42'. Los atributos que se 
pueden escribir también se pueden eliminar con la instrucción 'del'. Por 
ejemplo, 'del modname.the_answer' eliminará el atributo 'the_answer' del 
objeto nombrado por 'modname'.

Los espacios de nombres se crean en diferentes momentos y tienen diferentes 
tiempos de vida. El espacio de nombres que contiene los nombres incorporados 
se crea cuando se inicia el intérprete de Python y nunca se elimina. El espacio 
de nombres global para un módulo se crea cuando se lee la definición del módulo;
normalmente, los espacios de nombres de los módulos también duran hasta que el 
intérprete se cierra. Las declaraciones ejecutadas por la invocación de nivel 
superior del intérprete, ya sea leídas desde un archivo de script o de forma 
interactiva, se consideran parte de un módulo llamado __main__, por lo que 
tienen su propio espacio de nombres global. (Los nombres integrados en realidad 
también viven en un módulo; esto se llama funciones integradas).

El espacio de nombres local para una función se crea cuando se llama a la 
función y se elimina cuando la función devuelve o genera una excepción que no 
se maneja dentro de la función. (En realidad, olvidar sería una mejor manera 
de describir lo que realmente sucede). Por supuesto, cada invocación recursiva 
tiene su propio espacio de nombres local.

Un alcance es una región textual de un programa de Python donde se puede 
acceder directamente a un espacio de nombres. "Accesible directamente" aquí 
significa que una referencia no calificada a un nombre intenta encontrar el 
nombre en el espacio de nombres.

Aunque los ámbitos se determinan de forma estática, se utilizan de forma 
dinámica. En cualquier momento durante la ejecución, hay 3 o 4 ámbitos 
anidados cuyos espacios de nombres son directamente accesibles:

--> El ámbito más interno, que se busca primero, contiene los nombres locales.
--> Los ámbitos de cualquier función envolvente, que se buscan comenzando con 
el ámbito envolvente más cercano, contienen nombres no locales, pero también
no globales.
--> El penúltimo ámbito contiene los nombres globales del módulo actual.
--> El ámbito más externo (buscado en último lugar) es el espacio de nombres 
que contiene los nombres integrados.

Si un nombre se declara global, todas las referencias y asignaciones van 
directamente al penúltimo ámbito que contiene los nombres globales del módulo. 
Para volver a vincular las variables que se encuentran fuera del alcance más 
interno, se puede usar la declaración 'non local'; si no se declaran 
no locales, esas variables son de solo lectura (un intento de escribir en 
dicha variable simplemente creará una nueva variable local en el ámbito más 
interno, dejando sin cambios la variable externa con el mismo nombre).

Por lo general, el alcance local hace referencia a los nombres locales de la 
función actual (textualmente). Fuera de las funciones, el ámbito local hace 
referencia al mismo espacio de nombres que el ámbito global: el espacio de 
nombres del módulo. Las definiciones de clase colocan otro espacio de nombres 
en el ámbito local.

Es importante darse cuenta de que los ámbitos se determinan textualmente: el 
ámbito global de una función definida en un módulo es el espacio de nombres de
ese módulo, sin importar desde dónde o con qué alias se llame la función. 
Por otro lado, la búsqueda real de nombres se realiza dinámicamente, en tiempo
de ejecución; sin embargo, la definición del lenguaje está evolucionando 
hacia una resolución de nombres estática, en el momento de la "compilación"
, ¡así que no confíe en la resolución de nombres dinámica! (De hecho, las 
variables locales ya están determinadas estáticamente).

Una peculiaridad especial de Python es que, si no hay una declaración 'global'
o 'non local' en vigor, las asignaciones de nombres siempre van al ámbito más
interno. Las asignaciones no copian datos, solo vinculan nombres a objetos. 
Lo mismo ocurre con las eliminaciones: la declaración 'del x' elimina el enlace
de 'x 'del espacio de nombres al que hace referencia el ámbito local. De hecho,
todas las operaciones que introducen nuevos nombres utilizan el ámbito local:
en particular, las sentencias de importación y las definiciones de funciones 
vinculan el módulo o el nombre de la función en el ámbito local.

La declaración 'global' se puede utilizar para indicar que las variables 
particulares viven en el ámbito global y deben reubicarse allí; la 
declaración 'non local' indica que las variables particulares viven en un 
ámbito cerrado y deben reubicarse allí.
'''

#-----------------------------------------
# Ejemplo de ámbitos y espacios de nombres
#-----------------------------------------

# Este es un ejemplo que demuestra cómo hacer referencia a los diferentes 
# ámbitos y espacios de nombres, y cómo afectan los enlaces de variables 
# globales y no locales:

def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

print()
scope_test()
print("In global scope:", spam)
print()

# La salida del código de ejemplo es:

# --> After local assignment: test spam
# --> After nonlocal assignment: nonlocal spam
# --> After global assignment: nonlocal spam
# --> In global scope: global spam

# Tenga en cuenta cómo la asignación local (que es la predeterminada) no cambió
# el enlace de spam de 'scope_tes't. La asignación no local cambió el enlace 
# de spam de 'scope_test' y la asignación 'global' cambió el enlace a nivel de
# módulo.

# También puede ver que no había un enlace previo para 'spam'' no deseado 
# antes de la asignación 'global'.

'''
-------------------------------
Un primer vistazo a las clases
-------------------------------
Las clases introducen un poco de sintaxis nueva, tres tipos de objetos nuevos
y algunas semánticas nuevas.

-----------------------------------
--> Sintaxis de definición de clase
-----------------------------------

La forma más simple de definición de clase se ve así:

class NombreClase:
    <estatuto-1>
    .
    .
    .
    <estatuto-N>

Las definiciones de clases, como las definiciones de funciones 
(sentencias 'def') deben ejecutarse antes de que tengan algún efecto. 
(Posiblemente podría colocar una definición de clase en una rama de una 
declaración 'if', o dentro de una función).

En la práctica, las declaraciones dentro de una definición de clase 
generalmente serán definiciones de función, pero se permiten otras 
declaraciones y, a veces, son útiles; volveremos a esto más adelante. Las 
definiciones de funciones dentro de una clase normalmente tienen una forma 
peculiar de lista de argumentos, dictada por las convenciones de llamada para 
métodos; de nuevo, esto se explica más adelante.

Cuando se ingresa una definición de clase, se crea un nuevo espacio de nombres 
y se usa como ámbito local; por lo tanto, todas las asignaciones a variables 
locales van a este nuevo espacio de nombres. En particular, las definiciones 
de función vinculan aquí el nombre de la nueva función.

Cuando una definición de clase se deja normalmente (al final), se crea un 
objeto de clase. Esto es básicamente un envoltorio alrededor del contenido 
del espacio de nombres creado por la definición de clase; aprenderemos más 
sobre los objetos de clase en la siguiente sección. El ámbito local original 
(el que estaba en vigor justo antes de que se ingresara la definición de la 
clase) se restablece y el objeto de la clase se vincula aquí al nombre de la 
clase dado en el encabezado de la definición de la clase ('NombreClase' en 
el ejemplo).
'''

#-----------------
# Objetos de clase
#-----------------

# Los objetos de clase admiten dos tipos de operaciones: referencias de 
# atributos e instanciación.

# Las referencias de atributos usan la sintaxis estándar utilizada para todas 
# las referencias de atributos en Python: 'obj.name'. Los nombres de atributos 
# válidos son todos los nombres que estaban en el espacio de nombres de la 
# clase cuando se creó el objeto de la clase. Entonces, si la definición de 
# la clase se viera así:

class MyClass:
    """Una clase de ejemplo simple"""
    i = 12345

    def f(self):
        return 'hello world'
    
# Entonces 'MyClass.i' y 'MyClass.f' son referencias de atributo válidas, que 
# devuelven un número entero y un objeto de función, respectivamente. También 
# se pueden asignar atributos de clase, por lo que puede cambiar el valor de 
# 'MyClass.i' por asignación. '__doc__' también es un atributo válido, que 
# devuelve la cadena de documentación que pertenece a la clase: 
# "Una clase de ejemplo simple".

# La creación de instancias de clases utiliza la notación de funciones. 
# Simplemente suponga que el objeto de la clase es una función sin parámetros 
# que devuelve una nueva instancia de la clase. Por ejemplo (asumiendo la 
# clase anterior):

x = MyClass()

#  Crea una nueva instancia de la clase y asigna este objeto a la variable 
# local x

# La operación de creación de instancias ("llamar" a un objeto de una clase) 
# crea un objeto vacío. A muchas clases les gusta crear objetos con instancias 
# personalizadas para un estado inicial específico. Por lo tanto, una clase 
# puede definir un método especial llamado '__init__()', como este:

def __init__(self):
    self.datos = []

# Cuando una clase define un método '__init__()', la creación de instancias 
# de clase invoca automáticamente a '__init__()' para la instancia de clase 
# recién creada. Entonces, en este ejemplo, se puede obtener una nueva 
# instancia inicializada mediante:

x = MyClass()

# Por supuesto, el método '__init__()' puede tener argumentos para una mayor 
# flexibilidad. En ese caso, los argumentos dados al operador de creación de 
# instancias de clase se pasan a '__init__()'. Por ejemplo,

class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

x = Complex(3.0, -4.5)

print(x.r, x.i)
# --> (3.0, -4.5)
print()

#---------------------
# Objetos de instancia
#---------------------

# Ahora, ¿Qué podemos hacer con los objetos de instancia? Las únicas 
# operaciones que entienden los objetos de instancia son las referencias de 
# atributos. Hay dos tipos de nombres de atributos válidos: atributos de datos 
# y métodos.

# Los 'atributos de dato's corresponden a "variables de instancia" en el 
# lenguaje Smalltalk y a "miembros de datos" en el lenguaje C++. No es 
# necesario declarar los atributos de los datos; al igual que las variables 
# locales, surgen cuando se les asigna por primera vez. Por ejemplo, si 'x' es 
# a instancia de 'MyClass' creada anteriormente, el siguiente fragmento de 
# código imprimirá el valor 16, sin dejar rastro:

x.counter = 1
while x.counter < 10:
    x.counter = x.counter * 2
print(x.counter)
del x.counter

print()

# El otro tipo de referencia de atributo de instancia es un método. Un método 
# es una función que “pertenece a” un objeto. (En Python, el término método 
# no es exclusivo de las instancias de clase: otros tipos de objetos también 
# pueden tener métodos. Por ejemplo, los objetos de lista tienen métodos 
# llamados agregar, insertar, eliminar, clasificar, etc. Sin embargo, en la 
# siguiente discusión, usaremos el término método exclusivamente para hacer 
# referencia a métodos de objetos de instancia de clase, a menos que se 
# indique explícitamente lo contrario).

# Los nombres de métodos válidos de un objeto de instancia dependen de su 
# clase. Por definición, todos los atributos de una clase que son objetos de 
# función definen los métodos correspondientes de sus instancias. Entonces, 
# en nuestro ejemplo, 'x.f' es una referencia de método válida, ya que 
# 'MyClass.f' es una función, pero 'x.i' no lo es, ya que 'MyClass.i' no lo es. 
# Pero 'x.f' no es lo mismo que' MyClass.f': es un objeto de método, no un 
# objeto de función.

#------------------
# Objetos de método
#------------------

# Por lo general, se llama a un método justo después de vincularlo:

x = MyClass()
print(x.f())
# --> 
print()

# En el ejemplo de 'MyClass', esto devolverá la cadena 'hola mundo'. Sin 
# embargo, no es necesario llamar a un método de inmediato: x.f es un objeto 
# de método y puede almacenarse y llamarse más adelante. Por ejemplo:

'''
xf = x.f
while True:
    print(xf())
'''
    
# continuará imprimiendo hola mundo hasta el final de los tiempos.


# ¿Qué sucede exactamente cuando se llama a un método? Es posible que haya 
# notado que se llamó a x.f() sin un argumento anterior, aunque la definición 
# de función para f() especificaba un argumento. ¿Qué pasó con el argumento? 
# Seguramente Python genera una excepción cuando se llama a una función que 
# requiere un argumento sin ninguno, incluso si el argumento no se usa 
# realmente...

# En realidad, es posible que haya adivinado la respuesta: lo especial de los 
# métodos es que el objeto de instancia se pasa como el primer argumento de 
# la función. En nuestro ejemplo, la llamada x.f() es exactamente equivalente 
# a MyClass.f(x). En general, llamar a un método con una lista de 'n' 
# argumentos es equivalente a llamar a la función correspondiente con una 
# lista de argumentos que se crea insertando el objeto de instancia del 
# método antes del primer argumento.

# Si aún no comprende cómo funcionan los métodos, una mirada a la i
# mplementación quizás pueda aclarar las cosas. Cuando se hace referencia a 
# un atributo que no es de datos de una instancia, se busca la clase de la 
# instancia. Si el nombre denota un atributo de clase válido que es un objeto 
# de función, se crea un objeto de método empaquetando (punteros a) el objeto 
# de instancia y el objeto de función que se acaban de encontrar juntos en un 
# objeto abstracto: este es el objeto de método. Cuando se llama al objeto 
# de método con una lista de argumentos, se construye una nueva lista de 
# argumentos a partir del objeto de instancia y la lista de argumentos, y se 
# llama al objeto de función con esta nueva lista de argumentos.

#-------------------------------
# Variables de clase e instancia
#-------------------------------

# En términos generales, las variables de instancia son para datos exclusivos 
# de cada instancia y las variables de clase son para atributos y métodos 
# compartidos por todas las instancias de la clase:

class Dog:

    kind = 'canine'         # Variable de clase compartida por todas las instancias

    def __init__(self, name):
        self.name = name    # Variable de instancia única para cada instancia

d = Dog('Fido')
e = Dog('Buddy')
print(d.kind)               # Compartido por todos los perros
# --> 'canine'
print(e.kind)               # Compartido por todos los perros
# --> 'canine'
print(d.name)               # Único a d
# --> 'Fido'
print(e.name)               # Único a e
# --> 'Buddy'
print()

# Como se discutió al hablar sobre nombres y objetos, los datos compartidos 
# pueden tener efectos posiblemente sorprendentes al involucrar objetos 
# mutables como listas y diccionarios. Por ejemplo, la lista de trucos en el 
# siguiente código no debe usarse como una variable de clase porque todas 
# las instancias de Dog compartirían una sola lista:

class Dog:

    tricks = []             # Uso equivocado de una variable de clase mutable

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')  # Sólo se aplicaría a Fido
e.add_trick('play dead')  # Sólo se aplicaría a Buddy
# Trucos que hace Fido:
print(d.tricks)           # Inesperadamente compartido por todos los perros
# --> ['roll over', 'play dead']
print()

# El diseño correcto de la clase debería usar una variable de instancia en su 
# lugar:

class Dog:

    def __init__(self, name):
        self.name = name
        self.tricks = []    # Crea una lista vacía para cada perro

    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')

print(d.tricks)
# --> ['roll over']
print(e.tricks)
# --> ['play dead']
print()

#------------------
# Otros Comentarios
#------------------

# Si aparece el mismo nombre de atributo tanto en una instancia como en una 
# clase, la búsqueda de atributos prioriza la instancia:

class Warehouse:
   purpose = 'storage'
   region = 'west'

w1 = Warehouse()
print(w1.purpose, w1.region)
# --> storage west
w2 = Warehouse()
w2.region = 'east'
print(w2.purpose, w2.region)
# --> storage east
print()

# Los atributos de datos pueden ser referenciados por métodos, así como por 
# usuarios comunes ("clientes") de un objeto. En otras palabras, las clases no 
# se pueden usar para implementar tipos de datos abstractos puros. De hecho, 
# nada en Python hace posible imponer la ocultación de datos: todo se basa en 
# convenciones. (Por otro lado, la implementación de Python, escrita en C, 
# puede ocultar completamente los detalles de implementación y controlar el 
# acceso a un objeto si es necesario; esto puede ser usado por extensiones de 
# Python escritas en C).

# Los clientes deben usar los atributos de datos con cuidado: los clientes 
# pueden estropear las invariantes mantenidas por los métodos al estampar sus 
# atributos de datos. Tenga en cuenta que los clientes pueden agregar sus 
# propios atributos de datos a un objeto de instancia sin afectar la validez de 
# los métodos, siempre que se eviten los conflictos de nombres; nuevamente, 
# una convención de nomenclatura puede ahorrar muchos dolores de cabeza aquí.

# No existe una abreviatura para hacer referencia a atributos de datos 
# (¡u otros métodos!) desde dentro de los métodos. Encuentro que esto en 
# realidad aumenta la legibilidad de los métodos: no hay posibilidad de 
# confundir las variables locales y las variables de instancia al mirar un 
# método.

# A menudo, el primer argumento de un método se denomina self. Esto no es más 
# que una convención: el nombre self no tiene ningún significado especial para 
# Python. Tenga en cuenta, sin embargo, que al no seguir la convención, su 
# código puede ser menos legible para otros programadores de Python, y también 
# es concebible que se pueda escribir un programa de navegador de clase que se 
# base en tal convención.

# Cualquier objeto de función que sea un atributo de clase define un método 
# para instancias de esa clase. No es necesario que la definición de la función 
# se incluya textualmente en la definición de la clase: también está bien 
# asignar un objeto de función a una variable local en la clase. Por ejemplo:

# Función definida fuera de la clase
def f1(self, x, y):
    return min(x, x+y)

class C:
    f = f1

    def g(self):
        return 'hello world'

    h = g

# Ahora bien, 'f', 'g' y 'h' son todos atributos de la clase 'C' que se 
# refieren a objetos de función 'y', en consecuencia, todos son métodos de 
# instancias de C--h es exactamente equivalente a 'g'. Tenga en cuenta que 
# esta práctica generalmente solo sirve para confundir al lector de un 
# programa.

# Los métodos pueden llamar a otros métodos usando atributos de método del 
# argumento 'self':

class Bag:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def addtwice(self, x):
        self.add(x)
        self.add(x)

# Los métodos pueden hacer referencia a nombres globales de la misma manera que 
# las funciones ordinarias. El alcance global asociado con un método es el 
# módulo que contiene su definición. (Una clase nunca se usa como un ámbito 
# global). Si bien rara vez se encuentra una buena razón para usar datos 
# globales en un método, hay muchos usos legítimos del ámbito global: por un 
# lado, las funciones y los módulos importados al ámbito global pueden ser 
# utilizados por los métodos, así como las funciones y clases definidas en él. 
# Por lo general, la clase que contiene el método se define en sí misma en 
# este ámbito global, y en la siguiente sección encontraremos algunas buenas 
# razones por las que un método querría hacer referencia a su propia clase.

# Cada valor es un objeto y, por lo tanto, tiene una clase (también llamada 
# su tipo). Se almacena como 'object.__class__'.

#---------
# Herencia
#---------

# Por supuesto, una característica del lenguaje no merecería el nombre de 
# "clase" sin admitir la herencia. La sintaxis para una definición de clase 
# derivada se ve así:

'''
class NombreClaseDerivada(NombreClaseBase):
    <estatuto-1>
    .
    .
    .
    <estatuto-N>
'''
    
# El nombre 'NombreClaseBase' debe definirse en un ámbito que contenga la 
# definición de clase derivada. En lugar de un nombre de clase base, también 
# se permiten otras expresiones arbitrarias. Esto puede ser útil, por ejemplo, 
# cuando la clase base se define en otro módulo:

# --> class NombreClaseDerivada(nombremodulo.NombreClaseBase):

# La ejecución de una definición de clase derivada procede igual que para una 
# clase base. Cuando se construye el objeto de clase, se recuerda la clase base.
# Esto se usa para resolver referencias de atributos: si un atributo solicitado 
# no se encuentra en la clase, la búsqueda procede a buscar en la clase base. 
# Esta regla se aplica recursivamente si la propia clase base se deriva de 
# alguna otra clase.

# No hay nada especial en la creación de instancias de clases derivadas: 
# 'DerivedClassName()' crea una nueva instancia de la clase. Las referencias 
# de métodos se resuelven de la siguiente manera: se busca el atributo de clase 
# correspondiente, descendiendo por la cadena de clases base si es necesario, 
# y la referencia de método es válida si produce un objeto de función.

# Las clases derivadas pueden anular los métodos de sus clases base. Debido a 
# que los métodos no tienen privilegios especiales cuando llaman a otros métodos
# del mismo objeto, un método de una clase base que llama a otro método definido
# en la misma clase base puede terminar llamando a un método de una clase 
# derivada que lo invalida. (Para programadores de C++: todos los métodos en 
# Python son efectivamente virtuales).

# De hecho, un método de reemplazo en una clase derivada puede querer 
# extender en lugar de simplemente reemplazar el método de clase base del 
# mismo nombre. Hay una forma sencilla de llamar directamente al método de 
# la clase base: simplemente llame a BaseClassName.methodname(self, arguments).
# Esto es ocasionalmente útil para los clientes también. (Tenga en cuenta que
# esto solo funciona si se puede acceder a la clase base como BaseClassName 
# en el ámbito global).

# Python tiene dos funciones integradas que funcionan con herencia:

# --> 'Use isinstance()' para verificar el tipo de una instancia: 
# 'isinstance(obj, int)' será True solo si 'obj.__class__' es int o alguna 
# clase derivada de int.

# --> 'Use issubclass() para verificar la herencia de clases: 
# 'issubclass(bool, int)' es 'True' ya que 'bool' es una subclase de int. 
# Sin embargo, 'issubclass(float, int)' es 'False' ya que 'float' no es una 
# subclase de 'int'.

#------------------
# Herencia múltiple
#------------------

# Python también admite una forma de herencia múltiple. Una definición de 
# clase con múltiples clases base se ve así:

'''
class NombreClaseDerivada(Base1, Base2, Base3):
    <estatuto-1>
    .
    .
    .
    <estatuto-N>
'''
# Para la mayoría de los propósitos, en los casos más simples, puede pensar en 
# la búsqueda de atributos heredados de una clase principal como primero en 
# profundidad, de izquierda a derecha, sin buscar dos veces en la misma clase 
# donde hay una superposición en la jerarquía. Así, si un atributo no se 
# encuentra en DerivedClassName, se busca en Base1, luego (recursivamente) 
# en las clases base de Base1, y si no se encuentra ahí, se busca en Base2, 
# y así sucesivamente.

# De hecho, es un poco más complejo que eso; el orden de resolución del método 
# cambia dinámicamente para admitir llamadas cooperativas a super(). 
# Este enfoque se conoce en algunos otros lenguajes de herencia múltiple 
# como call-next-method y es más poderoso que la superllamada que se encuentra 
# en los lenguajes de herencia única.

# La ordenación dinámica es necesaria porque todos los casos de herencia 
# múltiple exhiben una o más relaciones de diamante (donde se puede acceder 
# a al menos una de las clases principales a través de múltiples rutas desde 
# la clase inferior). Por ejemplo, todas las clases heredan del objeto, por 
# lo que cualquier caso de herencia múltiple proporciona más de una ruta 
# para llegar al objeto. Para evitar que se acceda a las clases base más de 
# una vez, el algoritmo dinámico linealiza el orden de búsqueda de una manera 
# que conserva el orden de izquierda a derecha especificado en cada clase, 
# que llama a cada padre solo una vez y que es monótono (lo que significa 
# que una clase puede subclasificarse sin afectar el orden de precedencia 
# de sus padres). En conjunto, estas propiedades hacen posible diseñar 
# clases confiables y extensibles con herencia múltiple. Para obtener más 
# detalles, consulte https://www.python.org/download/releases/2.3/mro/.

#-------------------
# Variables privadas
#-------------------

# Las variables de instancia "privadas" a las que no se puede acceder excepto 
# desde dentro de un objeto no existen en Python. Sin embargo, existe una 
# convención que sigue la mayoría del código de Python: un nombre con un guión 
# bajo como prefijo (por ejemplo, _spam) debe tratarse como una parte 
# no pública de la API (ya sea una función, un método o un miembro de datos). 
# Debe considerarse un detalle de implementación y está sujeto a cambios sin
# previo aviso.

# Dado que existe un caso de uso válido para miembros privados de clase 
# (es decir, para evitar conflictos de nombres con nombres definidos por 
# subclases), existe un soporte limitado para dicho mecanismo, llamado
# manipulación de nombres. Cualquier identificador de la forma __spam 
# (al menos dos guiones bajos iniciales, como máximo un guión bajo final) 
# se reemplaza textualmente con _classname__spam, donde classname es el nombre 
# de la clase actual sin los guiones bajos iniciales. Esta manipulación se 
# realiza sin tener en cuenta la posición sintáctica del identificador, 
# siempre que ocurra dentro de la definición de una clase.

# La manipulación de nombres es útil para permitir que las subclases anulen 
# métodos sin interrumpir las llamadas a métodos intraclase. Por ejemplo:

class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update   # private copy of original update() method

class MappingSubclass(Mapping):

    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)

# El ejemplo anterior funcionaría incluso si 'MappingSubclass' introdujera un 
# identificador __update ya que se reemplaza con _Mapping__update en la 
# clase 'Mapping' y _MappingSubclass__update en la clase 'MappingSubclass' 
# respectivamente.

# Tenga en cuenta que las reglas de mutilación están diseñadas principalmente 
# para evitar accidentes; todavía es posible acceder o modificar una 
# variable que se considera privada. Esto incluso puede ser útil en 
# circunstancias especiales, como en el depurador.

# También tenga en cuenta que el código pasado a 'exec()' o' eval()' no 
# considera que el nombre de clase de la clase que invoca sea la clase actual;
# esto es similar al efecto de la declaración global, cuyo efecto también 
# está restringido al código que se compila en bytes juntos. La misma 
# restricción se aplica a 'getattr()', 'setattr()' y 'delattr()', así como 
# cuando se hace referencia a __dict__ directamente.

#-----------------
# ALgunos detalles
#-----------------

# A veces es útil tener un tipo de datos similar al "registro" de Pascal o la 
# "estructura" de C, que agrupa algunos elementos de datos con nombre. El 
# enfoque idiomático es usar clases de datos para este propósito:

from dataclasses import dataclass

@dataclass
class Employee:
    name: str
    dept: str
    salary: int

john = Employee('john', 'computer lab', 1000)
print(john.dept)
# --> 'computer lab'
print(john.salary)
# --> 1000
print()

# Una pieza de código de Python que espera un tipo de datos abstracto 
# particular a menudo se puede pasar a una clase que emula los métodos de 
# ese tipo de datos en su lugar. Por ejemplo, si tiene una función que 
# formatea algunos datos de un objeto de archivo, puede definir una clase 
# con los métodos 'read()' y 'readline()' que obtienen los datos de un búfer 
# de cadena y los pasan como argumento.

# Los objetos de método de instancia también tienen atributos: m.__self__ es 
# el objeto de instancia con el método 'm()', y m.__func__ es el objeto de 
# función correspondiente al método.

#-----------
# iteradores
#-----------

# A estas alturas, probablemente haya notado que la mayoría de los objetos 
# contenedores se pueden recorrer mediante una declaración 'for':

for element in [1, 2, 3]:
    print(element)
for element in (1, 2, 3):
    print(element)
for key in {'one':1, 'two':2}:
    print(key)
for char in "123":
    print(char)
# for line in open("myfile.txt"):
#    print(line, end='')
print()

# Este estilo de acceso es claro, conciso y conveniente. El uso de iteradores 
# impregna y unifica Python. Detrás de escena, la instrucción 'for' llama a 
# 'iter()' en el objeto contenedor. La función devuelve un objeto iterador que 
# define el método __next__() que accede a los elementos del contenedor de 
# uno en uno. Cuando no hay más elementos, __next__() lanza una excepción 
# 'StopIteration' que le dice al ciclo for que termine. Puede llamar al 
# método __next__() usando la función incorporada 'next()'; este ejemplo 
# muestra cómo funciona todo:

s = 'abc'
it = iter(s)
print(it)
# --> <str_iterator object at 0x10c90e650>
print(next(it))
# --> 'a'
print(next(it))
# --> 'b'
print(next(it))
# --> 'c'

# Lo siguiente generará un error, se acabaron los items
# print(next(it))
'''
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    next(it)
StopIteration
'''
print()

# Habiendo visto la mecánica detrás del protocolo del iterador, es fácil 
# agregar el comportamiento del iterador a sus clases. Defina un 
# método __iter__() que devuelva un objeto con un método __next__(). 
# Si la clase define __next__(), entonces __iter__() puede devolverse a 
# sí mismo:

class Reverse:
    """Iterador para recorrer una secuencia hacia atrás"""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

rev = Reverse('spam')
print(iter(rev))
# --> <__main__.Reverse object at 0x00A1DB50>

for char in rev:
    print(char)
# --> m
# --> a
# --> p
# --> s
print()

#------------
# Generadores
#------------

# Los generadores son una herramienta simple y poderosa para crear iteradores. 
# Están escritas como funciones regulares, pero usan la declaración de 'yield' 
# cuando quieren devolver datos. Cada vez que se llama a 'next()', el generador 
# continúa donde lo dejó (recuerda todos los valores de datos y qué declaración
# se ejecutó por última vez). Un ejemplo muestra que los generadores pueden 
# ser trivialmente fáciles de crear:

def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]

for char in reverse('golf'):
    print(char)

# --> f
# --> l
# --> o
# --> g
print()

# Todo lo que se puede hacer con generadores también se puede hacer con 
# iteradores basados ​​en clases, como se describe en la sección anterior. 
# Lo que hace que los generadores sean tan compactos es que los métodos
#  __iter__() y __next__() se crean automáticamente.

# Otra característica clave es que las variables locales y el estado de 
# ejecución se guardan automáticamente entre llamadas. Esto hizo que la 
# función fuera más fácil de escribir y mucho más clara que un enfoque que 
# utiliza variables de instancia como 'self.index' y 'self.data'.

# Además de la creación automática de métodos y el ahorro en estados del 
# programa, cuando los generadores finalizan, activan automáticamente 
# 'StopIteration'. En combinación, estas funciones facilitan la creación 
# de iteradores sin más esfuerzo que escribir una función regular.

#------------------------
# Expresiones generadoras
#------------------------

# Algunos generadores simples se pueden codificar de manera sucinta como 
# expresiones usando una sintaxis similar a las listas de comprensión pero 
# con paréntesis en lugar de corchetes. Estas expresiones están diseñadas 
# para situaciones en las que una función envolvente utiliza el generador 
# de inmediato. Las expresiones generadoras son más compactas pero menos 
# versátiles que las definiciones completas del generador y tienden a ser 
# más amigables con la memoria que las comprensiones de listas equivalentes.

# Ejemplos:

print(sum(i*i for i in range(10)))          # suma de cuadrados
# --> 285

xvec = [10, 20, 30]
yvec = [7, 5, 3]
print(sum(x*y for x,y in zip(xvec, yvec)))  # Producto punto
# --> 260

# unique_words = set(word for line in page  for word in line.split())

# valedictorian = max((student.gpa, student.name) for student in graduates)

data = 'golf'
print(list(data[i] for i in range(len(data)-1, -1, -1)))
# --> ['f', 'l', 'o', 'g']
print()


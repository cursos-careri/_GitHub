#-------------------------------------------------------------------------------
# # Cadenas ('strings')
#
# Notas creadas y editadas por: Sergio Fco. Hernández Machuca
# Xalapa, Veracruz, México
# 2023 - Julio
#
# La información proviene de diversas fuentes de internet, principalmente los 
# sitios oficiales del lenguaje Python (https://www.python.org) y Micropython 
# (https://micropython.org).
#-------------------------------------------------------------------------------

# Definiciones:
a = 'spam eggs'    # Comillas simples
print(a)
# --> spam eggs
b = 'doesn\'t'     # Uso de "\'" para escapar una comilla simple
print(b)
# --> "doesn't"
c = "doesn't"      # O usar dobles comillas
print(c)
# --> "doesn't"
# Otros ejemplos...
d = '"Yes," they said.'
print(d)
e = "\"Yes,\" they said."
print(e)
f = '"Isn\'t," they said.'
print(f)
print()

# Si no se desea que caracteres antecedidos por '\' sean interpretados como 
# caracteres especiales, se puede emplear cadenas crudas ('raw') agregando 'r' 
# antes de la primera comilla.
print('C:\nsome\name')  # Aquí, '\n' significa 'new line'
# --> C:\some
# --> ame
print(r'C:\some\name') # En esta opción ya está como debiera
# --> C:\some\name
print()

# Las cadenas se pueden concatenar con el operador '+' y repetirse con *:
# 3 veces 'un', seguido de 'ium'
print(3 * 'un' + 'ium')
# --> 'unununium'
print()

# Las cadenas pueden ser indexadas (subscritas), teniendo el primer carácter el 
# índice 0. En Python no existe el tipo 'char', un carácter es una cadena de 
# tamaño uno:
word = 'Python'
print(word[0])  # Carácter en posición 0
# --> 'P'
print(word[5])  # Carácter en posición 5
# --> 'n'
print()

# Los índices pueden ser también números negativos, para empezar a contar desde 
# el fin, la derecha:
print(word[-1])  # Último carácter
# --> 'n'
print(word[-2])  # Penúltimo carácter 
# --> 'o'
print(word[-6])
# --> 'P'
print()

# Además de indexamiento, también se puede realizar el rebanado ('slicing').
# Mientras el indexamiento se emplea para obtener elementos individuales, el 
# rebanado se usa para obtener subcadenas:
print(word[0:2])  # Caracteres desde la posición 0 (incluido) hasta la 2 (sin 
# incluirle)
# --> 'Py'
print(word[2:5])  # Caracteres desde la posición 2 (incluido) hasta la 5 (sin 
# incluirle)
# --> 'tho'
print()

# Los índices empleados en los cortes tienen valores por omisión interesantes.
# Si se omite el primer índice el valor por 'default' es '0', si se omite el 
# segundo índice, por 'default' se toma el tamaño de la cadena siendo rebanada.
print(word[:2])   # Caracteres desde el inicio hasta la posición 2, sin incluirle
# --> 'Py'
print(word[4:])   # Caracteres desde la posición 4, incluida, hasta el final
# --> 'on'
print(word[-2:])  # Caracteres desde la penúltima posición (incluyéndole) hasta 
# el final
# --> 'on'
print()

# Nótese que siempre se incluye el elemento de 'inicio' y siempre se excluye el 
# del final. Lo anterior asegura que s[:i] + s[i:] siempre será igual a s:
print(word[:2] + word[2:])
# --> 'Python'
print(word[:4] + word[4:])
# --> 'Python'
print()

# Una manera de recordar cómo funcionan los cortes ('slicing') es pensar que los 
# índices apuntan entre caracteres y no a los caracteres mismos, como se ilustra 
# a continuación. El extremo de la izquierda se numera como '0' para el primer 
# caracter, el extremo de la derecha del último caracter de la cadena de 'n' 
# caracteres tendrá el valor de 'n'.

'''
 +---+---+---+---+---+---+
 | P | y | t | h | o | n |
 +---+---+---+---+---+---+
 0   1   2   3   4   5   6
-6  -5  -4  -3  -2  -1
'''
# En el ejemplo la primera hilera de números da la posición de los índices, 
# de '0' a '6'. La segunda hilera da los índices negativos correspondientes. 
# La rebanada de 'i' a 'j' consiste en todos los caracteres entre los bordes 
# etiquetados 'i' y 'j' respectivamente.

# Para los índices no negativos, la longitud de la rebanada es la diferencia de los índices,
# si ambos están dentro de los límites. Por ejemplo, la longitud de word[1:3] es 2

# Si se intenta usar un índice que es demasiado grande se generará un error, por ejemplo:
# word[42]                             # ¡Error!: La cadena solo tiene 6 caracteres
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# IndexError: string index out of range

# Sin embargo, los índices para rebanadas son manejados con mayor soltura:
print(word[4:42])
# --> 'on'
print(word[42:])
# --> ''
print()

# Las cadenas no pueden ser cambiadas, son inmutables, asignar a una posición 
# indexada un valor en una cadena generará un error:
'''
word[0] = 'J'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
word[2:] = 'py'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
'''

# Si se requiere una cadena distinta, ésta se deberá crear:
k = 'J' + word[1:]
print(k)
# --> 'Jython'
l = word[:2] + 'py'
print(l)
# --> 'Pypy'
print()

# La función interna 'len()' regresa la longitud de la cadena:
s = 'supercalifragilisticexpialidocious'
print(len(s))
# --> 34

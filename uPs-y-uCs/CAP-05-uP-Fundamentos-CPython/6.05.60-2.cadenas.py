#-------------------------------------------------------------------------------
# Cadenas. Ejemplos del manual
# Referencia: https://docs.python.org/3.10/library/string.html?highlight=string#module-string
#
# Notas creadas y editadas por: Sergio Fco. Hernández Machuca
# Xalapa, Veracruz, México
# 2023 - Julio
#
# La información proviene de diversas fuentes de internet, principalmente los 
# sitios oficiales del lenguaje Python (https://www.python.org) y Micropython 
# (https://micropython.org).
#-------------------------------------------------------------------------------

"First, thou shalt count to {0}"  # References first positional argument
"Bring me a {}"                   # Implicitly references the first positional 
                                  # argument
"From {} to {}"                   # Same as "From {0} to {1}"
"My quest is {name}"              # References keyword argument 'name'
"Weight in tons {0.weight}"       # 'weight' attribute of first positional arg
"Units destroyed: {players[0]}"   # First element of keyword argument 'players'.

"Harold's a clever {0!s}"        # Calls str() on the argument first
"Bring out the holy {name!r}"    # Calls repr() on the argument first
"More {!a}"                      # Calls ascii() on the argument first


# Acceso a argumentos por posición:
print( '{0}, {1}, {2}'.format('a', 'b', 'c'))
print("- - -")
print('{}, {}, {}'.format('a', 'b', 'c'))
print("-----")
print('{2}, {1}, {0}'.format('a', 'b', 'c'))
print("- - -")
print('{2}, {1}, {0}'.format(*'abc'))      # Desempaquetamiento de la secuencia 
                                           # del argumento
print("-----")
print('{0}{1}{0}'.format('abra', 'cad'))   # Índices pueden ser repetidos
print()


# Acceso a argumentos por nombre:
print('Coordenadas: {latitude}, {longitude}'.format(latitude='37.24N', longitude='-115.81W'))
print("- - -")
coord = {'latitude': '37.24N', 'longitude': '-115.81W'}
print('Coordenadas: {latitude}, {longitude}'.format(**coord))
print()

''' No funciona con ESP32. Verificar 
# Acceso a argumentos por atributos:
c = 3-5j                  # Un número complejo
print(('El número complejo {0} tiene la parte real {0.real} y la parte imaginaria {0.imag}.').format(c))
print()


# Empleando una clase:
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def __str__(self):
        return 'Punto({self.x}, {self.y})'.format(self=self)

print(str(Point(4,2)))
print()

# Accediendo a elementos del argumento
coord = (3, 5)
print('X: {0[0]} ; Y: {0[1]}'.format(coord))
print()
'''

# Reemplazando %s y %r:
print("repr() muestra comilla: {!r}; str() ya no: {!s}".format('test1', 'test2'))
print("repr() muestra comilla: 'test1'; str() ya no: test2")
print()

# Alineando el texto y especificando el ancho
print('{:<30}'.format('alineado a la izquierda'))
print('{:>30}'.format('alineado a la derecha'))
print('{:^30}'.format('centrado'))
print('{:*^30}'.format('centrado'))        # Utiliza a '*' como relleno
print()

# Reemplazando %+f, %-f, y % f y especificando un signo:
print('{:+f}; {:+f}'.format(3.14, -3.14))  # Muéstralo siempre
print('{: f}; {: f}'.format(3.14, -3.14))  # Muestra un espacio para números 
                                           # positivos
print('{:-f}; {:-f}'.format(3.14, -3.14))  # Muestra sólo el signo de menos -- 
                                           # igual que '{:f}; {:f}'
print()

# Reemplazando %x y %o y convirtiendo valores a distintas bases:
# El formateo también soporta números binarios
print("int: {0:d};  hex: {0:x};  oct: {0:o};  bin: {0:b}".format(42))
print("int: {0:d};  hex: {0:#x};  oct: {0:#o};  bin: {0:#b}".format(42))
print()

# Usando la coma como separador de miles:
print('{:,}'.format(1234567890))
print()

# Expresando porcentaje:
puntos = 19
total = 22
print('Respuesta correcta: {:.2%}'.format(puntos/total))

# Usando formateo específico para el tipo de variable:
# Para CPython ensaye usar lo siguiente:
# import datetime

# Para uPython:
# from machine import RTC

# rtc = RTC()
# d = rtc.datetime((2017, 8, 23, 1, 12, 48, 0, 0)) # Ajuste de una fecha y hora 
                                                 # específica
# print(rtc.datetime())

# print('{:%Y-%m-%d %H:%M:%S :%S:%S}'.format(rtc.datetime()))

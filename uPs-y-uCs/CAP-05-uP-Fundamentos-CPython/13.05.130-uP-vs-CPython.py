#-------------------------------------------------------------------------------
# Diferencias entre MicroPython y CPython
#
# Notas creadas y editadas por: Sergio Fco. Hernández Machuca
# Xalapa, Veracruz, México
# 2023 - Julio
#
# La información proviene de diversas fuentes de internet, principalmente los 
# sitios oficiales del lenguaje Python (https://www.python.org) y Micropython 
# (https://micropython.org).
#-------------------------------------------------------------------------------

# La siguiente información es tomada del sitio oficial de Micropython.
# La referencia es: https://docs.micropython.org/en/latest/genrst/index.html 

print()
# MicroPython implementa Python 3.4 y algunas características selectas de 
# Python 3.5 y superiores. Las siguientes secciones describen el estado actual
# de estas funciones.

# Pitón 3.5
# Pitón 3.6
# Pitón 3.7
# Pitón 3.8
# Pitón 3.9
# Pitón 3.10

'''
Para las funciones de Python implementadas por MicroPython a veces hay 
diferencias en su comportamiento, en comparación con Python estándar. 

Las operaciones enumeradas en las secciones a continuación producen 
resultados contradictorios en MicroPython en comparación con Python estándar.

#----------#
# Sintaxis #
#----------#

--> El desempaquetado de argumentos no funciona si el argumento que se 
desempaqueta es el argumento 'n' o mayor, donde 'n' es el número de bits en un 
MP_SMALL_INT.

--> MicroPython permite usar := para asignar a la variable de una comprensión, 
CPython lanza un 'SyntaxError'.

--> uPy requiere espacios entre números literales y palabras clave, CPy no

--> Los escapes de nombres Unicode no están implementados

#------------------------------
# Parte Principal del Lenguaje
#------------------------------

#--> 'f-strings' no admite la concatenación con literales adyacentes si los 
# literales adyacentes contienen llaves o son 'f-strings'

#--> 'f-strings' no puede admitir expresiones que requieran análisis para 
# resolver llaves y corchetes anidados desequilibrados

#--> No se admiten 'f-strings' 'raw' (crudas) sin procesar

#--> 'f-strings' no admite conversiones del tipo '!a'

#--> El método especial __del__ no está implementado para clases definidas 
# por el usuario

#--> El Orden de Resolución de Método (MRO) no cumple con CPython

#--> Cuando se hereda de varias clases, super() solo llama a una clase

# --> Llamar a la propiedad 'getter super()' en la subclase devolverá un objeto de propiedad, no el valor

# --> Los mensajes de error para los métodos pueden mostrar recuentos de argumentos inesperados

# --> Los objetos de función no tienen el atributo __module__

# --> Los atributos definidos por el usuario para funciones no son soportados

# --> El administrador de contexto __exit__() no es llamado en un generador que no se ejecuta hasta el final

$ --> Las variables locales no están incluidas en el resultado locals()

# --> El código que se ejecuta en la función eval() no tiene acceso a las variables locales

# El segmento '__all__' no es compatible con '__init__.py' en MicroPython.

# --> El atributo __path__ de un paquete tiene un tipo diferente (cadena única en lugar de una lista de cadenas) en MicroPython

# --> MicroPython no admite paquetes de espacio de nombres divididos en el sistema de archivos.

# Los Tipos integrados son:
 Exceptionn
 bytearray
 bytes
 dict
 float
 int
 list
 str
 tuple

 # Los Módulos son:

 array
 builtins
 deque
 json
 os
 random
 estruct
 sys
'''

# Referir a - recursos - memoria en particular - velocidad de procesamiento -
#           -              
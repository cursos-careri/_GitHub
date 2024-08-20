#-------------------------------------------------------------------------------
# 1.05.10 Introducción a Python. Primeros elementos.
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
Nota: Este y los documentos anexos se pueden leer en IDEs del lenguaje Python, 
como 'Thonny' o 'Visual Studio Code'. De acuerdo con la extensión del archivo 
(por ejemplo *.txt, *.pdf ó *.py) éste se puede leer o ejecutar.

#-------------------------------------------------------------------------------

- Introducción a uPython a partir de Python.

- CPython es el Python regular, para máquinas de escritorio y laptops.

- Los ejemplos que se presentan deberán funcionar para ambas versiones.

- Palabras Reservadas
- Variables
- Tipos
- Secuencias
- Diccionarios
- Estructuras de Control
- Funciones
- Objetos

#-------------------------------------------------------------------------------
Usar el Tutorial de Python que ofrece el sitio oficial:
The Python Tutorial: https://docs.python.org/3.12/tutorial/index.html 

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

2.05.20 Palabras Reservadas. No deben usarse para declarar variables, 
constantes, funciones, módulos o elementos en Python.
- En 'Thonny' las palabras reservadas aparecen destacadas en relación con 
comentarios, variables y otros elementos.

En CPython las palabras reservadas son:

False      await      else       import     pass
None       break      except     in         raise
True       class      finally    is         return
and        continue   for        lambda     try
as         def        from       nonlocal   while
assert     del        global     not        with
async      elif       if         or         yield

Revisar: https://docs.python.org/es/3/reference/lexical_analysis.html?highlight=palabras%20reservadas
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

3.05.30 Comentarios

- Para una línea, se emplea el símbolo '#'
- Para un segmento se usa ''' cerrando con '''. También se puede usar comillas
normales
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

4.05.40 Variables y Tipos

- Las variables no requieren asignarse a algún tipo en particular, mantienen el
tipo del valor con el que son asociadas.

- Los Tipos interconstruidos (los que están definidos en Python desde su
instalación) son: numéricos, secuencias, mapeos, clases, instancias y 
excepciones.

- Sólo se pueden realizar operaciones con elementos del mismo tipo.

Numéricos: int, float
Secuencias: listas, tuplas, rangos
String: Es del tipo secuencia de texto

- Problemas al asignar una variable de un tipo a una variable de otro tipo.

- Lo siguiente se ve bien. Se infiere el tipo de las variables por el valor
asignado.
'''


#>>> a = 12
#>>> b = 15
#>>> a + b 
#27

Ahora mezclar con otros tipos (cadena, flotante) y verificar que sucede.

#>>> a = 34
#>>> b = 15
#>>> c = "1"
#>>> a+c 
'''
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can't convert 'int' object to str implicitly
>>> 

Para poder hacer lo anterior (por alguna razón) se emplea el 'casting'.
- 'Casting' Conversión de un tipo de variable a otro tipo de variable.
'''

#>>> a = 34
#>>> b = 15
#>>> c = "1"
#>>> a + int(c)
#35

#- Operación con cadenas:
#>>> a = "Hola "
#>>> b = "Mundo"
#>>> a+b 
#'Hola Mundo'
#>>> 

#- Otra operación de 'casting'
#>>> a = "Hola "
#>>> b = "Mundo "
#>>> c = 2
#>>> a + b + c 
'''
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can't convert 'int' object to str implicitly
'''

#>>> 
#>>> a + b + str(c)
#'Hola Mundo 2'
#>>> 

'''
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
5.05.50 Operadores para elementos de Tipo Numérico

- Consultarlos en: https://docs.python.org/3/library/stdtypes.html 

- Operadores de comparaciones: https://docs.python.org/3/library/stdtypes.html

- Operaciones (Métodos) para cadenas.

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
6.05.60 Cadenas y Formato

Referencia: https://docs.python.org/3.10/library/string.html?highlight=string#module-string

- Ejemplos de operaciones con cadenas de caracteres.

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
7.05.70 Listas, Tuplas, Rangos

Mutable: Una vez creado, puede ser cambiado posteriormente, contrario a 
inmutable. Se crea con '[]'

Con estos tipos se permite almacenar múltiples elementos con un mismo nombre.

- Listas: Conjunto de valores de variables, secuencias, mutables. Los elementos
de una lista pueden ser de distinto tipo.

- Tuplas: son secuencias de elementos, inmutables, pueden contener elementos de
distinto tipo. Se crea con '()'. Al crear una tupla de un elemento se debe 
añadir una coma al final.

- Rangos: Es una secuencia de números, inmutable. Se usan para el conteo en 
ciclos o lazos. 

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
'''
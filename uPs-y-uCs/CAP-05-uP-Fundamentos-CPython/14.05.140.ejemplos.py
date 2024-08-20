#-------------------------------------------------------------------------------
# Ejemplos
#
# Notas creadas y editadas por: Sergio Fco. Hernández Machuca
# Xalapa, Veracruz, México
# 2023 - Julio
#
# La información proviene de diversas fuentes de internet, principalmente los 
# sitios oficiales del lenguaje Python (https://www.python.org) y Micropython 
# (https://micropython.org).
#-------------------------------------------------------------------------------

#========================================================================
# Serie de Fibonacci:
# La suma de los dos elementos actuales definen al próximo:
a, b = 0, 1

while a < 10:
    print(a)
    a, b = b, a+b
print("------------------------------")

# Impresión de un argumento
i = 256*256
print('El valor de i es', i)
print("------------------------------")

# Impresión con cierto elemento terminal
a, b = 0, 1
while a < 1000:
    print(a, end=',')
    a, b = b, a+b

print()
print("------------------------------")
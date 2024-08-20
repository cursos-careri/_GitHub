#******************************************************************************
# Menú orientado a consola. Se ejecuta en Python de PC
# Tareas:
#  1) Adecuar este programa para ejecutarse en Micropython.
#  2) Incluir avisos más explícitos en respuesta a selecciones (sonido).
#  3) Realizar acciones (actuadores): LEDs, Motores, Etc.
#  4) Realizar lecturas de variables (sensores): Temperatura, Presión, Etc.
#  5) Utilice una pantala (LCD, OLED o TFT) para interactuar junto con
#     elementos de selección (encodificador rotativo, joystick, teclado, Etc.)
#  6) Aplique el esquema de Menú en un sistema electrónico en particular.
#==============================================================================

# Incorporamos el parámetro para mostrar el nombre del menú
# la 'f' en la impresión indica que se imprimirán valores de VARIABLES
def mostrar_menu(nombre, opciones): 
    print(f'# {nombre}')				# Imprime letrero del __menú
    print('   Seleccione opción: ')		# 'Seleecione su Opción'
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]}')

def leer_opcion(opciones):
    # 'input()' lee del teclado de la PC, sustituir esto para el uC
    # Pueden ser caracteres '+', '-', 'Enter', etcétera.
    while (a := input('Opción: ')) not in opciones:
        print('Opción incorrecta, vuelva a intentarlo.')
    return a								# Regresa el valor leído

def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()

# incorporamos el parámetro para mostrar el nombre del menú
def generar_menu(nombre, opciones, opcion_salida):  
    opcion = None
    while opcion != opcion_salida:
        mostrar_menu(nombre, opciones)		# Imprime el Menú
        opcion = leer_opcion(opciones)		# Lee del teclado / Encoder
        ejecutar_opcion(opcion, opciones)	# Ejecuta lo seleccionado
        print()								# ...continúa

#=============================================================================
#---[ ESTRUCTURA del MENÚ ]---
#=============================================================================

def menu_principal():
    opciones = {
        '1': ('LEDs On >', submenu1),  # Acción de una llamada a un...
        '2': ('Opción 2 >', submenu2),  #  submenu que genera un...
        '3': ('Opción 3 >', submenu3),  #  nuevo menú
        '4': ('Opción 4 >', submenu4),
        'x': ('Salir', salir)
    }
    generar_menu('-Sistema Básico uC-', opciones, 'x')  # Nombre del menú
#------------------------------------------------------------------------------

def submenu1():
    opciones = {
        'r': ('ROJO', funcion1),
        'v': ('VERDE', funcion2),
        'a': ('AMARILLO', funcion3),        
        'z': ('AZUL', funcion4),
        'x': ('Salir', salir)
    }
    generar_menu('ENCENDER', opciones, 'x')  # Nombre del submenú
#------------------------------------------------------------------------------
def submenu2():
    opciones = {
        'e': ('Opción e', funcionE),
        'f': ('Opción f', funcionF),
        'g': ('Opción g', funcionG),
        'd': ('Volver al menú principal', salir),
    }
    generar_menu('Submenú', opciones, 'd')  # Nombre del submenú
#------------------------------------------------------------------------------
def submenu3():
    opciones = {
        'i': ('Opción i', funcionI),
        'j': ('Opción j >', submenu3_1),
        'd': ('Volver al menú principal', salir),
    }
    generar_menu('Submenú', opciones, 'd')  # Nombre del submenú
#------------------------------------------------------------------------------
def submenu4():
    opciones = {
        '1': ('Motor A', funcionMotor),
        '2': ('Motor A', funcionMotor),
        '3': ('Motor A', funcionMotor),
        'x': ('SALIR', salir),
    }
    generar_menu('Submenú', opciones, 'x')  # Nombre del submenú
#------------------------------------------------------------------------------
def submenu3_1():
    opciones = {
        'k': ('Opción k', funcionK),
        'd': ('Volver al menú ', salir),
    }
    generar_menu('Submenú', opciones, 'd')  # Nombre del submenú
#------------------------------------------------------------------------------
#---[ ACCIONES ]
#------------------------------------------------------------------------------
# A partir de aquí creamos las funciones que ejecutan las ACCIONES a invocar
#---[ FUNCIONES para LEDs ]---
def funcion1():
    print('Enciende LED Rojo')
def funcion2():
    print('Enciende LED Verde')
def funcion3():
    print('Enciende LED Amarillo')
def funcion4():
    print('Enciende LED Azul')
#-----------------------------------------
def funcionA():
    print('Enciende LED Azul')
def funcionB():
    print('Has elegido la opción B')
def funcionC():
    print('Has elegido la opción C')
def funcionE():
    print('Has elegido la opción A')
def funcionF():
    print('Has elegido la opción A')
def funcionG():
    print('Has elegido la opción A')
def funcionI():
    print('Has elegido la opción I')
def funcionJ():
    print('Has elegido la opción J')
def funcionK():
    print('Has elegido la opción K')
def funcionMotor():
    print('Algo con los motores')
def salir():
    print('-= REPOSO =-')

#------------------------------------------------------------------------------
if __name__ == '__main__':
    menu_principal() # iniciamos el programa mostrando el menú principal
#******************************************************************************
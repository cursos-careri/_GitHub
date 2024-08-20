# --> Programa del parpadeo de un LED

from machine import Pin
from utime import sleep

# El LED interconstruido para el módulo DEV KIT1 está en la terminal '2'
led = Pin(2, Pin.OUT)	# Creación de objeto LED en una terminal,'salida'

# Estructura cíclica
while True:
	led.on()			# Encendido del LED 
	sleep(0.5)			# Retardo de tiempo (en segundos)
	led.off()			# Apagado del LED
	sleep(0.5)			# Retardo de tiempo
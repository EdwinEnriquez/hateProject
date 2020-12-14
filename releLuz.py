import RPi.GPIO as GPIO
import time
#Limpiar GPIO Salidas y suprimir error
GPIO.setwarnings(False)
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)

# configurar pin para relevador
GPIO.setup(4, GPIO.OUT)

#Encender Rele
GPIO.output(4, True)
#mantener encendido por 30min
time.sleep(1800)
#apagar rele
GPIO.output(4, False)

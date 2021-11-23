import RPi.GPIO as GPIO, time
import Adafruit_DHT  
import time

# Configuración de puertos
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN)


# Uso DHT
sensor = Adafruit_DHT.DHT22
pin = 4

while True:
# DHT11
    humedad, temperatura = Adafruit_DHT.read_retry(sensor, pin)

    print ('Humedad: ' , humedad)
    print ('Temperatura: ' , temperatura)
  


import RPi.GPIO as GPIO, time
import Adafruit_DHT  
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN)

while True:
  sensor = Adafruit_DHT.DHT22
  pin = 4
  humedad, temperatura = Adafruit_DHT.read_retry(sensor, pin)

  print ('Humedad: ' , humedad)
  print ('Temperatura: ' , temperatura)
 
  time.sleep(1) 

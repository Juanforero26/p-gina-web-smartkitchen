
import RPi.GPIO as GPIO
import Adafruit_GPIO.SPI as SPI
import Adafruit_DHT  
import paho.mqtt.publish as publish
from time import sleep
from datetime import datetime
now = datetime.now()

GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN)
GPIO.setup(17, GPIO.OUT)

sensor = Adafruit_DHT.DHT22
pin = 4
buzzer = 17
servo  = 20
while True:
   
    # DHT11
    humedad, temperatura = Adafruit_DHT.read_retry(sensor, pin)

    print ('Humedad: ' , humedad)
    print ('Temperatura: ' , temperatura)
   
    # Alarma Buzzer
    sleep(0.1)
    if humedad > 70:
        GPIO.output(buzzer,True)
      
        sleep(1)
        GPIO.output(buzzer,False)
        sleep(1)
        
        
    if temperatura > 70:
        GPIO.output(buzzer,True)
     
        sleep(2)
        GPIO.output(buzzer,False)
        sleep(1)
        
    if temperatura > 76:
        GPIO.output(servo,True)
     
        sleep(60)
        GPIO.output(servo,False)
        sleep(1)
    
            
    # Almacenamiento de variables
    Temperatura = temperatura
    Humedad = humedad
    
    # Creación del Topic de Thingspeak
    topic = "channels/"+"1520384"+"/publish/"+"LJ0BAWDO79UXX3XO"

    # Creación del mensaje 
    mensaje = "field1="+str(Temperatura)+"&field2="+str(Humedad)+str(now)
    try:
        publish.single(topic,payload=mensaje,hostname="mqtt.thingspeak.com",port=1883,tls=None,transport="tcp")
    except:
        print("Error 404")
    sleep(1)

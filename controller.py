





import mqtt
import ntptime
from machine import Pin
from time import sleep, time
relay = Pin(2, Pin.OUT)
ntptime.host = "1.europe.pool.ntp.org"

def apri(orario):
  relay(1)
  print("aperto")
  fields_data = {
    'field1' : "0",
    'field2' : orario
  }
  sleep(2 * 60)
  mqtt.Post_MQTT(fields_data)
  relay(0)

def execute():
  while True:
    print("ok")
    valori = mqtt.Get_MQTT()
    aperto = valori["aperto"]
    data = valori["data"]
    orario = valori["orario"]
    print(orario)
    orario_s = orario.replace('.', ':')
    print ("Aperto: " + str(aperto) + " Orario: " + str(orario_s) + " Data: " + str(data))
    print (aperto)
    fields_data = {
      'field1' : aperto,
      'field2' : orario
    }
    if orario_s == data[11:16] or aperto == "1":
      apri(orario)
    else:
      mqtt.Post_MQTT(fields_data)
    sleep(5)







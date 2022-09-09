



import machine
import urequests 
import json
 
def Post_MQTT(fields):
  HTTP_HEADERS = {'Content-Type': 'application/json'} 
  THINGSPEAK_WRITE_API_KEY = "H3QE60HLMPT4217Y"
  request = urequests.post( 
    'http://api.thingspeak.com/update?api_key=' +
    THINGSPEAK_WRITE_API_KEY, 
    json = fields, 
    headers = HTTP_HEADERS )  
  request.close() 
  print(fields) 
 
def Get_MQTT():
  x = urequests.get(url = 'https://api.thingspeak.com/channels/1824879/feeds.json?api_key=Y63WBDLLDI1EHZP1&results=1')  
  dictionary = json.loads(x.text)
  #print (dictionary)
  aperto = dictionary['feeds'][0]['field1']
  data = dictionary['feeds'][0]['created_at']
  orario = dictionary['feeds'][0]['field2']
  id = dictionary['feeds'][0]['entry_id']
  #print ("Orario: "  + orario  + "\n")
  #print ("Aperto: "  + str(aperto) + "\n")
  dic = {"aperto" : aperto, "orario" : orario, "data": data, "id" : id} 
  x.close() 
  print(dic)
  return dic






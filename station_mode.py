import network

def connection():
  wlan = network.WLAN(network.STA_IF)
  wlan.active(True)
  if not wlan.isconnected():
    print('connecting to network...')
    wlan.connect('FASTWEB-HA9REQ', '7EEDFJN6XG')
    while not wlan.isconnected():
      pass
  print('network config:', wlan.ifconfig())
  return wlan.ifconfig()[0] 



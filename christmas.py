import time
import os

presents = false #there are no service requests

while True:

  # turn off power to usb ports
  if presents == false:
    os.system("sudo ./uhubctl -p 2 -a 0")
  
  #turn on power to usb ports
  if presents == true:
    os.system("sudo ./uhubctl -p 2 -a 1")
  
  #test blinking
  if presents == false:
    presents = true
    
  else:
    presents = false
  
  time.sleep(5) #sleep for 5 seconds

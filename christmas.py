# when there are no service requests available the website displays
# "No ResNet Pilikia are currently open. Please check again later."
# <p style="font-size:18px">No ResNet Pilikia are currently open. Please check again later.</p>
# twill
# https://github.com/ctb/twill/blob/master/doc/python-api.txt
# example
# http://code.activestate.com/recipes/577465-web-testing-using-twill/

# twill documentation site down
#https://web.archive.org/web/20181114022639/http://twill.idyll.org/

# go <url> -- visit the given URL. The Python function returns the final URL visited, after all redirects.

#http://lists.idyll.org/pipermail/twill/2006-August/000526.html

import time
import os
from twill import get_browser
from twill.commands import *

presents = false #there are no service requests

b = get_browser()
b.go("https://resnet.hawaii.edu/pilikia/login")
b.formvalue(1, 'q', username) # might be fv()?
b.formvalue(2,'q',password)
b.submit('submit')
# need to click on the phone button
#submit()

while True:
  
  # reload the page
  b.reload()
  # check if there are any service requests
  try:
    find('<p style="font-size:18px">No ResNet Pilikia are currently open. Please check again later.</p>')
  except Exception as e:
      print e
      presents = true
  
  # turn off power to usb ports
  if presents == false:
    os.system("sudo ./uhubctl -p 2 -a 0")
  
  #turn on power to usb ports
  if presents == true:
    os.system("sudo ./uhubctl -p 2 -a 1")
  
  #test blinking
  
  #if presents == false:
  #  presents = true
    
  #else:
  #  presents = false
  
  # maybe just set presents to false at the end of every loop
  time.sleep(5) #sleep for 5 seconds

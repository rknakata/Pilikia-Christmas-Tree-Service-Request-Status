# Pilikia Status Light

# This program runs on a raspberry pi and uses the pilikia api that can be found
# at https://resnet.hawaii.edu/pilikia/check
# The API returns a 1 if there is a new request that has no communication or
# work logs open

import pycurl
import time
import os
from StringIO import StringIO


while True: # loops around every 5 seconds
    # curl the pilikia api

    url = 'https://resnet.hawaii.edu/pilikia/check'
    storage = StringIO()
    c = pycurl.Curl()
    c.setopt(c.URL, url)
    c.setopt(c.WRITEFUNCTION, storage.write)
    c.perform()
    c.close()
    content = storage.getvalue()
    print(content)

    presents = content
    # insert curl for result
    #try:
        #presents = curl for result
    #except Exception as e:
        #print(e)
        # change the color of the light to an error light after so many times restart the device

    # turn off power to the usb ports
    if presents == "0":
        print("The grinch is here")
        #os.system("sudo ./uhubctl -p 2 -a 0") # this is for using christmas tree

    # turn on power to the usb ports
    elif presents == "1":
        print("Its christmas!")
        #os.system("sudo ./uhubctl -p 2 -a 1") # this is for using christmas tree

    else:
        print("An error has occured invalid response recieved")
        # restart the device or change the color of the Light
    time.sleep(5)

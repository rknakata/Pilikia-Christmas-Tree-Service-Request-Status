# Pilikia Status Light

# This program runs on a raspberry pi and uses the pilikia api that can be found
# at https://resnet.hawaii.edu/pilikia/check
# The API returns a 1 if there is a new request that has no communication or
# work logs open

# To turn off power to the christmas tree power to the USB ports are disabled using UHUBCTL
# https://github.com/mvp/uhubctl


import requests
import time

while True: # loops around every 5 seconds
    # curl the pilikia api

    r = requests.get('https://resnet.hawaii.edu/pilikia/check')
    print("Curl Results for https://resnet.hawaii.edu/pilikia/check")
    print(r.content)

    type(r.content)

    print("just show the body delete")
    print(r.content)

    if '0' in str(r.content):
        print("The grinch is here")
        #os.system("sudo ./uhubctl -p 2 -a 0") # this is for using christmas tree

    elif '1' in str(r.content):
        print("Its Christmas")
        #os.system("sudo ./uhubctl -p 2 -a 1") # this is for using christmas tree

    else:
        print("this should not be hit '1'Turn the christmas tree on") # this should not be hit
        #make the tree blink to indicate an error has occured
        # restart the device maybe?

    time.sleep(5)

#!/usr/bin/env python

import time
import os
import urllib.request

def connected():
    try:
        urllib.request.urlopen('http://google.com') #Python 3.x
        return True
    except:
        return False


IsConnected = True
Counter = 0
print("Verifying Wi-Fi Status for electricity outage...")

while IsConnected :    
        IsConnected = connected()
        if IsConnected:
        # If WiFi is connected, check again in 5 seconds
            time.sleep(5)
            print("\n* ok *")
            Counter += 1
            if Counter == 5:
                Counter = 0
                print("\nVerifying Wi-Fi Status for electricity outage...")
        
        else:
        # Shutdown OS
            IsConnected = False
            print("Internet Disconnected!\nShutting down!!! Good Bye...")
            time.sleep(10)
            os.system("sudo shutdown -h now")

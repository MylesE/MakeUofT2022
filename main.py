import RPi.GPIO as GPIO

from pn532 import *
import codecs
import time

from api_call import *

def getAlbumURI(sensor):
        uri = "s"
        for i in range(6,15):
            data = sensor.ntag2xx_read_block(i)
            uri += codecs.decode(data, 'UTF-8')
        uri += str(sensor.ntag2xx_read_block(15))[12:14]
        return uri
    

if __name__ == '__main__':
    try:
        pn532 = PN532_SPI(debug=False, reset=20, cs=4)
        #pn532 = PN532_I2C(debug=False, reset=20, req=16)
        #pn532 = PN532_UART(debug=False, reset=20)

        ic, ver, rev, support = pn532.get_firmware_version()
        print('Found PN532 with firmware version: {0}.{1}'.format(ver, rev))

        # Configure PN532 to communicate with MiFare cards
        pn532.SAM_configuration()

        printMsg = True
        while (True):
            if printMsg == True:
                print('Waiting for playlist card')
                printMsg = False
            # Check if a card is available to read
            uid = pn532.read_passive_target(timeout=0.5)
            # Try again if no card is available.
            if uid is None:
               continue
            
            uri = getAlbumURI(pn532)
            
#             uri = "s"
#             for i in range(6,15):
#                 data = pn532.ntag2xx_read_block(i)
#                 uri += codecs.decode(data, 'UTF-8')
#             uri += str(pn532.ntag2xx_read_block(15))[12:14]
            
            printMsg = True
            doAction(uri)
            #playAlbum(uri)
            time.sleep(2)
        
    except Exception as e:
        print(e)
    finally:
        GPIO.cleanup()



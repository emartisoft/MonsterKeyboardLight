
# pip install hidapi

"""
Distributed under the terms of the MIT License.
Created on Apr, 25, 2021
@author: emarti, Murat Ozdemir
@comment: Set mono color for Monster Laptop Keyboard Light
@usage: python3 keyboardlight.py <RED> <GREEN> <BLUE> <BRIGHTNESS>

<RED> <GREEN> <BLUE> 0...255
<BRIGHTNESS> 0...50
"""

import hid
import sys

vendor_id = 0x048d
product_id = 0xce00

if (len(sys.argv)-1) != 4:
    print ("Set mono color for Monster Laptop Keyboard Light")
    print ("Usage: python3 keyboardlight.py <RED> <GREEN> <BLUE> <BRIGHTNESS>")
    print ("")
    print ("<RED> <GREEN> <BLUE> 0...255")
    print ("<BRIGHTNESS> 0...50")
    print ("example:")
    print ("to set color white => RED=255, GREEN=255, BLUE=255")
    print ("to set brightness  => BRIGHTNESS=20")
    print ("python3 keyboardlight.py 255 255 255 20")
    sys.exit()

R=sys.argv[1]
#print ("RED: %s" % R)
G=sys.argv[2]
#print ("GREEN: %s" % G)
B=sys.argv[3]
#print ("BLUE: %s" % B)
BR=sys.argv[4]
#print ("BRIGHTNESS: %s" % BR)
brightness=int(BR)
if brightness > 50:
    brightness=50
       
monsterKeyboardLight = hid.device()
monsterKeyboardLight.open(vendor_id, product_id) 

#print("Manufacturer: %s" % h.get_manufacturer_string())
# Manufacturer: ITE Tech. Inc.
#print("Product: %s" % h.get_product_string())
# Product: ITE Device(8291)

monsterKeyboardLight.set_nonblocking(0x01)

for x in range(0x08):
    monsterKeyboardLight.send_feature_report([0x14, 0x00, x+1, int(R), int(G), int(B), 0x00, 0x00])
    monsterKeyboardLight.send_feature_report([0x08, 0x02, x+1, 0x05, brightness, 0x08, 0x00, 0x01])
    
monsterKeyboardLight.close()



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
from tkinter import *

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
    
splashWindow = Tk()
x=(splashWindow.winfo_screenwidth() - 640)/2
y=(splashWindow.winfo_screenheight() - 275)/2

splashWindow.geometry('640x275+%d+%d' % (x, y))
splashWindow.title("Monster Keyboard Mono Light")
#splashWindow.resizable(False, False)

mk_png = PhotoImage(file='/Applications/MonsterKeyboard/monsterkeyboard.png')
splashLabel = Label(splashWindow, text = "Monster Keyboard Mono Light", image=mk_png)
splashLabel.pack()

splashWindow.overrideredirect(1)
splashWindow.overrideredirect(0) 
     
def setMonoLight():
    vendor_id = 0x048d
    product_id = 0xce00
    
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
    
    splashWindow.destroy()

splashWindow.after(3000, setMonoLight)
mainloop()


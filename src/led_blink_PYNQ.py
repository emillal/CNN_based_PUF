from time import sleep
from pynq.overlays.base import BaseOverlay
base = BaseOverlay("base.bit")

led0 = base.leds[0] #LED LD0
led1 = base.leds[1] #LED LD1
led2 = base.leds[2] #LED LD2
led3 = base.leds[3] #LED LD3

sw0 = base.switches[0] #switch0
sw1 = base.switches[1] #switch1

while(True): 
    if (sw0.read() == True):   
        led0.on()             
        led1.on()             
    else:
        led0.off()            
        led1.off()       
    
    if (sw1.read() == True):  
        led2.on()              
        led3.on()              
    else:
        led2.off()           
        led3.off()            
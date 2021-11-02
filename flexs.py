
import time #Import time
import RPi.GPIO as GPIO #GPIO will be referred as GPIO only
 
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
 

 
binarys = (10,9,11,5,6,13,19,26) #Array of pin numbers connect to DB0-DB7
 
 
bits = [0,0,0,0,0,0,0,0] #resulting values of 8-bit data
 
 
for binary in binarys:
    GPIO.setup(binary, GPIO.IN) #All binary pins are input pins
    
  #Trigger pin 
    GPIO.setup(22, GPIO.OUT) #WR and INTR pins are output
 

 

print("Flex Sensor with")

print("Raspberry Pi1")
time.sleep(2)

 
while 1:
 
    decimal = Voltage = 0 #intitialize to zero
    print("Raspberry Pi2")
    GPIO.output(22, 1) #Turn ON Trigger
    time.sleep(0.1)
    GPIO.output(22, 0) #Turn OFF Trigger
    for i in range(8):
        if(GPIO.input(binarys[i]) == True):
            bits[i] = 1
        if(GPIO.input(binarys[i]) == False):
            bits[i] = 0      
    for i in range(8):
        decimal = decimal + (bits[i] * (2**(7-i)))
    print('D=')
    print(decimal)
    Voltage = decimal * 19.63 *0.001 #one unit is 19.3mV
    if (Voltage>3.8):
        print("Bent Forward")
    elif (Voltage<3.5):
        print("Bent Backward")
    else:
        print("Stable")
    Voltage = str(round(Voltage,2)) #limit to two digit after decimal
    print("V="); 
    print(Voltage)
    time.sleep(0.5) #relaxing time

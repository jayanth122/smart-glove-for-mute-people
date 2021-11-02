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
while 1:
    decimal = 0 #intitialize to zero
    GPIO.output(22, 1) #Turn ON Trigger
    time.sleep(0.1)
    GPIO.output(22, 0) #Turn OFF Trigger
#Read the input pins and update result in bit array
    for i in range(8):
        if(GPIO.input(binarys[i]) == True):
            bits[i] = 1
        if(GPIO.input(binarys[i]) == False):
            bits[i] = 0
    for i in range(8):
        decimal = decimal + (bits[i] * (2**(7-i)))
    print ( decimal)
    time.sleep(0.5) #relaxing time

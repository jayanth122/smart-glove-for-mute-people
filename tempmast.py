import time
import pygame
import Adafruit_ADXL345
import RPi.GPIO as pins
import serial as S1

ser = S1.Serial('/dev/ttyACM0', 9600)
pygame.init()

lhello = pygame.mixer.Sound('hellow.wav')
hello = pygame.mixer.Sound('/home/pi/Voices/hellofinal.wav')
rfine = pygame.mixer.Sound('finew.wav')
thankyou = pygame.mixer.Sound('/home/pi/Voices/thankyoufinal.wav')
move = pygame.mixer.Sound('/home/pi/Voices/moveasidefinal.wav')
bye = pygame.mixer.Sound('/home/pi/Voices/byefinal.wav')
give = pygame.mixer.Sound('/home/pi/Voices/pleasegiveittomefinal.wav')

lhello.play()
time.sleep(3)
#rfine.play()
#time.sleep(8)
#hello.play()
#time.sleep(10)

accel = Adafruit_ADXL345.ADXL345()

         
while True:
    # Read the X, Y, Z axis acceleration values and print them.
    x, y, z = accel.read()
    print('X={0}, Y={1}, Z={2}'.format(x, y, z))
    
    line = ser.readline()
    for s in line.split():
        if s.isdigit():
            f=int(s)      
    print(f)
    if(f>800):
        print('sensor1:',f)
        text='"Please come here"'
        print(text)
    if (x<=100 and x>=-100 and z<=100 and z>=-100 and y<=300 and y>=200):
        #move.play()
        
        pins.setmode(pins.BOARD) ## GPIO is being programmed

        pins.setup(40,pins.OUT) ## initialize digital pin40 as an output

        pins.output(40,pins.HIGH) ## turn the LED ON

        time.sleep(1) ## sleep for a second

        pins.output(40,pins.LOW) ## pins.cleanup empties all the output pins.

        time.sleep(1) ##sleep for a second

        pins.output(40,pins.HIGH) ## turn the LED ON

        time.sleep(1) ## sleep for a second

        pins.output(40,pins.LOW) ## pins.cleanup empties all the output pins.

        time.sleep(1) ##sleep for a second

        pins.output(40,pins.HIGH) ## turn the LED ON

        time.sleep(1) ## sleep for a second

        pins.output(40,pins.LOW) ## pins.cleanup empties all the output pins.

        time.sleep(1) ##sleep for a second

        pins.cleanup()

        time.sleep(2)
        
    elif (x<=100 and x>=-100 and z<=100 and z>=-100 and y>=-300 and y<=-200):
        thankyou.play()
        time.sleep(2)
    elif (y<=100 and y>=-100 and z<=100 and z>=-100 and x>=200 and x<=300):
        hello.play()
        time.sleep(2)
    elif (x<=100 and x>=-100 and y<=100 and y>=-100 and z>=200 and z<=300):
        #give.play()
        
        pins.setmode(pins.BOARD) ## GPIO is being programmed

        pins.setup(40,pins.OUT) ## initialize digital pin40 as an output

        pins.output(40,pins.HIGH) ## turn the LED ON

        time.sleep(1) ## sleep for a second

        pins.output(40,pins.LOW) ## pins.cleanup empties all the output pins.

        time.sleep(1) ##sleep for a second

        pins.output(40,pins.HIGH) ## turn the LED ON

        time.sleep(1) ## sleep for a second

        pins.output(40,pins.LOW) ## pins.cleanup empties all the output pins.

        time.sleep(2)
        
    elif (y<=100 and y>=-100 and z<=100 and z>=-150 and x>=-300 and x<=-200):
        bye.play()
        time.sleep(2)
    # Wait half a second and repeat.
    #time.sleep(2)


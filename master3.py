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

vit = pygame.mixer.Sound('/home/pi/Voices/Vitap is the best.wav')
washroom = pygame.mixer.Sound('/home/pi/Voices/Which way is the washroom.wav')
thank = pygame.mixer.Sound('/home/pi/Voices/thank you.wav')
plshelp = pygame.mixer.Sound('/home/pi/Voices/Please help me.wav')
giveit = pygame.mixer.Sound('/home/pi/Voices/please give it to me.wav')
hola = pygame.mixer.Sound('/home/pi/Voices/Hello.wav')
gbye = pygame.mixer.Sound('/home/pi/Voices/goodbye.wav')
excuse = pygame.mixer.Sound('/home/pi/Voices/Excuse me.wav')
congo = pygame.mixer.Sound('/home/pi/Voices/Congratulations.wav')
atb = pygame.mixer.Sound('/home/pi/Voices/All the Best.wav')

hola.play()
time.sleep(3)
#rfine.play()
#time.sleep(8)
#hello.play()
#time.sleep(10)

accel = Adafruit_ADXL345.ADXL345()

mode = 1

while True:

    if mode == 1:
    
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

            if (f<800 and x<=100 and x>=-100 and z<=100 and z>=-100 and y<=300 and y>=200): # left
                excuse.play()
                time.sleep(2)
                
            elif (f<800 and x<=100 and x>=-100 and z<=100 and z>=-100 and y>=-300 and y<=-200): # Right
                thankyou.play()
                time.sleep(2)

            elif (f<800 and y<=100 and y>=-100 and z<=100 and z>=-100 and x>=200 and x<=300): # hello
                hola.play()
                time.sleep(2)

            elif (f<800 and x<=100 and x>=-100 and y<=100 and y>=-100 and z>=200 and z<=300): # Give
                giveit.play()
                time.sleep(2)
                
            elif (f<800 and y<=100 and y>=-100 and z<=100 and z>=-150 and x>=-300 and x<=-200): # Come
                gbye.play()
                time.sleep(2)
            
            ## Finger Bent

            elif (f>800 and x<=100 and x>=-100 and z<=100 and z>=-100 and y<=300 and y>=200): # left
                pins.setmode(pins.BOARD) ## GPIO is being programmed

                pins.setup(40,pins.OUT) ## initialize digital pin40 as an output

                pins.output(40,pins.LOW) ## turn the LED ON

                pins.cleanup()
                
                time.sleep(2)

            elif (f>800 and x<=100 and x>=-100 and z<=100 and z>=-100 and y>=-300 and y<=-200): # Right
                pins.setmode(pins.BOARD) ## GPIO is being programmed

                pins.setup(40,pins.OUT) ## initialize digital pin40 as an output

                pins.output(40,pins.HIGH) ## pins.cleanup empties all the output pins.
                
                time.sleep(2)

            elif (f>800 and y<=100 and y>=-100 and z<=100 and z>=-100 and x>=200 and x<=300): # hello
                washroom.play()
                time.sleep(2)

            elif (f>800 and x<=100 and x>=-100 and y<=100 and y>=-100 and z>=200 and z<=300): # Give
                vit.play()
                time.sleep(2)

            elif (f>800 and y<=100 and y>=-100 and z<=100 and z>=-150 and x>=-300 and x<=-200): # Come
                plshelp.play()
                time.sleep(2)
                mode = 2
                break
            # Wait half a second and repeat.
            #time.sleep(2)
            
    elif mode == 2:
    
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

            if (f<800 and x<=100 and x>=-100 and z<=100 and z>=-100 and y<=300 and y>=200): # left
                move.play()
                time.sleep(2)
                
            elif (f<800 and x<=100 and x>=-100 and z<=100 and z>=-100 and y>=-300 and y<=-200): # Right
                thankyou.play()
                time.sleep(2)

            elif (f<800 and y<=100 and y>=-100 and z<=100 and z>=-100 and x>=200 and x<=300): # hello
                hola.play()
                time.sleep(2)

            elif (f<800 and x<=100 and x>=-100 and y<=100 and y>=-100 and z>=200 and z<=300): # Give
                giveit.play()
                time.sleep(2)
                
            elif (f<800 and y<=100 and y>=-100 and z<=100 and z>=-150 and x>=-300 and x<=-200): # Come
                gbye.play()
                time.sleep(2)
            
            ## Finger Bent

            elif (f>800 and x<=100 and x>=-100 and z<=100 and z>=-100 and y<=300 and y>=200): # left
                pins.setmode(pins.BOARD) ## GPIO is being programmed

                pins.setup(40,pins.OUT) ## initialize digital pin40 as an output

                pins.output(40,pins.LOW) ## turn the LED ON

                pins.cleanup()
                
                time.sleep(2)

            elif (f>800 and x<=100 and x>=-100 and z<=100 and z>=-100 and y>=-300 and y<=-200): # Right
                pins.setmode(pins.BOARD) ## GPIO is being programmed

                pins.setup(40,pins.OUT) ## initialize digital pin40 as an output

                pins.output(40,pins.HIGH) ## pins.cleanup empties all the output pins.
                
                time.sleep(2)

            elif (f>800 and y<=100 and y>=-100 and z<=100 and z>=-100 and x>=200 and x<=300): # hello
                washroom.play()
                time.sleep(2)

            elif (f>800 and x<=100 and x>=-100 and y<=100 and y>=-100 and z>=200 and z<=300): # Give
                vit.play()
                time.sleep(2)

            elif (f>800 and y<=100 and y>=-100 and z<=100 and z>=-150 and x>=-300 and x<=-200): # Come
                plshelp.play()
                time.sleep(2)
                mode = 1
                break
            
            # Wait half a second and repeat.
            #time.sleep(2)

import serial as S1
import time
ser = S1.Serial('/dev/ttyACM0', 9600)

while 1:
    line = ser.readline()
    for s in line.split():
        if s.isdigit():
            f=int(s)      
    print(f)
    if(f>800):
        print('sensor1:',f)
        text='"Please come here"'
        print(text)
    


import math 
from nanpy import (ArduinoApi,SerialManager) 
import serial #for the sensor input function for the snsory control
from nanpy import Servo 
import time 
import pyttsx # For the speech synthesys function speaking function enable 
import sklearn 
import csv 
engine = pyttsx.init()
#voices = engine.getProperty('voices')
#for voice in voices:
 #    engine.setProperty('voice',voice.id)
  #   print voice.id
# Servo input function 

servo =  Servo(2)  # Finger 1
servo2 = Servo(3) # Finger 2 
servo3 = Servo(4) # Finger 3 
servo4 = Servo(5) # Finger 4 
servo5 = Servo(6) # Finger 5 
servo6 = Servo(9) # Finger 6
 
Handfinger = SerialManager('/dev/ttyACM0',115200) 
Handcontrol = ArduinoApi(connection=Handfinger) 
try:
  Sensorserial = serial.Serial("/dev/ttyUSB0",115200) # Serial communication for the sensors serial 
except: 
  print("Sensors serial failure please check the sensors serial port") 
while True: 
     #delimeter split the data from the  serial communication system 
   try:
     Sensory = Sensorserial.readline() 
     Sensory.split(",")  
     Sensorydata = Sensory.split(",")  # Splitting the sensors 
     Sensor1_feild_sense = Sensorydata[0]
     Sensor2_feild_sense = Sensorydata[1] 
     Sensor3_feild_sense = Sensorydata[2]
     Sensor4_feild_sense = Sensorydata[3] 
     Sensor5_feild_sense = Sensorydata[4]
     Sensor6_feild_sense = Sensorydata[5]
     print('Sensor1:'+Sensor1_feild_sense)
     print('Sensor2:'+Sensor2_feild_sense)
     print('Sensor3:'+Sensor3_feild_sense)
     print('Sensor4:'+Sensor4_feild_sense)
     print('Sensor5:'+Sensor5_feild_sense)
     print('Sensor6:'+Sensor6_feild_sense)
     Mem1 = {0,23,434}
     Mem1.add(int(Sensor1_feild_sense))
     Mem1.add(int(Sensor2_feild_sense))
     Mem1.add(int(Sensor3_feild_sense))
     Mem1.add(int(Sensor4_feild_sense))
     Mem1.add(int(Sensor5_feild_sense))
     Mem1.add(int(Sensor6_feild_sense))
     print(Mem1)
     print("Sensor1 expected value :")
     print(765 in Mem1) 
     print("Sensor2 expected value :")
     print(4095 in Mem1)
     # Sensor1 condition working control application  
     if int(Sensor1_feild_sense) >= 600:
        #if 4095 in Mem1 == "True":
          engine.say('I feel touch ')
          engine.runAndWait()
          for move in [45,90]:      
            servo.write(move) 
            servo2.write(move+20)
            servo3.write(move+30)
            servo4.write(90-move)  
            servo5.write(move+10)
            servo6.write(move-30)
            print("finger1 Angle:"+ str(move)) 
            time.sleep(0.1) 
          
     else: 
         print("Sensor1 feild sense waiting status......."+ "[" +str(Sensor1_feild_sense) + "]") 
         print("Sensor2 feild sense waiting status......."+ "[" +str(Sensor2_feild_sense) + "]")
         print("Sensor3 feild sense waiting status......."+ "[" +str(Sensor3_feild_sense) + "]") 
         print("Sensor4 feild sense waiting status......."+ "[" +str(Sensor4_feild_sense) + "]")
         print("Sensor5 feild sense waiting status......."+ "[" +str(Sensor5_feild_sense) + "]") 
         print("Sensor6 feild sense waiting status......."+ "[" +str(Sensor6_feild_sense) + "]")
   except:
     print("Error sensoryfunction") 
    
          
    

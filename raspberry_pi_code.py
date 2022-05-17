#Code to read data from serial port and send it to alexa via flask 
#Developed by Shebin Jose Jacob

from flask import Flask  
from flask_ask import Ask, statement  
import requests  import json  
import serial 
ser = serial.Serial("/dev/ttyACM0", 9600)  #change here for your serial port
app = Flask(__name__)  ask = Ask(app, '/') 
@ask.launch 
@ask.intent("Check")   
if (ser.read()==1)   
def yes():   
 return statement("New mail has arrived , Check it soon")   
else    
def no():      
 return statement("No mails yet")   
if __name__ == "__main__":   
app.run(debug=True) 
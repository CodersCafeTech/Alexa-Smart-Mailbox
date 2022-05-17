#Code to read data from proximity sensor
#Developed by Shebin Jose Jacob


int sensor = 5;  
int mail   = 0; 
void setup() { 
 pinMode(sensor, INPUT);  
 Serial.begin(9600);  
}
void loop() {
 mail = digitalRead(sensor); 
 if(mail == 1) {  
   Serial.write(1);              # returns 1 if mail is present 
   } 
 else{   
 Serial.write(0);                # returns 0 if mail is not present
   }
}
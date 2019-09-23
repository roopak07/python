int led = 13;
char mydata=0;
// the setup routine runs once when you press reset:
void setup() {                
  // initialize the digital pin as an output.
  pinMode(led, OUTPUT);     
    Serial.begin(9600);
}
// the loop routine runs over and over again forever:
void loop() {
   mydata = int(Serial.read());

if (mydata=='1') 
  digitalWrite(led, HIGH);   // turn the LED on (HIGH is the voltage level)
 
  if(mydata=='0')
  digitalWrite(led, LOW);    // turn the LED off by making the voltage LOW
}

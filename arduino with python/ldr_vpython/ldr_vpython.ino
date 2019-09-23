int ir;
void setup() {
  Serial.begin(9600);
}


void loop() {
  
  int ir = analogRead(A0);
  int val=map(ir,0,1023,0,20);
  int val1=20-val;  
  Serial.println(val1);
  delay(500);        // delay in between reads for stability
} 

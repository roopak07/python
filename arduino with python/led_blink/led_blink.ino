int data;
void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
pinMode(LED_BUILTIN,OUTPUT);
digitalWrite(LED_BUILTIN, LOW);
Serial.println("HI!, I am Arduino");
}

void loop() {
  // put your main code here, to run repeatedly:
while (Serial.available())
{
  data = Serial.read();
}
if(data=='1')
digitalWrite(LED_BUILTIN, HIGH);

else if(data == '0')
digitalWrite(LED_BUILTIN, LOW);
}

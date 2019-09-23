void setup() {
Serial.begin(9600);
}
void loop() {
int potvalue=analogRead(A0);
Serial.print("pot values:");
Serial.println(potvalue);
}

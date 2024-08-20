/*
 Reads an analog input on pin 0,1,2, maps it to 1-255 and writes it to the 
 serial port.
 Attach the center pin of a potentiometer to pin A0, and the outside pins to 
 +5V and ground. Same for A1 and A2.
 */

int in[] = { 0, 0, 0, 0 };

void setup() {
  Serial.begin(57600);  // Initialize serial communication at 57600 bits 
                        // per second
}

//=============================================================================
void loop() {
  for (int i = 0; i < 2; i++)  // Read the input on analog pin 0-2
  {
    in[i] = analogRead(i);
    in[i] = map(in[i], 0, 1023, 1, 255);
    delay(10);
  }

  Serial.write(0);  // De limits the packet, tells Processing where the data 
                    // packet starts
  delay(1);

  for (int i = 0; i < 2; i++)  // Writes the array to the serial port
  {
    Serial.write(in[i]);
    delay(1);  // Delay in between writes for stability
  }

  Serial.write(in[1]);  // Processing code is expecting 4 bytes so this is just a dummy for now
  Serial.write(in[1]);
}
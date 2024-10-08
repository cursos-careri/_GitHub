import processing.serial.*;

Serial port;  // Create object from Serial class
float val;    // Data received from the serial port

void setup() {
  size(440, 220);
  // IMPORTANT NOTE:
  // The first serial port retrieved by Serial.list()
  // should be your Arduino. If not, uncomment the next
  // line by deleting the // before it. Run the sketch
  // again to see a list of serial ports. Then, change
  // the 0 in between [ and ] to the number of the port
  // that your Arduino is connected to.
  printArray(Serial.list());
  String arduinoPort = Serial.list()[1];
  port = new Serial(this, arduinoPort, 57600);
}

void draw() {
  
  if (port.available() > 0) { // If data is available,
    val = port.read();        // read it and store it in val
    println(val);             // Verificar qué está llegando a Processing
    val = map(val, 0, 255, 0, height);  // Convert the value
  }
  rect(40, val-10, 360, 20);
}

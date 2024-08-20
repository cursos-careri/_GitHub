import processing.serial.*;

Serial myPort;           // Create object from Serial class
char [] inVal = new char[4];      // Data received from the serial port
PFont f;
Dial dialA, dialB;
Bar barA;
Map mapA;
int i = 0;

void setup ()
{
  frameRate(100);
  size (1000, 800);

  // println (Serial.list());
  printArray (Serial.list());
  String portName = Serial.list()[1];
  myPort = new Serial(this, portName, 57600);

  dialA = new Dial (300, 180, 180, 0, 100, "RPM x 100");
  dialB = new Dial (300, 540, 180, 0, 180, "Oil Temp C");
  barA = new Bar (850, 40, 500, 0, 10, "Presión Aceite");
  mapA = new Map (100, 400, 300);
}

void draw()
{
  background(220);
  fill(255, 0, 0);
  noStroke();
  if (myPort.available() > 0)
  inVal [0] = myPort.readChar();
  if (inVal [0] == '#')
  while (i < 4)
  {
    if (myPort.available() > 0)
    {
      inVal[i] = myPort.readChar();  // read it and store it in inVal
      i++;
    }
  }

  dialA.display(inVal[0]);
  dialB.display (inVal[1]);
  barA.display (inVal[2]);
  mapA.display (20, 150);
  println (inVal[0]);
  println (inVal[1]);
  println (inVal[2]);
  println (inVal[3]);
  i = 0;
}

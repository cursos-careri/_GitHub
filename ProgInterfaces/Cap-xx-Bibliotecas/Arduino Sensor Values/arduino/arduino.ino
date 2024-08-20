#include "DHT.h"
#define DHTPIN 2       //connect DHT data pin to D2
#define DHTTYPE DHT11  // DHT 11
DHT dht(DHTPIN, DHTTYPE);
float temp = 0;
float hum = 0;
int pot = A0;
int potvalue;

void setup() {
  Serial.begin(9600);
  pinMode(pot, INPUT);
  pinMode(DHTPIN, OUTPUT);
  dht.begin();  //Begins to receive Temperature and humidity values.
}

void loop() {
  temp = dht.readTemperature();

  hum = dht.readHumidity();
  potvalue = analogRead(pot);
  int potvalue1 = map(potvalue, 0, 1023, 0, 100);
  Serial.print(temp);
  Serial.print(",");
  Serial.print(hum);
  Serial.print(",");
  Serial.print(potvalue1);

  delay(200);
}
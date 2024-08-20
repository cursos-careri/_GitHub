void setup() {
  size(480, 120);
  stroke(0, 102);
}

void draw() {
  float peso = dist(mouseX, mouseY, pmouseX, pmouseY);
  println(peso);
  strokeWeight(peso);
  line(mouseX, mouseY, pmouseX, pmouseY);
}

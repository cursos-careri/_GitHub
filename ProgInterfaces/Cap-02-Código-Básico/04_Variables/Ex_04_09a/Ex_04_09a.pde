
void setup() {
  size(480, 120);
  strokeWeight(2);
}

void draw() {
  for (int i = 20; i < 400; i += 20) {
    stroke((random(255)), (random(255)), (random(255)));
    line(i, 0, i + i/2, 80);
    line(i + i/2, 80, i*1.2, 120);
  }
}

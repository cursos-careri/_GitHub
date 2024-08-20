
int factor;

void setup() {
  size(480, 120);
  strokeWeight(2);
}

void draw() {
  background(102);
  for (int i = 20; i < 400; i += 20) {
    factor = mouseX;
    if (factor == 0) {
      factor = 1;
    }
    line(i, 0, i + i/factor, 80);
  }
}

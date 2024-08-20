

size(480, 120);
background(0);
fill(255);
stroke(102);

for (int y = 20; y <= height-20; y += 10) {  // Altura
  for (int x = 20; x <= width-20; x += 10) { // A la derecha
    ellipse(x, y, 8, 12);                    // Dibujado del círculo
    // Dibujado de una línea desde el centro de cada círculo
    line(x, y, 240, 60);
  }
}

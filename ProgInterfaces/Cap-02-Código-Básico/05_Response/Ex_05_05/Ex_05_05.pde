//-------------------------------------------------------------------------
void setup() {
  size(480, 120);  // Lienzo.
  fill(0, 102);    // Relleno, color negro, alpha de 102.
  noStroke();      // No dibujar las líneas.
}
//-------------------------------------------------------------------------
void draw() {
  background(204);                // "Repinta" el fondo en cada "frame".
  ellipse(mouseX, mouseY, 9, 9);  // Dibuja en donde está el 'mouse'.
}

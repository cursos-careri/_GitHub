// Dibujado de un búho

void setup() {
  size(480, 120);              // Tamaño del lienzo
}

void draw() {
  background(176, 204, 226);  // Fondo
  // Mueve el origen de (0,0) a 110 coordenadas a la derecha y
  // 110 coordenadas hacia abajo. Ahora el (0,0) está abajo.
  // --> En 'X', más positivo a la derecha
  // --> En 'Y', más positivo para abajo
  // Todo lo que continúa se hace relativo a la coordenada (0,0)
  translate(110, 110);        // Corrimiento
  stroke(138, 138, 125);      // Color del lápiz
  strokeWeight(70);           // Grosor del lápiz
  
  line(0, -35, 0, -65);       // Cuerpo 
  noStroke();
  
  
  /*
  fill(255);
  ellipse(-17.5, -65, 35, 35); // Domo del ojo izquierdo
  ellipse(17.5, -65, 35, 35);  // Domo del ojo derecho 
  arc(0, -65, 70, 70, 0, PI);  // Barbilla
  fill(51, 51, 30);
  
  ellipse(-14, -65, 8, 8);     // Ojo izquierdo
  ellipse(14, -65, 8, 8);      // Ojo derecho
  quad(0, -58, 4, -51, 0, -44, -4, -51); // Pico
  */
}

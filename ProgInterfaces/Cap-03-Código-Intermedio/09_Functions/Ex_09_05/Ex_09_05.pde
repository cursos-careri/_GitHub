//=============================================================================
// Dibujado de dos búhos con una función
// Autor: SFHM (adaptación, comentarios) 
// Fecha: 2023/08/28
//=============================================================================

//---[SECCIÓN AJUSTES]---
void setup() {
  size(480, 120);
}

//---[SECCIÓN DIBUJADO]---
void draw() {
  background(176, 204, 226);
  owl(110, 110);
  owl(180, 110);
}

//-----------------
//---[FUNCIONES]---
//-----------------
//------------------------------------
// Función para el dibujado de un búho
// Argumentos:
//   Posición (x,y)
//   Agregar el cambio de color
//------------------------------------
void owl(int x, int y) {
  
  pushMatrix();                // Preserva el 'Sistema de Coordenadas' actual
  
  translate(x, y);
  stroke(138, 138, 125);
  strokeWeight(70);
  
  line(0, -35, 0, -65);        // Cuerpo
  noStroke();
  
  fill(255);
  ellipse(-17.5, -65, 35, 35); // Parte del ojo
  ellipse(17.5, -65, 35, 35);  // Parte del ojo
  arc(0, -65, 70, 70, 0, PI);  // Barbilla
  
  fill(51, 51, 30);
  ellipse(-14, -65, 8, 8);         // Ojo
  ellipse(14, -65, 8, 8);          // Ojo
  quad(0, -58, 4, -51, 0, -44, -4, -51); // Pico
  
  popMatrix();                // Restaura el 'Sistema de Coordenadas' previo
}

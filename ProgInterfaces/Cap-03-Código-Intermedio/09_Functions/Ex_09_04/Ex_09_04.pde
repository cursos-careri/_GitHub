//=============================================================================
// Hechura de dos búhos, cada uno por separado
// Autor: SFHM (adaptación, comentarios)
// Fecha: 2023/08/2028
//=============================================================================

//-----------------------
//---[SECCIÓN AJUSTES]---
//-----------------------
void setup() {
  size(480, 120);
}

//--------------------------------
//---[SECCIÓN DIBUJADO CÍCLICO]---
//--------------------------------
void draw() {
  background(176, 204, 226);
  
  // Búho de la izquierda
  translate(110, 110);          //
  
  stroke(138, 138, 125);
  strokeWeight(70);
  
  line(0, -35, 0, -65);         //
  noStroke();
  
  fill(255);
  ellipse(-17.5, -65, 35, 35); // 
  ellipse(17.5, -65, 35, 35);  // 
  arc(0, -65, 70, 70, 0, PI);  // 
  
  fill(51, 51, 30);
  ellipse(-14, -65, 8, 8);     // 
  ellipse(14, -65, 8, 8);      // 
  quad(0, -58, 4, -51, 0, -44, -4, -51); // 
  
  // Búho de la derecha
  // Ahora nos mevemos 70 pixeles a la derecha
  translate(70, 0);
  
  stroke(138, 138, 125);
  strokeWeight(70);
  
  line(0, -35, 0, -65);         //
  noStroke();
  
  fill(255);
  ellipse(-17.5, -65, 35, 35);  // 
  ellipse(17.5, -65, 35, 35);   // 
  arc(0, -65, 70, 70, 0, PI);   // 
  
  fill(51, 51, 30);
  ellipse(-14, -65, 8, 8);      // 
  ellipse(14, -65, 8, 8);       // 
  quad(0, -58, 4, -51, 0, -44, -4, -51); // 
}

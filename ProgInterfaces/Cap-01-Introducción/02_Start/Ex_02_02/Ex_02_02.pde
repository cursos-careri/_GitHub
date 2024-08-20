//*****************************************************************************
// Un ejemplo de programa genérico.
//
// Realize cambios en cada línea, observe cómo se modifican los elementos
// que se dibujan, su color y ubicación.
//=============================================================================

//-----[ AJUSTE INICIAL ]-----
void setup() {
  size(480, 120);      // Tamaño del lienzo (ventana) en donde se dibuja 
}

//-----[ IMPRESIÓN en PANTALLA CÍCLICA ]
void draw() {
  if (mousePressed) {   // ¿Está oprimido el botón del Mouse?
    fill(0);            // El relleno de la figura es de color negro
  } else {              //... no está oprimido el botón
    fill(255);          // El relleno es blanco
  }
  ellipse(mouseX, mouseY, 80, 80);  // Dibujar el círcuo en esta posición
}
//*****************************************************************************

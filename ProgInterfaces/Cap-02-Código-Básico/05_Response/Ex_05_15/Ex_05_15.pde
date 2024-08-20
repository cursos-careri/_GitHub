
int x = 80;        // Coordanada esuperior del rectángulo 'X'
int y = 30;        // Coordenada en 'Y'
int w = 80;        // Ancho del rectángulo (a lo largo, varía 'x')
int h = 60;        // Alto del rectángulo (a lo alto, varía 'y')

void setup() {
  size(240, 120);
}

void draw() {
  background(204);  // Se pinta el lienzo de nuevo
  
  // Si está 'a la derecha' del inicio del rectángulo (a lo largo de 'x')
  // o está 'a la izquierda' del fin del rectángulo (a lo largo de 'x')
  if ((mouseX > x) && (mouseX < x+w) && // Y ADEMÁS...
    // Si está 'abajo del tope' a lo alto (recorrido a lo largo de 'y')
    // o está 'arriba del tope' a lo alto (recorrido a lo largo de 'y')
    (mouseY > y) && (mouseY < y+h)) {
    fill(0,0,255);          // Se rellena de AZUL
  } else {                  //... si no sucediera lo anterior...        
    fill(255,0,0);          // Se rellena de ROJO
  }
  rect(x, y, w, h);         // Ahora se traza el rectángulo con el 
                            // relleno antes seleccionado
}

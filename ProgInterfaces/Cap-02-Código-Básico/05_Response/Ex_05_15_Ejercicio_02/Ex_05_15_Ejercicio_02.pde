//*************************************************************************
// Ejercicio para identificar zonas con el paso del apuntador del mouse
//*************************************************************************
//-----[ VARIABLES GLOBALES ]-----
int x = 80;        // Coordenada "X" del vértice superior izquierdo de Botón-1
int y = 30;        // Coordenada en "Y"
int x1 = 170;      // Coordenada "X" del vértice superior izquierdo de Botón-2
int y1 = 30;       // Coordenada en "Y"
int x2 = 260;      // Coordenada "X" del vértice superior izquierdo de Botón-3
int y2 = 30;       // Coordenada en "Y"
int w = 80;        // Ancho común de los botones
int h = 60;        // Alto común de los botones

int paso = 0;      // Identifica por cuál lugar se ha pasado. En experimento.
//----------------------------------------------------------------------------------
void setup() {
  size(480, 320);
  textSize(64);
  textAlign(CENTER);
}
//----------------------------------------------------------------------------------
void draw() {
  background(204);
  // Verifica si el apuntador del mouse está en la zona rectangular
  if ((mouseX > x) && (mouseX < x+w) && (mouseY > y) && (mouseY < y+h)) {
    paso = 1;              // Identificador de etapa
    fill(0, 255, 0);       // Relleno
    rect(x, y, w, h);      // Impresión de la figura
    if (keyPressed) {      // ¿Se oprimió alguna tecla?
      text(key, x+40, y+120);
    } else {
      ;
    }
  } else {
    fill(255, 0, 0);         // Cambio del relleno
    rect(x, y, w, h);        // Impresión de la figura
  }

  // Verifica si el apuntador del mouse está en la zona rectangular
  if ((mouseX > x1) && (mouseX < x1+w) && (mouseY > y1) && (mouseY < y1+h)) {
    fill(0, 255, 0);
    rect(x1, y1, w, h);
    if (keyPressed) {      // ¿Se oprimió alguna tecla?
      text(key, x+40, y+120);
    } else {
      ;
    }
  } else {
    fill(255, 0, 0);
    rect(x1, y1, w, h);
  }
  // Verifica si el apuntador del mouse está en la zona rectangular
  if ((mouseX > x2) && (mouseX < x2+w) && (mouseY > y2) && (mouseY < y2+h)) {
    fill(0, 255, 0);
    rect(x2, y2, w, h);
    if (keyPressed) {      // ¿Se oprimió alguna tecla?
      text(key, x+40, y+120);
    } else {
      ;
    }
  } else {
    fill(255, 0, 0);
    rect(x2, y2, w, h);
  }
}

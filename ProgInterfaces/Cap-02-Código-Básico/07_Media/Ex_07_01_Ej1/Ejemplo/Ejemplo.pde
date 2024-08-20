//*****************************************************************************
// Ejemplo para el cargado de imágenes en una ventana. Pasos a seguir:
//
// 1. Agregar la imagen a la carpeta 'data' del sketch.
// 2. Crear una variable 'PImage' para almacenar la imagen.
// 3. Cargar la imagen con la función loadImage().
//
// Después se emplea la función  image() para colocar la imagen.
//
//=============================================================================
//---[ VARIABLES ]---
PImage img;

//-----[ AJUSTES ]-----
void setup() {
  size(480, 120);
  img = loadImage("lunar.jpg");
}

//-----[ LAZO PRINCIPAL ]-----
void draw() {
  image(img, 0, 0);
}
//*****************************************************************************
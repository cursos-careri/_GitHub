//*****************************************************************************
// Realizar un ejercicio en donde se extienden los movimientos del brazo 
// articulado
//
// 1.- Implementar un esquema en donde el brazo se extienda a toda el área
//     de la ventana.
// 2.- Agregue un grado más de libertad al brazo en el plano X-Y.
// 3.- Modifique el grado de abatimiento de alguna de las uniones.
//
//=============================================================================



//---[ VARIABLES GLOBALES ]---
float angle = 0.0;					// Ángulo en una ariculación
float angleDirection = 1;		// Dirección del ángulo
float speed = 0.005;				// Velocidad del cambio

//-----[ AJUSTES ]-----
void setup() {
  size(600, 400);						// Tamaño de la ventana
}

//-----[ CICLO PRINCIPAL ]-----
void draw() {
  background(204);					// Repinta el fondo en cada ciclo
  translate(20, 25); 				// Punto de inicio de coordenadas, desplazado
  rotate(angle);						// Rotación que adquirirá lo que se dibuje (1)
  strokeWeight(12);					// Dimensiones del lápiz
  line(0, 0, 40, 0);				// Dibujo...
  translate(40, 0);  				// Movimiento a la próxima unión
  rotate(angle * 2.0);			// Nueva rotación (2)
  strokeWeight(6);					// Lápiz más grueso
  line(0, 0, 30, 0);				// Trazado
  translate(30, 0);  				// Movimiento a la próxima unión 
  rotate(angle * 2.5);			// Siguiente ángulo de rotación (3)
  strokeWeight(3);					// Lápiz de otro grosor
  line(0, 0, 20, 0);				// Trazado 
  
	angle += speed * angleDirection;	// Modificación de la variable 'ángulo'
																		// para las siguientes impresiones
  // Identificación del ángulo máximo a trazar. Si se llegó al tope se 
	// continúa en la dirección contraria.
  if ((angle > QUARTER_PI) || (angle < 0)) {
    angleDirection = -angleDirection;
  }
}
//*****************************************************************************

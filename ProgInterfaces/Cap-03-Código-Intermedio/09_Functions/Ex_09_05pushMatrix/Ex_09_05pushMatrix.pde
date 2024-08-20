size(400, 400);

fill(255);
rect(0, 0, 200, 200);  // Rectángulo Blanco

pushMatrix();          // Se GUARDA el 'Sistema de Coordenadas' actual

translate(120, 80);    // NUEVO Sistema de Coordenadas
fill(0);  
rect(0, 0, 200, 200);  // Rectángulo Negro

popMatrix();           // Se RESTAURA 'Sistema de Coordenadas' anterior

fill(100);  
rect(60, 40, 200, 200);  // Rectángulo Gris, en el 'Sistema de Coordenadas'
                         // previo.

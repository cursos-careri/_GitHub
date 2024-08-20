void setup() {
  println("Listo para Rodar");
  rollDice(20);
  rollDice(20);
  rollDice(6);
  println("Terminamos.");
}

void rollDice(int numSides) {
  int d = 1 + int(random(numSides));
  println("Rodando... " + d);
}

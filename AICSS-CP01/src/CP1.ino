#include <Arduino.h>

void setup() {
  Serial.begin(115200);
}

void loop() {
  Serial.println("--------------------------------------------");
  Serial.println("inicializando máquina 1, aguarde");
  delay(5000);

  String m1 = "Máquina 1";
  Serial.println(String(m1) + ", SUCESSO");
  delay(3000);
  Serial.println(String(m1) + ", SUCESSO");
  delay(3000);
  Serial.println(String(m1) + ", SUCESSO");
  delay(3000);
  Serial.println(String(m1) + ", SUCESSO");
  delay(3000);
  Serial.println(String(m1) + ", SUCESSO");
  delay(3000);
  Serial.println(String(m1) + ", FALHA, VERIFIQUE A MÁQUINA!");
  delay(9000);
  Serial.println("Finalizando máquina 1");
  delay(1000);

  Serial.println("--------------------------------------------");
  Serial.println("inicializando máquina 2, aguarde");
  delay(5000);
  
  String m2 = "Máquina 2";
  Serial.println(String(m2) + ", SUCESSO");
  delay(3000);
  Serial.println(String(m2) + ", SUCESSO");
  delay(3000);
  Serial.println(String(m2) + ", SUCESSO");
  delay(3000);
  Serial.println(String(m2) + ", SUCESSO");
  delay(3000);
  Serial.println(String(m2) + ", SUCESSO");
  delay(3000);
  Serial.println(String(m2) + ", FALHA, VERIFIQUE A MÁQUINA!");
  delay(4000);
  Serial.println("Finalizando máquina 2");
  delay(1000);

  Serial.println("reinicializando máquinas, aguarde!");
  delay(7000);
  Serial.println("--------------------------------------------");

  Serial.println("inicializando máquina 1, aguarde");
  delay(5000);
  String m3 = "Máquina 1";
  Serial.println(String(m3) + ", SUCESSO");
  delay(1000);
  Serial.println(String(m3) + ", FALHA, VERIFIQUE A MÁQUINA!");
  delay(5000);
  Serial.println(String(m3) + ", SUCESSO");
  delay(1000);
  Serial.println(String(m3) + ", FALHA, VERIFIQUE A MÁQUINA!");
  delay(4000);
  Serial.println(String(m3) + ", SUCESSO");
  delay(1000);
  Serial.println(String(m3) + ", FALHA, VERIFIQUE A MÁQUINA!");
  delay(9000);
  Serial.println("Finalizando máquina 1");
  delay(1000);

  Serial.println("--------------------------------------------");
  Serial.println("inicializando máquina 2, aguarde");
  delay(5000);
  String m4 = "Máquina 2";
  Serial.println(String(m4) + ", FALHA, VERIFIQUE A MÁQUINA!");
  delay(6000);
  Serial.println(String(m4) + ", FALHA, VERIFIQUE A MÁQUINA!");
  delay(5000);
  Serial.println(String(m4) + ", FALHA, VERIFIQUE A MÁQUINA!");
  delay(4000);
  Serial.println(String(m4) + ", FALHA, VERIFIQUE A MÁQUINA!");
  delay(3000);
  Serial.println(String(m4) + ", SUCESSO");
  delay(7000);
  Serial.println(String(m4) + ", FALHA, VERIFIQUE A MÁQUINA!");
  delay(4000);
  Serial.println("Finalizando máquina 2");
  delay(1000);

}
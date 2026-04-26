/* CP2: AICSS + Cyber */
#include <Arduino.h>
#include <DHT.h>
#include "mbedtls/sha256.h"

// CP AICSS: Controle do LED (como declarar o pino do LED?) (como controlar o acionamento do LED?)
#define LED_PIN 26
bool acendeLED = false;

// CP AICSS: Controle do BOTÃO (como controlar o pino do BOTÃO?)
#define BTN_PIN 13

// CP AICSS: Como controlar o DHT22?
// (pino, modelo, criação do objeto de software para controle do DHT)
#define DHTPIN 19
#define DHTMODEL DHT22
DHT dht(DHTPIN, DHTMODEL);

// De acordo com o visto em sala de aula, de quanto em quanto tempo deve ser
// realizada a coleta de medições do DHT 22? Use um intervalo de tempo
// adequado e que não seja menor que o mínimo conforme a especificação do sensor
const int intervalo_coleta = 3000;
uint32_t tempo_anterior = 0;

// CP AICSS: Use a variável senha_ativar para armazenar o hash da senha de ativação
// A senha é 1234
const char* senha_ativar = "03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4";
// CP AICSS: Use a variável senha_desativar para armazenar o hash da senha de desativação
// A senha é 4321
const char* senha_desativar = "fe2592b42a727e977f055947385b709cc82b16b9a87f88c6abf3900d65d0cdc3";

// CP AICSS: Duas variáveis de controle da Estufa: variável para identificação e para nome
// CP AICSS: Controle para verificar se está no modoAtivo para coleta das medições.
// Nossa variável deve iniciar desativada. Qual valor booleano deve-se atribuir à variável? 
String estufa = "estufa1";
float id = 1.0;
bool modoAtivo = false;

// CP AICSS: FORNECIDO PELO PROFESSOR
String bytesToHex(const uint8_t* hash, size_t len);
String sha256(String entrada);

// CP AICSS: FORNECIDO PELO PROFESSOR - Armazena o comando
String comando = "";

void setup() {
    // CP AICSS: Controle de inicialização do Monitor Serial
    Serial.begin(115200);
    // CP AICSS: Como se programa a inicialização do pino do LED?
    pinMode(LED_PIN, OUTPUT);
    // CP AICSS: Como se programa a inicialização do pino do BOTÃO?
    pinMode(BTN_PIN, INPUT_PULLUP);
    // CP AICSS: Como se programa a inicialização do sensor DHT22?
    dht.begin();
    Serial.println("Sistema Inicializado - CP2 - AICSS + Cyber");
}

void loop() {
    // CP AICSS: FORNECIDO PELO PROFESSOR - Controle para verificação se é o momento de digitar a senha
    bool digitarSenha = false;
    bool botaoPressionado = false;
    // CP AICSS: O que deve ser inserido no IF a seguir para verificar se o botão foi pressionado?
    if (digitalRead(BTN_PIN) == LOW) {
        botaoPressionado = true;
        Serial.println("");
        Serial.println("Botão pressionado!");
        digitarSenha = true;
    }

    // CP AICSS: O que deve ser inserido no IF a seguir, considerando que deseja-se verificar
    // se a variável digitarSenha é verdadeira?
    if (digitarSenha == true) {
        Serial.println("Digite a senha: ");

        // Espera o primeiro caractere chegar
        while (Serial.available() == 0) {
            delay(200);
        }

        Serial.setTimeout(1500);  // Define timeout para 1,5 segundo
        String pass = Serial.readStringUntil('\n');
        pass.trim();

        String hashDigitado = sha256(pass);
        Serial.println("");
        Serial.print("Hash da senha digitada: ");
        Serial.println("");
        Serial.println(hashDigitado);

        if (hashDigitado.equalsIgnoreCase(senha_ativar)) {
            modoAtivo = true;
            // CP AICSS: O usuário digitou a senha de ATIVAÇÃO, imprima um aviso no Monitor Serial sobre isso
            Serial.println("");
            Serial.println("A senha de ATIVAÇÃO foi inserida corretamente. Iniciando Processos!");
            Serial.println("");
            // CP AICSS: Como "imprimir" o cabeçalho do .csv?
            Serial.println("");
            Serial.println("O cabeçalho dos valores para .csv são impressos dessa forma: ");
            Serial.println("ID,Estufa,Temp,Umid,IC");
            // CP AICSS: Como acender o LED para indicar que digitou a senha correta?
            digitalWrite(LED_PIN, HIGH);
        } else if (hashDigitado.equalsIgnoreCase(senha_desativar)) {
            modoAtivo = false;
            // CP AICSS: O usuário digitou a senha de DESATIVAÇÃO, imprima um aviso no Monitor Serial sobre isso
            Serial.println("");
            Serial.println("A senha de DESATIVAÇÃO foi inserida corretamente. Desativando processo!");
            Serial.println("");
            // CP AICSS: Como desligar o LED para indicar que o sistema foi desativado?
            digitalWrite(LED_PIN, LOW);
        } else {
            // CP AICSS: Usuário digitou senha incorreta, manter estado atual
            // (apenas imprimir no Monitor Serial que a senha está incorreta)
            Serial.println("");
            Serial.println("A senha digitada está incorreta. A estufa continuará o precesso!");
            Serial.println("");
        }
        digitarSenha = false;
    }

    if (modoAtivo) {
        // O modo de coleta de medições está ativo.
        if (millis() - tempo_anterior >= intervalo_coleta) {
            tempo_anterior = millis();

            // Como declarar uma variável para armazenar a temperatura
            // e já coletar a medição de temperatura?
            float temp = dht.readTemperature();
            
            // Como declarar uma variável para armazenar a umidade
            // e já coletar a medição de umidade?
            float umid = dht.readHumidity();
            
            // O if a seguir tem por finalidade verificar se a medição de temperatura e umidade
            // está inválida. Se estiver inválida, imprimir um aviso no Monitor Serial
            // e retornar
            if (isnan (temp) || isnan(umid) ) {
                Serial.println("");
                Serial.println("Falha na leitura!");
                Serial.println("");
                return;
            }

            // Como declarar uma variável para armazenar o índice de calor
            // e já coletar a medição de índice de calor?
            float indiceCalor = dht.computeHeatIndex(temp, umid, false);
            
            // Como imprimir os valores coletados de id, nome da máquina, temperatura, umidade e índice de calor?
            Serial.println("");
            Serial.printf("ID: %.2f | Estufa: %s | Temperatura: %.2f | Umidade: %.2f | índice de calor: %.2f", id, estufa.c_str(), temp, umid, indiceCalor);
            Serial.println("");
            id++;
        }
    }
    delay(50);
}

/* FUNÇÕES FORNECIDAS PELO PROFESSOR PARA USO DE SHA-256 EM ESP32 */

// Função para converter bytes para string hexadecimal
String bytesToHex(const uint8_t* hash, size_t len) {
	String hex = "";
	const char hexChars[] = "0123456789abcdef";
	for (size_t i = 0; i < len; i++) {
	  hex += hexChars[(hash[i] >> 4) & 0x0F];
	  hex += hexChars[hash[i] & 0x0F];
	}
	return hex;
}

// Função para calcular SHA-256 de uma string
String sha256(String entrada) {
	uint8_t hash[32];  // SHA-256 = 256 bits = 32 bytes
	mbedtls_sha256_context ctx;

	mbedtls_sha256_init(&ctx);
	mbedtls_sha256_starts_ret(&ctx, 0); // 0 = SHA-256
	mbedtls_sha256_update_ret(&ctx, (const unsigned char*)entrada.c_str(), entrada.length());
	mbedtls_sha256_finish_ret(&ctx, hash);
	mbedtls_sha256_free(&ctx);

	return bytesToHex(hash, sizeof(hash));
}

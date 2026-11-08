#include "DHTesp.h"

const int DHT_PIN = 15;  // DHT22 data pin
const int LED_PIN = 4;   // LED control pin

DHTesp dhtSensor;

void setup() {
  Serial.begin(115200);
  Serial.println("ESP32 Temperature Monitor with LED Warning");

  // Initialize sensors and pins
  dhtSensor.setup(DHT_PIN, DHTesp::DHT22);
  pinMode(LED_PIN, OUTPUT);
}

void loop() {
  // Read temperature and humidity
  TempAndHumidity data = dhtSensor.getTempAndHumidity();

  // Print values to Serial Monitor
  Serial.print("Temperature: ");
  Serial.print(String(data.temperature, 1));
  Serial.print(" °C  |  Humidity: ");
  Serial.print(String(data.humidity, 1));
  Serial.println(" %");

  // Threshold logic: Turn LED ON if temperature is above 30°C
  if (data.temperature > 30.0) {
    digitalWrite(LED_PIN, HIGH);
    Serial.println(" High Temperature Warning! LED is ON.");
  } else {
    digitalWrite(LED_PIN, LOW);
  }

  // Wait 2 seconds before the next reading
  delay(2000);
}
#define BLYNK_PRINT Serial
#include <ESP8266WiFi.h>
#include <BlynkSimpleEsp8266.h>
// You should get Auth Token in the Blynk App.
// Go to the Project Settings (nut icon).
char auth[] = "56117a80f9b446e6bb5f160e89bc3fba";
// Your WiFi credentials.
// Set password to "" for open networks.
char ssid[] = "Hamara Wifi";
char pass[] = "bhikari sala";
void setup()
{
  // Debug console
  Serial.begin(9600);
  Blynk.begin(auth, ssid, pass);
}
void loop()
{
  Blynk.run();
}

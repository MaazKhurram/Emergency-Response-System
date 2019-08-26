/*
* Arduino Wireless Communication Tutorial
*     Example 1 - Transmitter Code
*                
* by Dejan Nedelkovski, www.HowToMechatronics.com
* 
* Library: TMRh20/RF24, https://github.com/tmrh20/RF24/
*/
#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>
RF24 radio(7, 8); // CE, CSN
const byte address[][6] = { "00001", "00002" };
int led_state=0;
  
void setup() {
  radio.begin();
  radio.setPALevel(RF24_PA_MIN);
  radio.stopListening();
  pinMode (31,INPUT);
  Serial.begin(9600);


  
  
  
}
void loop() {
  delay(5);
  radio.openWritingPipe(address[0]);
  const char text[] = "Hello World";
  radio.write(&text, sizeof(text));
  
  delay(5);
  radio.openWritingPipe(address[1]);
  led_state=digitalRead(31);
  radio.write(&led_state, sizeof(led_state));
  Serial.println(digitalRead(31));
  
  
}

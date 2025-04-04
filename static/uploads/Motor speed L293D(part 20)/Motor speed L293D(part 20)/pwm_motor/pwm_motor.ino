#include "ThingSpeak.h"
#include<ESP8266WiFi.h>

const int LM35=A0;
WiFiClient client;
char ssid[]="";
char pass[]="";
unsigned long channelno=;
int fno=1;
const char * api="";

void setup()
{
  Serial.begin(115200);
  WiFi.mode(WiFi_STA);
  ThingSpeak.begin(client)
}

void loop()
{
  if(WiFi.status()!=WL_CONNECTED)
  {
    while(WiFi.status()!=WL_CONNECTED)
    {
      WiFi.begin(ssid,pass);
      Serial.print(".");
      delay(5000);
    }


  }

  int adc;
  float temp;
  adc=analogRead(LM35);
  temp=adc*3;
  temp=temp/10;
  ThingSpeak.writeField(cn,fn,tmp,apikey)



}
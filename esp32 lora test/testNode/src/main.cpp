#include <LoRarxtx.h>
#include <LoRa.h>
#include <SPI.h>
#include <Arduino.h>

long lastSendTime = 0;        // last send time
int interval = 2000;        // interval between sends
void setup(){
    Serial.begin(115200);
    LoRa.setPins(SS, RST, DIO0);
    LoRa.setTxPower(18);
    SPI.begin(SCK, MISO, MOSI, SS);
    while(!LoRa.begin(923E6)){
        Serial.println("LoRa Initailization failed!");
        delay(500);
    }
    LoRa.onReceive(onReceive);
    LoRa.receive();
    LoRa.setSpreadingFactor(7);
    Serial.println("LoRa init succeeded.");
}

void loop(){
    if (millis() - lastSendTime > interval) {
        String message = "Test";   // send a message
        sendMessage(message);
        Serial.println("Sending " + message);
        lastSendTime = millis();            // timestamp the message
        interval = 3000;     // 2-3 seconds
        LoRa.receive();    // go back into receive mode
        if(!receiveData){
            static int count = 0;
            count++;
            Serial.print("Waiting for data Round: ");
            Serial.println(count);
        }else{
            Serial.println("Data received already.");
        }
    }
}
// TODO: Either switch from using json, or add validation to the document

#include <RobotLib.h>
#include <ArduinoJson.h>

Motor leftMotor;
Motor rightMotor;

void setup() {
    leftMotor.begin(4, 5, 6);
    rightMotor.begin(7, 8, 9);

    Serial.begin(115200);
}

void loop () {
    if(Serial.available() > 0) {
        DynamicJsonDocument doc(1024);
        deserializeJson(doc, Serial);

        if(doc == NULL) return;

        leftMotor.output(doc["left_motor"]);
        rightMotor.output(doc["right_motor"]);
    }
}
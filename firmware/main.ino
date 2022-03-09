#include <RobotLib.h>
#include <ArduinoJson.h>

Motor leftMotor;
Motor rightMotor;

// The last time a packet was received
int lastPacket = 0;
// Used when a timeout occurs and we write 0 to the motors
bool hasWritten = false;

int left = 0;
int right = 0;

void setup()
{
    leftMotor.begin(4, 5, 6);
    rightMotor.begin(7, 8, 9);

    Serial.begin(115200);
}

void loop()
{
    leftMotor.output(left);
    rightMotor.output(right);

    if(millis() - 1000 > lastPacket) {
        left = 0;
        right = 0;
    }

    if (Serial.available() > 0)
    {
        DynamicJsonDocument doc(1024);
        deserializeJson(doc, Serial);

        if (doc == NULL) {
            return;
        }

        lastPacket = millis();
        hasWritten = false;

        left = doc["left_motor"].as<float>();
        right = doc["right_motor"].as<float>();
        if(left < 0.01 && left > -0.01) {
            left = 0;
        }
        if(right < 0.01 && right > -0.01) {
            right = 0;
        }
    }
}
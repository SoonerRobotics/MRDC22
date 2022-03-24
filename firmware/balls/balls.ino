#include <RobotLib.h>
#include <ardubson.h>

BSONStreamParser streamParser;

void messageHandler(BSONObject* bson_obj);

float intake = 0;
float elevator = 0;
float launcher = 0;

void setup()
{
  Serial.begin(115200);

  pinMode(3, OUTPUT);
  pinMode(6, OUTPUT);

  analogWrite(3, 0);
  analogWrite(6, 0);

  streamParser.setMessageHandler(messageHandler);
}

void messageHandler(BSONObject * bson_obj) {
  uint16_t cmd = bson_obj->getField("cmd").getInt();

  if (cmd == 0x02) {
    elevator = bson_obj->getField("elevator_motor").getDouble();
    intake = bson_obj->getField("intake_motor").getDouble();
    launcher = bson_obj->getField("launcher_motor").getDouble();
  }
}

void loop()
{
  processSerialInput();

  analogWrite(3, intake * 255);
  analogWrite(6, elevator * 255);
}

void processSerialInput() {
  while (Serial.available()) {
    char c = Serial.read();
    streamParser.analizeIncomingChars(c);
  }
  streamParser.update();
}

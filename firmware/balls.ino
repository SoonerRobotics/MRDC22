#include <RobotLib.h>
#include <ardubson.h>

Motor leftMotor;
Motor rightMotor;

BSONStreamParser streamParser;

void messageHandler(BSONObject* bson_obj);

int intake = 0;
int elevator = 0;
int launcher = 0;

void setup()
{
  Serial.begin(115200);

  streamParser.setMessageHandler(messageHandler);
}

void messageHandler(BSONObject * bson_obj) {
  uint16_t cmd = bson_obj->getField("cmd").getInt();

  if (cmd == 0x02) {
    elevator = bson_obj->getField("elevator_motor").getInt();
    intake = bson_obj->getField("intake_motor").getInt();
    launcher = bson_obj->getField("launcher_motor").getInt();
  }
}

void loop()
{
  processSerialInput();

  // WRITE MOTOR VALUES HERE
  // use the three variables written above
}

void processSerialInput() {
  while (Serial.available()) {
    char c = Serial.read();
    streamParser.analizeIncomingChars(c);
  }
  streamParser.update();
}
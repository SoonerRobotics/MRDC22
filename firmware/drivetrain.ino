#include <RobotLib.h>
#include <ardubson.h>

Motor leftMotor;
Motor rightMotor;

BSONStreamParser streamParser;

void messageHandler(BSONObject *bson_obj);

int left = 0;
int right = 0;

void setup()
{
  leftMotor.begin(4, 5, 6);
  rightMotor.begin(7, 8, 9);

  Serial.begin(115200);

  streamParser.setMessageHandler(messageHandler);
}

void messageHandler(BSONObject *bson_obj)
{
  uint16_t cmd = bson_obj->getField("cmd").getInt();

  if (cmd == 0x01)
  {
    left = bson_obj->getField("left_motor").getInt();
    right = bson_obj->getField("right_motor").getInt();
  }
}

void loop()
{
  processSerialInput();

  // NOTE: These two if statements are not tested, but they should work
  if (left < 0.1 && left > -0.1)
  {
    left = 0;
  }

  if (right < 0.1 && right > -0.1)
  {
    right = 0;
  }

  leftMotor.output(left);
  rightMotor.output(right);
}

void processSerialInput()
{
  while (Serial.available())
  {
    char c = Serial.read();
    streamParser.analizeIncomingChars(c);
  }
  streamParser.update();
}
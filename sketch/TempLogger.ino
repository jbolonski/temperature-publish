int tempPin = 0;
int byteRead=0;

void setup()
{
  analogReference(INTERNAL);
  Serial.begin(9600);
  while(!Serial){}
  RetrieveTemp(tempPin);
}

void loop()
{
  byteRead=Serial.read();

  if(byteRead==72){
    Serial.println( "{\"Status\":\"ONLINE\"}" );
  }

  if(byteRead==84){
    float tempC = RetrieveTemp(tempPin);
    Serial.println( "{\"Temperature\":"+String(tempC,2)+"}" );
  }

  byteRead=0;
}

float RetrieveTemp(int pin){
  float tempC;
  int reading;
  
  reading = analogRead(pin);
  tempC = reading / 9.31;
  return tempC;
}



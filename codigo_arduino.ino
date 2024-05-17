
int pino_led_g = 7;
int pino_led = 5;
//Pino ligado ao sensor de nivel de liquido
int pinosensor = 3;

void setup()
{
  Serial.begin(9600);
  pinMode(pinosensor, INPUT);
  pinMode(pino_led, OUTPUT);
  pinMode(pino_led_g, OUTPUT);
  
}

void loop()
{
  //int estado = digitalRead(pinosensor);
  /*Serial.print("Estado sensor : ");*/
  //Serial.println(estado);
  char command = Serial.read();
  
 /* switch(estado)
  {
    case 0:
      Serial.println("Abaixo do Limite.");
      digitalWrite(pino_led,LOW);
      break;
    case 1:
      Serial.println("LIMITE ALCANÇADO !!");
      digitalWrite(pino_led, HIGH);
      break;
  }*/
  
  if (Serial.available() > 1) {
    char command = Serial.read();
  
    if (command == '7') {
      digitalWrite(pino_led_g, HIGH);
    }
    else {
      digitalWrite(pino_led_g, LOW);
    }
    delay(500)
  }
  delay(5000);
}

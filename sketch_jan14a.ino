#define echoPin 6 
#define trigPin 7

int motor1pin1 = 2;
int motor1pin2 = 3;
int motor2pin1 = 4;
int motor2pin2 = 5;

void setup() {
  pinMode(motor1pin1, OUTPUT);
  pinMode(motor1pin2, OUTPUT);
  pinMode(motor2pin1, OUTPUT);
  pinMode(motor2pin2, OUTPUT);

  pinMode(9, OUTPUT); 
  pinMode(10, OUTPUT);

  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  Serial.begin(9600);
}

void loop() {
  int dist = measureDistance();
  // Measure distance using ultrasonic sensor

  Serial.print("Distance: ");
  Serial.print(dist);
  Serial.println(" cm");

  // Adjust motor speed and direction based on distance
  if (dist < 20) { // Adjust the distance threshold as needed
    // Object detected, stop and turn
    stopMotors();
  } else {
    // Logo tespiti sonuçlarına göre motorları kontrol et
    if (Serial.available() > 0) {
      int command = Serial.parseInt();

      // Gelen komutlara göre motorları kontrol et
      if (command == 1) {
        // 1 geldiğinde sağa dön
        turnRight();
      } else if (command == -1) {
        // -1 geldiğinde sola dön
        turnLeft();
      } else if (command == 0) {
        // 0 geldiğinde düz git
        moveForward();
      } else if (command == 404) {
        // 404 geldiğinde motorları durdur
        stopMotors();
      }
    }
  }
}

int measureDistance() {
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  int duration = pulseIn(echoPin, HIGH);
  int distance = (duration * 0.034) / 2;
  return distance;
}

void moveForward() {
  analogWrite(9, 200); // ENA pin
  analogWrite(10, 200); // ENB pin

  digitalWrite(motor1pin1, HIGH);
  digitalWrite(motor1pin2, LOW);

  digitalWrite(motor2pin1, HIGH);
  digitalWrite(motor2pin2, LOW);
}

void stopMotors() {
  digitalWrite(motor1pin1, LOW);
  digitalWrite(motor1pin2, LOW);

  digitalWrite(motor2pin1, LOW);
  digitalWrite(motor2pin2, LOW);
}

void turnRight() {
  digitalWrite(motor1pin1, HIGH);
  digitalWrite(motor1pin2, LOW);

  digitalWrite(motor2pin1, LOW);
  digitalWrite(motor2pin2, HIGH);
  delay(1000); // Adjust the turn duration as needed
  stopMotors();
}

void turnLeft() {
  digitalWrite(motor1pin1, LOW);
  digitalWrite(motor1pin2, HIGH);

  digitalWrite(motor2pin1, HIGH);
  digitalWrite(motor2pin2, LOW);
  delay(1000); // Adjust the turn duration as needed
  stopMotors();
}
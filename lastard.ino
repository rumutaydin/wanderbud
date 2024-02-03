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
  int dist = measureDistance(); // calculate the distance with an obstacle through ultrasonic sensor

  Serial.print("Distance: ");
  Serial.print(dist);
  Serial.println(" cm");

  if (dist >= 20) { // If greater than 20, the obstacle not in the way (can be changed), look for the result that comes from YOLO, move or stop accordingly

    if (Serial.available() > 0) {
      int command = Serial.parseInt();

      if (command == 1) {
        turnRight();
      } else if (command == -1) {
        turnLeft();
      } else if (command == 0) {
        moveForward();
      } else if (command == 404) {
        stopMotors();
      }
    }
  } else {

    stopMotors();
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
  analogWrite(9, 100); 
  analogWrite(10, 100); 

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

  analogWrite(9, 50); 
  analogWrite(10, 100); 
  digitalWrite(motor1pin1, HIGH);
  digitalWrite(motor1pin2, LOW);

  digitalWrite(motor2pin1, LOW);
  digitalWrite(motor2pin2, HIGH);

}

void turnLeft() {
  analogWrite(9, 100); 
  analogWrite(10, 50); 

  digitalWrite(motor1pin1, LOW);
  digitalWrite(motor1pin2, HIGH);

  digitalWrite(motor2pin1, HIGH);
  digitalWrite(motor2pin2, LOW);

}
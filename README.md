# Wanderbud: AI-Powered Suitcase with Object Detection

## Overview

Wanderbud is an innovative project that brings together the power of artificial intelligence and robotics to create a suitcase that autonomously follows its owner. The project utilizes a Raspberry Pi 4, Arduino Uno, an ultrasonic sensor, a motor driver, and two DC motors. The key feature of Wanderbud is its ability to track its owner using object detection with YOLOv5, a deep learning model.

## Hardware Components

- Raspberry Pi 4
- Arduino Uno
- Ultrasonic Sensor
- Motor Driver
- 2 DC Motors

## Object Detection Model

We designed various logos for our brand, Wanderbud, and created a custom dataset, manually labeling the images. The dataset, along with our colored logos, is provided in the project. We trained the YOLOv5 model with our dataset using Ultralytics instructions and Google Colab. Due to the absence of ML inference accelerators in the hardware, we opted for TensorFlow Lite inference and quantization to int8 and fp16 models to optimize performance.

## Software Components

### 1. `detect.py`

This Python script is derived from the YOLOv5 model's `detect.py`. We made slight modifications to integrate it with our project. If someone wishes to rebuild this project, they need to replace the original YOLOv5 `detect.py` file with our customized version during the inference process.

### 2. `lastard.ino`

The Arduino code responsible for controlling the wheels based on the object detection results. It contains the logic for turning left, turning right, going straight, and stopping the motors. The Arduino runs in a loop to check readings from the ultrasonic sensor and the serial connection.

### 3. `serial_code.py`

This Python script manages the communication with the Arduino by sending relevant information based on the object detection inference. It is invoked within the `detect.py` file and plays a crucial role in the coordination between the Raspberry Pi and the Arduino.

## Workflow

1. Capture real-time footage from the robot's camera.
2. Process each frame and perform object detection to identify if the Wanderbud logo is detected.
3. Send detection information and bounding box coordinates to the Arduino if the logo is detected; otherwise, send a "not detected" signal.
4. Arduino continuously checks ultrasonic sensor readings for obstacles in front of the robot.
5. Arduino also monitors the serial connection, receiving commands such as turn left, turn right, go straight, or stop motors based on distance measurements and bounding box coordinates.

## How to Build and Run

1. Clone the repository from GitHub.
2. Replace the original YOLOv5 `detect.py` file with our customized version.
3. Upload the `lastard.ino` code to the Arduino Uno.
4. Run the `detect.py` script, which will invoke the `serial_code.py` for communication with the Arduino.

Now, Wanderbud should be ready to autonomously follow its owner, avoiding obstacles along the way.

Feel free to explore and contribute to the project!

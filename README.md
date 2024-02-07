# Wanderbud: AI-Powered Suitcase that Follows its Owner

## Overview

Wanderbud is an innovative project that brings together the power of artificial intelligence and robotics to create a suitcase that autonomously follows its owner. The key feature of Wanderbud is its ability to track its owner using object detection with YOLOv5, a deep learning model. 

Wanderbud is currently in the proof of concept phase. The project is actively progressing as we refine the logic of the robot's movement. At this stage, we acknowledge that the current approach, relying on object detection with a Wanderbud logo, is impractical as it requires users to affix the logo to themselves. We began with object detection as a starting point, aiming to limit test the concept and initiate development. However, we are now focused on updating this logic to provide a more seamless experience. Our goal is to develop a solution that doesn't necessitate the use of a specific marker and instead focuses on efficient and intuitive tracking mechanisms. Stay tuned for updates as we continue to enhance Wanderbud's functionality.

## Object Detection Model

We designed various logos for our brand, Wanderbud, and created a custom dataset, manually labeling the images. The dataset, along with our colored logos, is provided in the project. We trained the YOLOv5 model (yolov5s.pt checkpoint) with our dataset using Ultralytics instructions and Google Colab. Due to the absence of ML inference accelerators in the hardware, we opted for TensorFlow Lite inference and quantization to int8 and fp16 models to optimize performance.

## Hardware Components

- Raspberry Pi 4 model B+
- Arduino Uno
- Ultrasonic Sensor
- Motor Driver
- 2 DC Motors
- 4 1.5V battery(for arduino)
- 5V=2.4A Powerbank(for raspi)
- Serial cable
- Male&female jumper wires


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


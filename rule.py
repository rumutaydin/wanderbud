'''A try of using rule-based detection -instead of YOLO- that could benefit edge computing such as our project. 
However, we didn't find a way to fully employ this approach as the confidence scores were low, even though 
the usage of resource were low'''

import cv2
import numpy as np

def detect_narrow_square_logo(frame):

    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_color = np.array([90, 100, 100])
    upper_color = np.array([100, 255, 255])

    mask = cv2.inRange(hsv_frame, lower_color, upper_color)
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    filtered_contours = [cnt for cnt in contours if cv2.contourArea(cnt) > 100]


    for contour in filtered_contours:

        epsilon = 0.02 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)

        x, y, w, h = cv2.boundingRect(approx)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    return frame

cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()
    result_frame = detect_narrow_square_logo(frame)
    cv2.imshow('Narrow Square Logo Detection', result_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
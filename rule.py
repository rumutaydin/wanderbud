import cv2
import numpy as np

def detect_narrow_square_logo(frame):
    # Görüntüyü BGR renk uzayından HSV'ye dönüştürme
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Algılanacak dar renk aralığını belirleme (HSV)
    lower_color = np.array([90, 100, 100])
    upper_color = np.array([100, 255, 255])

    # Renk filtresi oluşturma
    mask = cv2.inRange(hsv_frame, lower_color, upper_color)

    # Algılanan nesneleri tespit etme
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Algılanan konturları filtreleme
    filtered_contours = [cnt for cnt in contours if cv2.contourArea(cnt) > 100]

    # Algılanan nesnelerin etrafına dikdörtgen çizme
    for contour in filtered_contours:
        # Dikdörtgen çevresini daha sıkı ve doğru hale getirme
        epsilon = 0.02 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)

        x, y, w, h = cv2.boundingRect(approx)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    return frame

# Kamera bağlantısını başlatma
cap = cv2.VideoCapture(0)

while True:
    # Kameradan bir kare al
    ret, frame = cap.read()

    # Kare şeklinde logoyu algıla
    result_frame = detect_narrow_square_logo(frame)

    # Algılama sonucunu ekranda göster
    cv2.imshow('Narrow Square Logo Detection', result_frame)

    # Çıkış için 'q' tuşuna basın
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kamera bağlantısını kapatma
cap.release()
cv2.destroyAllWindows()
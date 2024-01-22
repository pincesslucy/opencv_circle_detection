import cv2
import numpy as np

red, green, blue = (0, 0, 255), (0, 255, 0), (255, 0, 0)

white, black = (255, 255, 255), (0, 0, 0)
image = np.full((480, 640, 3), white, np.uint8) 

def detect_color(image, x, y):
    (b, g, r) = image[y, x]
    return (b, g, r)

def draw_circle(image, circles):
    for i in circles[0,:]:
        color = detect_color(image, i[0], i[1])
        cv2.rectangle(image,(i[0] - i[2], i[1] + i[2]),(i[0] + i[2], i[1] - i[2]), (0,255,0),2)
        cv2.putText(image, str(color), (i[0] - i[2], i[1] - i[2]), cv2.FONT_HERSHEY_SIMPLEX, 0.5, black, 2)

capture = cv2.VideoCapture(0)
while True:
    ret, frame = capture.read()
    if not ret: break
    if cv2.waitKey(30) >= 0: break
    image = frame
    image = cv2.GaussianBlur(image, (9, 9), 0)
    gimage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    try:
        circles = cv2.HoughCircles(gimage, cv2.HOUGH_GRADIENT, 1, 50 ,param1=60 ,param2=50,minRadius=0, maxRadius=0)
        circles = np.uint16(np.around(circles))

        draw_circle(image, circles)
        cv2.imshow("Exercise 2", image)
    except:
        continue

capture.release()
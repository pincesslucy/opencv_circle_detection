import cv2
import numpy as np

red, green, blue = (0, 0, 255), (0, 255, 0), (255, 0, 0)

white, black = (255, 255, 255), (0, 0, 0)
image = np.full((480, 640, 3), white, np.uint8) 

def detect_color(image, x, y):
    (b, g, r) = image[y, x]
    return (b, g, r)

size = 0
prior = 0
for i in range(7):
    size = np.random.randint(10, 70)
    pt = (np.random.randint(0, 500) + size + prior, np.random.randint(0, 340) + size + prior)
    color = (red if size % 2 == 0 else green if size % 3 == 0 else blue)
    cv2.circle(image, pt, size, color, -1)
    prior = size * 2 + 2

image = cv2.GaussianBlur(image, (9, 9), 0)
gimage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

circles = cv2.HoughCircles(gimage, cv2.HOUGH_GRADIENT, 1, 30 ,param1=50,param2=25,minRadius=0, maxRadius=0)
circles = np.uint16(np.around(circles))

for i in circles[0,:]:
    color = ('red' if detect_color(image, i[0], i[1]) == red else 'green' if detect_color(image, i[0], i[1]) == green else 'blue')
    cv2.rectangle(image,(i[0] - i[2], i[1] + i[2]),(i[0] + i[2], i[1] - i[2]), (0,255,0),2)
    cv2.putText(image, color, (i[0] - i[2], i[1] - i[2]), cv2.FONT_HERSHEY_SIMPLEX, 0.5, black, 2)

title = "Draw circles"
cv2.imshow(title, image)
cv2.waitKey(0)
cv2.destroyAllWindows()


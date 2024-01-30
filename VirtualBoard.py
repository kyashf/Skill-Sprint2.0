import cv2
import numpy as np

drawing = False  # True if mouse is pressed

def draw_circle(event, x, y, flags, param):
    global drawing

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        cv2.circle(img, (x, y), 5, (0, 0, 255), -1)

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            cv2.circle(img, (x, y), 5, (0, 0, 255), -1)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False

img = np.ones((800, 1200, 3), np.uint8) * 255

cv2.namedWindow('Virtual White Board')
cv2.setMouseCallback('Virtual White Board', draw_circle)

while True:
    cv2.putText(img, 'Virtual White Board made by Yash Kumar', (300, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2, cv2.LINE_AA)

    cv2.imshow('Virtual White Board', img)
    k = cv2.waitKey(1) & 0xFF

    # Press 'c' (Clear) the drawing
    if k == ord('c'):
        img = np.ones((800, 1200, 3), np.uint8) * 255

    # Press 'q' (Exit) program
    elif k == ord('q'):
        break

cv2.destroyAllWindows()
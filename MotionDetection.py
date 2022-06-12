import cv2
from cv2 import cvtColor
import numpy as np
import time
import os
status = False

cap = cv2.VideoCapture(0)
cam = cv2.VideoCapture(0)
ret, Frame1 = cap.read()
ret, Frame2 = cap.read()
try:

    # creating a folder named data
    if not os.path.exists('data'):
        os.makedirs('data')

    # if not created then raise error
except OSError:
    print('Error: Creating directory of data')
currentframe = 0
while cap.isOpened():
    diff = cv2.absdiff(Frame1, Frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    retur, Thres = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilute = cv2.dilate(Thres, None, iterations=3)
    contoures, hire = cv2.findContours(
        dilute, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    #cv2.drawContours(Frame1, contoures, -1, (0, 255, 0,), 2)
    for contour in contoures:
        (x, y, w, h) = cv2.boundingRect(contour)
        if cv2.contourArea(contour) > 5000:
            cv2.rectangle(Frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)
            status = True
            # time.sleep(1)
            name = './data/frame' + str(currentframe) + '.jpg'
            print('Creating...' + name)

            cv2.imwrite(name, Frame1)
            currentframe += 1

        else:
            continue
                            
    status = False   
    cv2.imshow("feed", Frame1)
    Frame1 = Frame2   
    ret, Frame2 = cap.read()

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    

cv2.destroyAllWindows
cap.release()
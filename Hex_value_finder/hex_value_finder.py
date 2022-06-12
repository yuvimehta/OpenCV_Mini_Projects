from asyncio import events

from sys import builtin_module_names
from cv2 import EVENT_LBUTTONDOWN, EVENT_RBUTTONDOWN, FONT_HERSHEY_COMPLEX
import numpy as np
import cv2
import time
#event = [i for i in dir(cv2) if "EVENT" in i]
# print(event)


def rgb_to_hex(rgb):
    return '%02x%02x%02x' % rgb


def click_event(event, x, y, flags, param):

    if event == cv2.EVENT_LBUTTONDOWN:
        blue = img[y, x, 0]
        red = img[y, x, 1]
        green = img[y, x, 2]
        strxy1 = rgb_to_hex((red, green, blue))
        strxyz = str(red) + ',' + str(green) + ',' + str(blue)
        cv2.putText(img, strxy1, (x, y), FONT_HERSHEY_COMPLEX,
                    0.5, (255, 0, 0), 1)

        cv2.imshow('image', img)


path = input("file path:- ")
img = cv2.imread(path)
cv2.imshow("image", img)
cv2.setMouseCallback('image', click_event)


cv2.waitKey(0)
cv2.destroyAllWindows
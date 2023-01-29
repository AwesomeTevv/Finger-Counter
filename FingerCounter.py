import cv2
import time
import os

cam_width = 1280
cam_height = 720

cap = cv2.VideoCapture(0)

cap.set(3, cam_width)
cap.set(4, cam_height)

while True:
    success, img = cap.read()
    
    cv2.imshow("Finger Counter", img)
    cv2.waitKey(1)


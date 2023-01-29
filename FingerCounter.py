import cv2
import time
import os

cam_width = 1280
cam_height = 720

cap = cv2.VideoCapture(0)

cap.set(3, cam_width)
cap.set(4, cam_height)

prev_time = 0
curr_time = 0

while True:
    success, img = cap.read()
    
    curr_time = time.time()
    fps = 1 / (curr_time - prev_time)
    prev_time = curr_time
    
    cv2.putText(img, f'fps: {int(fps)}', (20, 40), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 2)
    
    cv2.imshow("Finger Counter", img)
    cv2.waitKey(1)


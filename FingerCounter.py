import cv2
import time
import os

cam_width = 1280
cam_height = 720

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, cam_width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, cam_height)

prev_time = 0
curr_time = 0

folderPath = "HandImages"
myList = os.listdir(folderPath)

overlayList = []
for imgPath in myList:
    image = cv2.imread(f'{folderPath}/{imgPath}')
    overlayList.append(image)

while True:
    success, img = cap.read()
    
    height, width, center = overlayList[0].shape
    img[0 : height, 0 : width] = overlayList[0]
    
    curr_time = time.time()
    fps = 1 / (curr_time - prev_time)
    prev_time = curr_time
    
    cv2.putText(img, f'fps: {int(fps)}', (20, 40), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 2)
    
    cv2.imshow("Finger Counter", img)
    cv2.waitKey(1)


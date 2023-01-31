import cv2
import time
import os
import HandTrackingModule as htm

# * Constants
landmark_x = 1
landmark_y = 2

cam_width = 1280
cam_height = 720

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, cam_width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, cam_height)

prev_time = 0
curr_time = 0

folderPath = "HandImages"
myList = os.listdir(folderPath)

detector = htm.handDetector(detectionConfidence = 0.75)

overlayList = []
for imgPath in myList:
    image = cv2.imread(f'{folderPath}/{imgPath}')
    overlayList.append(image)

fingertip_ids = [8, 12, 16, 20]

while True:
    success, img = cap.read()
    
    img = detector.findHands(img)
    
    landmark_list = detector.findPosition(img, draw = False)
    
    if len(landmark_list) != 0:
        fingers = []
        
        #! Checking if the thumb is out
        if landmark_list[4][landmark_x] > landmark_list[3][landmark_x]:
            fingers.append(1)
        else:
            fingers.append(0)
        
        #! Checking if the other fingers are out
        for tip in fingertip_ids:
            if landmark_list[tip][landmark_y] < landmark_list[tip - 2][landmark_y]:
                fingers.append(1)
            else:
                fingers.append(0)
        
        # print(fingers)
        total_fingers = fingers.count(1)
        print(total_fingers)
    
    height, width, center = overlayList[0].shape
    img[100 : height + 100, 0 : width] = overlayList[0]
    
    curr_time = time.time()
    fps = 1 / (curr_time - prev_time)
    prev_time = curr_time
    
    cv2.putText(img, f'fps: {int(fps)}', (20, 40), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 2)
    
    cv2.imshow("Finger Counter", img)
    cv2.waitKey(1)


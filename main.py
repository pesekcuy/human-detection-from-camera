from time import sleep
import cv2
import numpy as np

cv2.startWindowThread()
capture = cv2.VideoCapture(0)

hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

whileLoopIterator = True

while(whileLoopIterator):
    # reading the frame
    ret,frame = capture.read()
    frame = cv2.resize(frame, (960, 540))
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    humans,_ =hog.detectMultiScale(frame, winStride=(12, 12), padding=(24, 24), scale=1.05)
    
    print("Human detected:", len(humans))
    humans = np.array([[x, y, x + w, y + h] for (x, y, w, h) in humans])
    for (xA, yA, xB, yB) in humans:
        # display the detected boxes in the colour picture
        cv2.rectangle(frame, (xA, yA), (xB, yB), (255, 255, 255), 2)
    # displaying the frame
    cv2.imshow('frame',frame)
    sleep(5)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        # breaking the loop if the user types q
        # note that the video window must be highlighted!
        whileLoopIterator = False

capture.release()
cv2.destroyAllWindows()

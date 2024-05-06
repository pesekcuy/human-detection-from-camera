# Import the needed modules
from time import sleep
import cv2
import numpy as np

# Start video capture from the camera with OpenCV
cv2.startWindowThread()
capture = cv2.VideoCapture(0)

# Set the SVM people detector
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

# Start the while loop to detect human from camera feeds
# It will run in infinite loop unless the user does the specified action in the if block
whileLoopIterator = True
while(whileLoopIterator):
    ret,frame = capture.read() # reading the capture
    frame = cv2.resize(frame, (1024, 768)) # resizing the capture
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # turning the capture into grayscale

    # detection start
    humans,_ =hog.detectMultiScale(frame, winStride=(12, 12), padding=(24, 24), scale=1.05) 
    print("Human detected:", len(humans)) # print amount of human detected
    
    # creating white block to detect human in the feed
    humans = np.array([[x, y, x + w, y + h] for (x, y, w, h) in humans])
    for (xA, yA, xB, yB) in humans:
        # display the detected boxes in the colour picture
        cv2.rectangle(frame, (xA, yA), (xB, yB), (255, 255, 255), 2)
    
    cv2.imshow('frame',frame) # displaying the frame
    sleep(2) # bring the camera to sleep for 2 seconds for each loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        # breaking the loop if the user types q
        # note that the video window must be highlighted!
        whileLoopIterator = False

capture.release()
cv2.destroyAllWindows()

import os
import cv2


def checkforface(image):
    cascPath = "haarcascade_frontalface_default.xml"       # Get user supplied values
    faceCascade = cv2.CascadeClassifier(cascPath)         # Create the haar cascade


    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Detect faces in the image
    faces = faceCascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5, minSize=(30, 30), flags = cv2.CASCADE_SCALE_IMAGE)
    if(len(faces)>0):
        return True
    else:
        return False

#img=r"C:/Users/Aayush/Desktop/Test/rainbow-finger.jpg"
#img=cv2.imread(img)
#print(checkforface(img))

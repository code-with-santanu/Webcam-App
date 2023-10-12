import cv2
import time


# 0 is the index of available webcam in system
imgcapture = cv2.VideoCapture(0)
result = True

fileName = int(round(time.time() * 1000))
fileName = './images/{}.png'.format(fileName)
while (result):
    ret, frame = imgcapture.read()
    cv2.imwrite(fileName, frame)
    result = False
    print("Image Captured")

imgcapture.release()

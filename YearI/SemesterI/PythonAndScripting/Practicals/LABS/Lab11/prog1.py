import numpy as np
import cv2
import datetime

current_time = datetime.datetime.now()
print("LAB 11 SHUBHANG GUPTA "+str(current_time))
img = cv2.imread("lake.jpg")
pixel = img[100, 100]
print(pixel)
print(img.shape)
cv2.imshow("forensic",img)
for i in range(100,300):
    for j in range(100,300):
        img[i,j] = [0,0,0]
cv2.imshow("forensic",img)
cv2.waitKey(0)
cv2.destroyAllWindows()


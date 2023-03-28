import cv2
import numpy as np
import matplotlib.pyplot as plt
import datetime

current_time = datetime.datetime.now()
print("LAB 11 SHUBHANG GUPTA "+str(current_time))
image=cv2.imread('lake.jpg',1)
roi=image[100:400,200:400]
cv2.imshow("forensic", roi)
cv2.waitKey(0)
cv2.destroyAllWindows()


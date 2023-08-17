import cv2 
import datetime

current_time = datetime.datetime.now()
print("LAB 11 SHUBHANG GUPTA "+str(current_time))
image=cv2.imread('lake.jpg')
img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
threshold=160 
ret, thresh1=cv2.threshold(img, threshold,255,cv2.THRESH_BINARY)
ret, thresh2 = cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY_INV)
ret, thresh3= cv2.threshold(img, threshold, 255, cv2.THRESH_TRUNC)
ret, thresh4 = cv2.threshold (img, threshold, 255, cv2.THRESH_TOZERO)
ret, thresh5= cv2.threshold(img, threshold, 255, cv2.THRESH_TOZERO_INV)
cv2.imshow('Binary Threshold', thresh1) 
cv2.imshow('Binary Inverted', thresh2) 
cv2.imshow('Truncated Threshold', thresh3)
cv2.imshow("Zero Threshold", thresh4)
cv2.imshow('Zero Inverted', thresh5)
cv2.waitKey(0)
cv2.destroyAllWindows()


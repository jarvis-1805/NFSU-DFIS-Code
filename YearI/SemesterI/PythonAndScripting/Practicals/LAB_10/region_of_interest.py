import cv2

image = cv2.imread('lake.jpg')
roi = image[100 : 400, 400 : 800]

cv2.imshow("name", image)
cv2.imshow("region of interest", roi)
cv2.waitKey(0)


import cv2 as opencv

image = opencv.imread('lake.jpg')
output = image.copy()

rect = opencv.rectangle(output, (700, 300),(500, 200), (25, 255, 200), 6)

opencv.imshow("rectangle",rect)
opencv.waitKey(0)


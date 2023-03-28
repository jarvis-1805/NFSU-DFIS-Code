import cv2 as opencv

image = opencv.imread('lake.jpg')
output = image.copy()

text=input("enter your text: ")
text = opencv.putText(output, text, (300, 450),opencv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

opencv.imshow("text",text)
opencv.waitKey(0)


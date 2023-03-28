from datetime import datetime
import cv2


current_time = datetime.now()
print("LAB 10 Shubhang Gupta " + str(current_time))

path = r"foster-lake.jpg"
img_rgb = cv2.imread(path, 1)
cv2.imshow("DICE", img_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()


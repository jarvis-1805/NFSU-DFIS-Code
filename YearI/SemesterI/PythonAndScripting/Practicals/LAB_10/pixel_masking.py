import cv2

img = cv2.imread('lake.jpg')
pixel = img [100, 100]

print(pixel)
print(img.shape)

cv2.imshow("name", img)

for i in range(100, 300):
  for j in range(100, 300):
    img[i, j] = [0, 0, 0]

cv2.imshow("changed", img)
cv2.waitKey(0)
cv2.destroyAllWindows()


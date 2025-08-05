import numpy as np
import pandas as np
import cv2

img = cv2.imread("Kitchen.png", cv2.IMREAD_GRAYSCALE)
img2 = img.copy()
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        if img[i,j] < 155:
            img[i,j] = 0
        else:
            img[i,j] = 255
cv2.imshow("Kitchen", img)
cv2.waitKey(0)

for i in range(img2.shape[0]):
    for j in range(img2.shape[1]):
        img2[i,j] = -img2[i,j]
cv2.imshow("Kitchen", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

road = cv2.imread("Road.png", cv2.IMREAD_COLOR)
print(road.shape)
for i in range(road.shape[0]):
    for j in range(road.shape[1]):
       road[i, j] = road[i, j]
cv2.imshow("Road", road)
cv2.waitKey(0)
cv2.destroyAllWindows()

gray_road = cv2.cvtColor(road, cv2.COLOR_BGR2GRAY)
cv2.imwrite("Grey_road.png", gray_road)
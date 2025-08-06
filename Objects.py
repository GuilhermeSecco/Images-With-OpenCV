import numpy as np
import pandas as pd
import cv2

img = cv2.imread("Objects.png", cv2.IMREAD_GRAYSCALE)
print(img.shape)
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
            if img[i,j] < 110:
                img[i,j] = 0
            else:
                img[i,j] = 255

cv2.imshow("Black and White", img)
cv2.waitKey(0)
cv2.imwrite("BW_Objects.png", img)
cv2.destroyAllWindows()

img2 = img.copy()
for i in range(img2.shape[0] - 1):
    for j in range(img2.shape[1] - 1):
            a1 = img[i-1,j-1]
            a2 = img[i-1,j]
            a3 = img[i-1,j+1]
            a4 = img[i,j-1]
            a5 = img[i,j+1]
            a6 = img[i+1,j-1]
            a7 = img[i+1,j]
            a8 = img[i+1,j+1]
            sigma = (int(a1) + int(a2) + int(a3) + int(a4) + int(a5) + int(a6) + int(a7) + int(a8))
            if sigma > 0 and sigma < 2040:
                img2[i][j] = 0
            else:
                img2[i][j] = 255

cv2.imshow("Border", img2)
cv2.waitKey(0)
cv2.imwrite("BW_Objects_Border.png", img2)
cv2.destroyAllWindows()
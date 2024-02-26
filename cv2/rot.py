import cv2
import numpy as np

image = cv2.imread("cat.jpeg")

h, w = image.shape[:2]

M = cv2.getRotationMatrix2D((w / 2, h / 2), 90, 1) # center(회전할 중심), 각도(왼쪽으로 도는듯), 스케일(크기 말하는듯?)
dst = cv2.warpAffine(image, M, (w, h))

cv2.imshow("dst", dst)

cv2.waitKey(0)
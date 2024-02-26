import cv2

image = cv2.imread('cat.jpeg')
image[:, :, 2] = 0 #전체 픽셀에 대해서 인덱스 2(BGR중 R) 0으로 바꿈

cv2.imshow("color_change", image)
cv2.waitKey(0)
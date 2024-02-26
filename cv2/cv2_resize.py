import cv2
import numpy as np
image = cv2.imread('cat.jpeg')

# print(image.shape)

# image_big = cv2.resize(image, None, fx=1.0, fy=2.0, interpolation = cv2.INTER_CUBIC)
# cv2.imshow("big image", image_big)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# image_small = cv2.resize(image, None, fx=0.4, fy=0.4, interpolation = cv2.INTER_AREA)
# cv2.imshow('small image', image_small)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

h, w = image.shape[:2]

M = np.float32([[1,0, 100], [0, 1, -500]]) # 변환 행렬(x= 오른쪽, y=아래쪽)
dst = cv2.warpAffine(image, M, (w, h))

cv2.imshow("dst", dst)

cv2.waitKey(0) 
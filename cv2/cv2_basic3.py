import cv2

import time

image = cv2.imread('cat.jpeg')

# start_time = time.time()

# for i in range(0, 100):
#     for j in range(0, 100):
#         image[i, j] = [255, 255, 255]

# print(f"--- {time.time()-start_time} second ---")


start_time = time.time()

image[0:100, 0:100] = [150, 150, 150]

print(f"--- {time.time()-start_time} second ---")

cv2.imshow("img", image)

cv2.waitKey(0)

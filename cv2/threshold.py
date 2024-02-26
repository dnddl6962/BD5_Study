#threshold: 한계치
import cv2

#흑백 이미지 불러오기
image = cv2.imread('gray.png', cv2.IMREAD_GRAYSCALE)

# 담을 이미지 리스트 초기화
images = []

ret, thres1 = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
images.append(thres1)
ret, thres2 = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY_INY)
images.append(thres1)
ret, thres3 = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
images.append(thres1)
ret, thres4 = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
images.append(thres1)
ret, thres5 = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
images.append(thres1)




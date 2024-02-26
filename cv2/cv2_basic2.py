import cv2

image = cv2.imread('cat.jpeg')

print(image.shape) # h, w, c 높이 넓이 채널
print(image.size) 

px = image[300, 500] # 특정 픽셀 

print(f"B: {px[0]}, G: {px[1]}, R: {px[2]}")# bgr순서대로 출력

print(px[2]) # r값만 출력


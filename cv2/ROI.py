# import cv2
# import json
# import os
# import numpy as np
# from datetime import datetime

# dragged_areas = []  # 드래그한 영역을 저장할 리스트
# isDragging = False
# x0, y0, w, h = -1, -1, -1, -1
# blue, red = (255, 0, 0), (0, 0, 255)

# def save_to_json(info, img_name):
#     img_name_without_extension = os.path.splitext(img_name)[0]
#     current_time = datetime.now().strftime("%Y%m%d%H%M%S%f")[:-3]
#     json_filename = f'./json/{img_name_without_extension}_rec_{current_time}.json'

#     # NumPy uint8 값을 Python 기본 데이터 형식으로 변환
#     def convert(o):
#         if isinstance(o, np.uint8):
#             return int(o)
#         raise TypeError

#     json_data = {"result": True, "data": info}

#     with open(json_filename, 'w') as json_file:
#         json.dump(json_data, json_file, default=convert, indent=2)

# def save_cropped(img, img_name, drag_info):
#     img_name_without_extension = os.path.splitext(img_name)[0]
#     current_time = datetime.now().strftime("%Y%m%d%H%M%S%f")[:-3]
#     cropped_filename = f'./result/{img_name_without_extension}_crop_{current_time}.jpg'

#     roi = img[drag_info['y1']:drag_info['y2'], drag_info['x1']:drag_info['x2']]
#     cv2.imwrite(cropped_filename, roi)

# def onMouse(event, x, y, flags, param):
#     global isDragging, x0, y0, w, h, img

#     if event == cv2.EVENT_LBUTTONDOWN:
#         isDragging = True
#         x0, y0 = x, y

#     elif event == cv2.EVENT_MOUSEMOVE:
#         if isDragging:
#             img_draw = img.copy()
#             cv2.rectangle(img_draw, (x0, y0), (x, y), blue, 2)
#             cv2.imshow('img', img_draw)

#     elif event == cv2.EVENT_LBUTTONUP:
#         if isDragging:
#             isDragging = False
#             w, h = x - x0, y - y0

#             if w > 0 and h > 0:
#                 img_draw = img.copy()
#                 cv2.rectangle(img_draw, (x0, y0), (x, y), red, 2)
#                 cv2.imshow('img', img_draw)

#                 roi_info = {
#                     'id': len(dragged_areas) + 1,
#                     'red': img[y, x][2],
#                     'green': img[y, x][1],
#                     'blue': img[y, x][0],
#                     'x1': x0,
#                     'y1': y0,
#                     'x2': x,
#                     'y2': y
#                 }

#                 # 드래그한 영역 정보 추가
#                 dragged_areas.append(roi_info)

#                 save_cropped(img, 'dog.jpg', roi_info)

#             else:
#                 cv2.imshow('img', img)
#                 print('좌측 상단에서 우측 하단으로 영역을 드래그하세요.')

# img = cv2.imread('dog.jpg')
# cv2.imshow('img', img)
# cv2.setMouseCallback('img', onMouse)

# while True:
#     key = cv2.waitKey(1)
#     if key != -1:  # 아무 키나 누르면 종료
#         break

# # 작업이 끝난 뒤, 모든 드래그 영역을 JSON 파일로 저장
# save_to_json(dragged_areas, 'dog.jpg')

# cv2.destroyAllWindows()

import cv2
import json
import os
import numpy as np
from datetime import datetime

dragged_areas = []  # 드래그한 영역을 저장할 리스트
isDragging = False
x0, y0, w, h = -1, -1, -1, -1
blue, red = (255, 0, 0), (0, 0, 255)

def save_to_json(info, img_name):
    img_name_without_extension = os.path.splitext(img_name)[0]
    current_time = datetime.now().strftime("%Y%m%d%H%M%S%f")[:-3]
    json_filename = f'./json/{img_name_without_extension}_rec_{current_time}.json'

    # NumPy uint8 값을 Python 기본 데이터 형식으로 변환
    def convert(o):
        if isinstance(o, np.uint8):
            return int(o)
        raise TypeError

    # 드래그한 영역의 ID를 001, 002, 003과 같은 형식으로 변환
    formatted_info = [{'id': f"{i + 1:03d}", **roi_info} for i, roi_info in enumerate(info)]

    json_data = {"result": True, "data": formatted_info}

    with open(json_filename, 'w') as json_file:
        json.dump(json_data, json_file, default=convert, indent=2)

def save_cropped(img, img_name, drag_info):
    img_name_without_extension = os.path.splitext(img_name)[0]
    current_time = datetime.now().strftime("%Y%m%d%H%M%S%f")[:-3]
    cropped_filename = f'./result/{img_name_without_extension}_crop_{current_time}.jpg'

    roi = img[drag_info['y1']:drag_info['y2'], drag_info['x1']:drag_info['x2']]
    cv2.imwrite(cropped_filename, roi)

def onMouse(event, x, y, flags, param):
    global isDragging, x0, y0, w, h, img

    if event == cv2.EVENT_LBUTTONDOWN:
        isDragging = True
        x0, y0 = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if isDragging:
            img_draw = img.copy()
            cv2.rectangle(img_draw, (x0, y0), (x, y), blue, 2)
            cv2.imshow('img', img_draw)

    elif event == cv2.EVENT_LBUTTONUP:
        if isDragging:
            isDragging = False
            w, h = x - x0, y - y0

            if w > 0 and h > 0:
                img_draw = img.copy()
                cv2.rectangle(img_draw, (x0, y0), (x, y), red, 2)
                cv2.imshow('img', img_draw)

                roi_info = {
                    'red': img[y, x][2],
                    'green': img[y, x][1],
                    'blue': img[y, x][0],
                    'x1': x0,
                    'y1': y0,
                    'x2': x,
                    'y2': y
                }

                # 드래그한 영역 정보 추가
                dragged_areas.append(roi_info)

                save_cropped(img, 'dog.jpg', roi_info)

            else:
                cv2.imshow('img', img)
                print('좌측 상단에서 우측 하단으로 영역을 드래그하세요.')

img = cv2.imread('dog.jpg')
cv2.imshow('img', img)
cv2.setMouseCallback('img', onMouse)

while True:
    key = cv2.waitKey(1)
    if key != -1:  # 아무 키나 누르면 종료
        break

# 작업이 끝난 뒤, 모든 드래그 영역을 JSON 파일로 저장
save_to_json(dragged_areas, 'dog.jpg')

cv2.destroyAllWindows()

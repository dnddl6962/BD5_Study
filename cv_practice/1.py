import cv2
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
import time

image = cv2.imread('cat.jpeg', cv2.IMREAD_COLOR)
cv2.imshow('result', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

img_gray =cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('result_gray', img_gray)
cv2.waitKey(0)
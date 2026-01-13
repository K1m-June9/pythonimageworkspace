import cv2
import numpy as np

#이미지 파일 읽기
image = cv2.imread('img.jpg')

#윈도우 만들기
title1, title2 = '위치1', '위치2'
cv2.namedWindow(title1, cv2.WINDOW_AUTOSIZE)
cv2.namedWindow(title2, cv2.WINDOW_NORMAL)

#윈도우 위치 조정하기
cv2.moveWindow(title1, 350, 450)
cv2.moveWindow(title2, 450, 450)

#이미지 띄우기
cv2.imshow(title1, image)
cv2.imshow(title2, image)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)
import cv2 as cv
import numpy as np

img = cv.imread('img/sunset.jpg')
title = 'mouse event'
x,y,w,h = cv.selectROI(title, img, False)
if w and h:
    roi = img[y:y+h, x:x+w]
    cv.imwrite('./cropped2.jpg', roi)   # ROI 영역만 파일로 저장 ---⑦
    
def onMouse(event, Mx, My, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        img2=cv.imread('cropped2.jpg')
        img[My:My+h,Mx:Mx+w]=img2
        cv.imshow(title,img)


cv.setMouseCallback(title,onMouse)

while True:
    if cv.waitKey(0)&0xFF==27:
        break
cv.destroyAllWindows()
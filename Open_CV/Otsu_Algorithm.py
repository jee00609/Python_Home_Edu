import numpy as np
import cv2
from matplotlib import pyplot as plt


#cv2.imread(fileName, flag) 여기서 flag 값이 -1:alpha 값까지 읽음 / 0: 그레이스케일로 읽음 / 1: 컬러로 읽음
im = cv2.imread('img/scaned_paper.jpg',0)
im_flat = np.reshape(im,(im.shape[0]*im.shape[1]))

[hist, _] = np.histogram(im, bins=256, range=(0, 255))
# 정규화이므로 확률과 같은 값을 갖는다. (sum = 1).
hist = 1.0*hist/np.sum(hist)

val_max = -999
thr = -1
for t in range(1,255):
    # 노가다 (비효율적)
    q1 = np.sum(hist[:t])
    q2 = np.sum(hist[t:])
    m1 = np.sum(np.array([i for i in range(t)])*hist[:t])/q1#RuntimeWarning: invalid value encountered in double_scalars= > 왜지???
    m2 = np.sum(np.array([i for i in range(t,256)])*hist[t:])/q2
    val = q1*(1-q1)*np.power(m1-m2,2)
    if val_max < val:
        val_max = val
        thr = t

print("임계값 : ",thr)

#BRG 바꾸지 않은 사진
img = cv2.imread('img/scaned_paper.jpg')
plt.imshow(img)
plt.show()

#오리지날 사진
plt.imshow(img[:,:,::-1])
plt.show()

#그레이스케일
#cmap='gray' 부분을 써 주어야 matplotlib이 흑백 사진을 제대로 출력 ->출처: https://crmn.tistory.com/50 [크롬망간이 글 쓰는 공간]
plt.imshow(im,cmap='gray')
plt.show()

#cmap='gray' 부분을 써 주어야 matplotlib이 흑백 사진을 제대로 출력 ->출처: https://crmn.tistory.com/50 [크롬망간이 글 쓰는 공간]
plt.imshow(im > thr,cmap='gray')
plt.show()

#https://github.com/jmlipman/LAID/blob/master/IP/Otsu/otsu.py 읽고 이해가지 않는 부분 체크

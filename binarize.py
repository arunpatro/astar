import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('raw.jpg');
rows,cols,ch = img.shape
pts1 = np.float32([[0,150],[1725,178],[39,1303],[1695,1240]])
pts2 = np.float32([[0,0],[1500,0],[0,1000],[1500,1000]])

M = cv2.getPerspectiveTransform(pts1,pts2)
dst = cv2.warpPerspective(img,M,(1500,1000))

gray = cv2.cvtColor(dst,cv2.COLOR_BGR2GRAY)
thres = cv2.threshold(gray,150,255,cv2.THRESH_BINARY)[1]

kernel = np.ones((5,5),np.uint8)
closing = cv2.morphologyEx(thres, cv2.MORPH_CLOSE, kernel,iterations = 10)

# plt.imshow(closing,cmap='gray')
# plt.show()
cv2.imwrite('bin.png',closing)
b = cv2.resize( closing.astype('float'), ( 6, 4 ), interpolation = cv2.INTER_LINEAR )
cv2.imwrite('bin_tiny.png',b)
cv2.imwrite('bin_small.png',0.2*cv2.resize(closing,(0,0),fx=0.1,fy=0.1))


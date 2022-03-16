import cv2 as cv
import numpy as np
from pyrsistent import b 

blank = np.zeros((500, 500, 3), dtype = 'uint8') # blank.shape[0] = 100 (height) _ hàng
                                                 # blank.shape[1] = 500 (width) _ cột
cv.imshow('Blank', blank)

# 1. Paint the image a certain colour (Ve anh mot mau nhat dinh)
# blank[:] = 0, 255, 0 ==> Full green
blank[0:10, 0: 5] = 0, 0, 255 # hàng 0 tới hàng 9, cột 0 tới cột 4 |||| Có thể zoom phần màu đen trong window hiển thị để xem rõ hơn 
cv.imshow('Green', blank)

# 2. Draw a rectangle 
# function rectangle(image, point 1, point 2, color, thickness = None)
# point = (cột, hàng)
cv.rectangle(blank, (0,0), (blank.shape[1]//2,blank.shape[0]//2), (0,255,0), thickness = cv.FILLED) # thickness = 2: ve bien gioi 
                                                                                                    # thickness = cv.FILLED: lap day hinh chu nhat     
cv.imshow('Rectangle', blank)

# 3. Draw a circle
cv.circle(blank, (blank.shape[1]//2,blank.shape[0]//2), 100, (0,0,255), thickness = 3) # radius: ban kinh
                                                                                       # thickness = cv.FILLED hoac thickness = -1 
cv.imshow('Circle', blank)

# 4. Draw a line
cv.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (255,255,255), thickness = 3)
cv.imshow('Line', blank)

# 5. Write Text
cv.putText(blank, 'Hello', (300, 400), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), thickness = 2)
cv.imshow('Text', blank)

cv.waitKey(0)
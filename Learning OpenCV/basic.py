# 5 essential functions in OpenCV

import cv2 as cv 

img = cv.imread('/home/thanh/Pictures/Raspberry.png') # size (width, height): 200 252
cv.imshow('Raspberry logo', img)

# 1. Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray image', gray)

# 2. Blur (lam mo)
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT) # (7,7) is kernel
cv.imshow('Blur', blur)

# 3. Edge Cascade
canny = cv.Canny(img, 125, 175)
cv.imshow('Canny Edge', canny)

# 4. Dilating the image (lam gian anh ra)
dilated = cv.dilate(canny, (3,3), iterations = 1)
cv.imshow('Dilated', dilated)

# 5. Eroding
eroded = cv.erode(dilated, (3, 3), iterations = 1)
cv.imshow('Eroding', eroded)

# 6. Resize
resized = cv.resize(img, (200, 100)) # giu nguyen chieu rong, bop chieu dai 
cv.imshow('Resize', resized)


cv.waitKey(0)

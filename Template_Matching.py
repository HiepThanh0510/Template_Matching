import cv2
import numpy as np


# load image and convert to grayscale
image = cv2.imread('/home/thanh/Pictures/Family.jpg', 1)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

template = cv2.imread('/home/thanh/Pictures/Mom.png', 0)
w, h = template.shape[::-1]

# apply template matching
corr_map = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF_NORMED)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(corr_map)

# take minimum
top_left = max_loc
bottom_right = (top_left[0] + w, top_left[1] + h)

# draw frame
cv2.rectangle(image, top_left, bottom_right, (0, 255, 0), 2)

# save corr map in grayscale 
corr_map = (corr_map + 1.0) * 127.5
corr_map = corr_map.astype('uint8')
cv2.imwrite('/home/thanh/Pictures/corr_map_grayscale.png', corr_map)

# apply color map
corr_map = cv2.applyColorMap(corr_map, cv2.COLORMAP_JET)

# save 
cv2.imwrite('/home/thanh/Pictures/corr_map_color.png', corr_map)
cv2.imwrite('/home/thanh/Pictures/result.png', image)

 

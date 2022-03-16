import cv2 as cv 
# Fuction for Images, Videos and Live Video
def RescaleFrame(frame, scale = 0.5):
    height = int(frame.shape[0] * scale)
    width = int(frame.shape[1] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)

# Function for Live Video
def ChangeRes(width, height):
    capture.set(3, width)
    capture.set(4, height)

#READING VIDEO
capture = cv.VideoCapture('/home/thanh/Videos/Test_video/brain.mp4')

while 1:
    isTrue, frame = capture.read()
    # cv2.resize(src, dsize[, dst[, fx[, fy[, interpolation]]]])
    # src: source/input image
    # dsize: desized (mong muon) size for the output image 
     
    frame_resized = RescaleFrame(frame)
    cv.imshow('Original Video', frame)
    cv.imshow('Scale Video', frame_resized)

    if cv.waitKey(5) & 0xFF == ord('q'): break

capture.realease()
cv.destroyAllWindows()
  


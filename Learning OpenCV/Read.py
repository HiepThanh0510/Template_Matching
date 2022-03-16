import cv2 as cv

# READ IMAGE 
# image = cv.imread('/home/thanh/Pictures/Raspberry.png')
# cv.imshow('Raspberry', image)
# cv.waitKey(0)


# READ VIDEO 
capture = cv.VideoCapture('/home/thanh/Videos/Test_video/test.mp4')

count = 0 

while 1:
    isTrue, frame = capture.read() # return each frame of test.mp4 into frame variable 
                                   # and variable isTrue return 0 or 1, nếu video vẫn còn return frame 
                                   # cho biến frame thì isTrue có giá trị là 1, khi đã quét hết video  
                                   # thì biến isTrue trả về giá trị 0 (tức False)
    
    # Display each frame by cv.imshow()
    cv.imshow('Video', frame)

    # Check switch 'q' 
    # type(cv.waitKey(x)) is 4 bytes ~ 32 bits 
    # Khi chưa type gì cả thì cv.waitKey(x) = -1 (0xFFFFFFFF), 0xFF = 0x000000FF 
    if cv.waitKey(5) & 0xFF == ord('q'):
        break

capture.release()
cv.destroyAllWindows()    


    

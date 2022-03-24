import cv2 as cv
from pyzbar import pyzbar

cap = cv.VideoCapture(0)

while 1:
    ret, frame = cap.read()
    barcodes = pyzbar.decode(frame)
    for barcode in barcodes:
        (x, y, w, h) = barcode.rect
        cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)
        barcodeData = barcode.data.decode("utf-8")
        barcodeType = barcode.type
        text = '{}'.format(barcodeData, barcodeType) # original code '{} - {}'
        #get_text = text[0:6]
        #print(get_text)
        print(text)
        cv.putText(frame, text, (x-10, y-10), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
        
    cv.imshow('Reading QR codes', frame)

    if cv.waitKey(5) & 0xFF == ord('q'): 
        break

cap.release()
cv.destroyAllWindows()

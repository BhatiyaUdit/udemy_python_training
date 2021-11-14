import cv2
import time

video = cv2.VideoCapture(0, cv2.CAP_DSHOW)

a = 0
while True:
    a = a + 1
    check, frame = video.read()
    print(check)
    print(frame)
    cv2.imshow("Capture", frame)
    key = cv2.waitKey(1)
    print(key)
    if key == ord('q'):
        break

print(a)
video.release()
cv2.destroyAllWindows()

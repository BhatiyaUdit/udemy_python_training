import cv2

video = cv2.VideoCapture(0, cv2.CAP_DSHOW)

_, first_frame = video.read()
cv2.imshow("First Frame", first_frame)
first_frame = cv2.cvtColor(first_frame, cv2.COLOR_RGB2GRAY)
first_frame = cv2.GaussianBlur(first_frame, (21, 21), 0)

# face_detector_xml = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
# print(face_detector_xml)

while True:
    check, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    cv2.imshow("Color Frame", frame)
    cv2.imshow("Gray Frame", gray)
    # faces_in_image = face_detector_xml.detectMultiScale(gray, scaleFactor=1.08, minNeighbors=6)

    # for face in faces_in_image:
    #     print(face)
    #     start_x, start_y, width, height = face
    #     line_Color = (0, 255, 0)  # RGB format
    #     line_width = 2
    #     image = cv2.rectangle(frame, (start_x, start_y), (start_x + width, start_y + height), line_Color, line_width)
    #
    # cv2.imshow("Color Outline Frame", image)

    blurred_frame = cv2.GaussianBlur(gray, (21, 21), 0)
    cv2.imshow("Blurred Frame", blurred_frame)
    delta = cv2.absdiff(first_frame, blurred_frame)
    cv2.imshow("Delta Frame", delta)

    threshold_frame = cv2.threshold(delta, 30, 255, cv2.THRESH_BINARY)
    cv2.imshow("Threshold Frame", threshold_frame[1])

    contours, _ = cv2.findContours(threshold_frame[1].copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    print("Contours -->", contours)
    print("__", _)

    for contour in contours:
        if cv2.contourArea(contour) < 10000:
            continue
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
    cv2.imshow("Color Outline Frame", frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

video.release()
cv2.destroyAllWindows()

# #
#       1)  To Store First Frame use a different variable initialize with None and
#           Do not over write that variable
#       2)  Once we have first frame we need to calculate Delta Frame in Second
#           Iteration (Difference between base frame and second frame)
#           Before that apply Gaussian Blur to the gray image to reduce noise and increase accuracy
#           (21,21) tuple , 0 standard deviation (GO TO Documentation for Gaussian Blurring)
#           Calculate delta using absdiff method of CV2
#       3)  After that we need to create a threshold frame that will display a black and white frome
#           where if the threshold is matched then white is displayed else black  cv2.threshold
#       4)  Now for the Contours we need to find the contours in threshold frame where white and black starts and ends
#           To find the contours use method findContours# ---  write all the steps after study
# #

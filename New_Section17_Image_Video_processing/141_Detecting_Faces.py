import cv2

face_detector_xml = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
print(face_detector_xml)

image = cv2.imread("./images/2.jpg")
print(image.shape)
# convert image to gray color as Gray images are better suited for face recoginition

image_gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

# Scale Factor below is the factor with which
# python will decrease the image size 1.05 - 5% and then re-search for the faces
# lower the number higher the accuracy but more time consuming
# very low number can decrease the accuracy

faces_in_image = face_detector_xml.detectMultiScale(image_gray,
                                                    scaleFactor=1.08,
                                                    minNeighbors=6
                                                    )

print(faces_in_image)

for face in faces_in_image:
    print(face)
    start_x, start_y, width, height = face
    line_Color = (0, 255, 0)  # RGB format
    line_width = 2
    image = cv2.rectangle(image, (start_x, start_y), (start_x + width, start_y + height), line_Color, line_width)

# resizing image
image_height = image.shape[0]
image_width = image.shape[1]

new_height = int(image_height / 2)
new_width = int(image_width / 2)
image = cv2.resize(image, (new_width, new_height))

cv2.imshow("gray", image_gray)
cv2.imshow("grat", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("./images/faces2.jpg", image)

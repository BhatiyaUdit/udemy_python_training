import cv2

image = cv2.imread('./images/galaxy.jpg', 0)
print(type(image))
print(image)

print(image.shape)
print(image.ndim)

cv2.imshow("wind", image)

resizedimg = cv2.resize(image, (500,500))

# resizing based on current dimensions image.shape[1]/2 --> must be integer

cv2.imshow("resized", resizedimg)
cv2.waitKey(0)
cv2.destroyAllWindows()


cv2.imwrite("resized/resized.jpg", resizedimg)

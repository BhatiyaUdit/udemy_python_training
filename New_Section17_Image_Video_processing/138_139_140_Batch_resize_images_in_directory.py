import cv2
import glob

# from os import walk
#
# x = walk("./images")
# print(x.__dir__())
# f = []
# for (dirpath, dirnames, filenames) in walk("./images"):
#     print(filenames)
#     f.extend(filenames)
#     break


print(glob.glob("./images/*.jpg"))

image_list = glob.glob("./images/*.jpg")
for image_name in image_list:
    print(image_name)
    image = cv2.imread(image_name, 0)
    print(image.shape)
    resized_image = cv2.resize(image, (100, 100))
    cv2.imwrite("./resized/" + image_name + "_resized.jpg", resized_image)

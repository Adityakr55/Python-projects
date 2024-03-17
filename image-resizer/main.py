import cv2

# Configurable Parameters
source = "Aditya.jpeg"
destination = "newImage.png"
scale_percent = int(input("Enter the desired scale percentage: "))

image = cv2.imread(source, cv2.IMREAD_UNCHANGED)
cv2.imshow("title",image)


new_width = int(image.shape[1] * scale_percent / 100)
new_height = int(image.shape[0] * scale_percent / 100)

output = cv2.resize(image, (new_width, new_height))
cv2.imwrite(destination, output)
cv2.waitKey(0)
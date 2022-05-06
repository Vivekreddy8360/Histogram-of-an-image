# Developed By: Koduru Sanath Kumar Reddy
# Register Number: 212221240024.
import cv2
import matplotlib.pyplot as plt

# Write your code to find the histogram of gray scale image and color image channels.

gray_image=cv2.imread('grayscaleimage.jpeg')
hist=cv2.calcHist([gray_image],[0],None,[256],[0,256])
plt.imshow(gray_image)
plt.show()
plt.figure()
plt.title("histogram")
plt.xlabel('grayscale value')
plt.ylabel('pixel count')
plt.stem(hist)
plt.show()





# Display the histogram of gray scale image and any one channel histogram from color image

color_image=cv2.imread('car.jpeg')
hist=cv2.calcHist([color_image],[0],None,[256],[0,256])
plt.imshow(color_image)
plt.show()
plt.figure()
plt.title("histogram")
plt.xlabel('colorscale value')
plt.ylabel('pixel count')
plt.stem(hist)
plt.show()





# Write the code to perform histogram equalization of the image.

gray_image = cv2.imread('gray.jpg',0)
equ=cv2.equalizeHist(gray_image)
cv2.imshow('Gray image',gray_image)
cv2.imshow('Equalized Image',equ)
cv2.waitKey(0)
cv2.destroyAllWindows()








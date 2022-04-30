# Histogram and Histogram Equalization of an image
## Aim
To obtain a histogram for finding the frequency of pixels in an Image with pixel values ranging from 0 to 255. Also write the code using OpenCV to perform histogram equalization.

## Software Required:
Anaconda - Python 3.7

## Algorithm:
Step1: Import the necessary libraries and read two images, Color image and Gray Scale image

Step2: Calculate the Histogram of Gray scale image and each channel of the color image.

Step3: Display the histograms with their respective images.

Step4: Equalize the grayscale image.

Step5: Display the grayscale image.

## Program:
```python
# Developed By:m.vivek reddy
# Register Number:212221240030
import cv2
import matplotlib.pyplot as plt

## Write your code to find the histogram of gray scale image and color image channels.
gray_image = cv2.imread("butterfly.jpg")
plt.imshow(gray_image)
plt.show()
hist=cv2.calcHist([gray_image],[0],None,[256],[0,256])
plt.figure()
plt.title("Histogram")
plt.xlabel('Grayscale value')
plt.ylabel('Pixel Count')
plt.stem(hist)
plt.show()




# Display the histogram of gray scale image and any one channel histogram from color image
color_image=cv2.imread("venice.jpg")
plt.imshow(color_image)
plt.show()
hist1=cv2.calcHist([color_image],[1],None,[256],[0,256])
plt.figure()
plt.title("Histogram")
plt.xlabel("Intensity Value")
plt.ylabel("Pixel Count")
plt.stem(hist1)
plt.show()




# Write the code to perform histogram equalization of the image. 
gray_image = cv2.imread('butterfly.jpg',0)
equ=cv2.equalizeHist(gray_image)
cv2.imshow('Gray image',gray_image)
cv2.imshow('Equalized Image',equ)
cv2.waitKey(0)
cv2.destroyAllWindows()







```
## Output:
### Input Grayscale Image and Color Image
![1](https://user-images.githubusercontent.com/94525701/166115572-865a6d0d-9c88-4e49-b2b9-005cb7f97835.png)
### Histogram of Grayscale Image and any channel of Color Image
![2](https://user-images.githubusercontent.com/94525701/166115575-f820aaf1-ad8a-4fac-b27e-bd572b60dd1b.png)
### Histogram Equalization of Grayscale Image
![3](https://user-images.githubusercontent.com/94525701/166115583-a9401534-f06f-483f-8f66-b27cb3181681.png)

## Result: 
Thus the histogram for finding the frequency of pixels in an image with pixel values ranging from 0 to 255 is obtained. Also,histogram equalization is done for the gray scale image using OpenCV.

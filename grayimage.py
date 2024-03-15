import cv2 
  
# Load the input image 
image = cv2.imread('image1.jpg') 
  
# Use the cvtColor() function to grayscale the image 
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 

gray_image.save("gray.jpg")

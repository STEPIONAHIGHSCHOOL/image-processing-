#python libraries
import cv2​
import numpy as np
import matplotlib.pyplot as plt​

# Load the image​
image = cv2.imread("bird.jpg")  # replace with any image, e.g., "dog.jpg"​
print(image.shape) # Output: height, width, 3)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)​

# Apply effects for guessing game​
gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)   # grayscale​ (black and white)
blur = cv2.GaussianBlur(image, (25, 25), 0)   # blurred​ (softens the image)
edges = cv2.Canny(gray, 100, 200)  # edges​

# Display results​
titles = ["Original", "Grayscale", "Blurred", "Edges"]​
images = [image, gray, blur, edges]​
plt.figure(figsize=(10, 8))​

# Display all images in 2x2 grid
for i in range(4):​
 plt.subplot(2, 2, i + 1) #create a subplot(2 rows, 2 columns)​
 if titles[i] in ["Grayscale", "Edges"]:​
  plt.imshow(images[i], cmap='gray') ​# display grayscale image or edge images in gray
 else:​
    plt.imshow(image[i]) # display color images in RGB​
  plt.title(titles[i]) #​ Set the title for each subplot 
  plt.axis("off") # hide the axis for cleaner display​
plt.tight_layout( ) # adjust spacing between images​
plt.show( )

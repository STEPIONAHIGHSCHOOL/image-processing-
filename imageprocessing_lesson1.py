# Python Libraries
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread("cat.png")  # Replace with your image file

# Check if image loaded successfully

print("Image Shape:", image.shape)  # Height, Width, Channels

# Convert BGR to RGB
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Apply effects for guessing game
gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)      # Grayscale
blur = cv2.GaussianBlur(image, (25, 25), 0)         # Blurred
edges = cv2.Canny(gray, 100, 200)                   # Edge Detection

# Display results
titles = ["Original", "Grayscale", "Blurred", "Edges"]
images = [image, gray, blur, edges]
plt.figure(figsize=(10, 8))

# Display all images in a 2x2 grid
for i in range(4):
        plt.subplot(2, 2, i + 1)

        if titles[i] in ["Grayscale", "Edges"]:
            plt.imshow(images[i], cmap="gray")
        else:
            plt.imshow(images[i])

        plt.title(titles[i])
        plt.axis("off")

plt.tight_layout()
plt.show()

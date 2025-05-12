import cv2
import numpy as np

# Create a simple test image - a colorful gradient
def create_test_image(filename="test_image.jpg"):
    # Create a 600x600 RGB image
    img = np.zeros((600, 600, 3), dtype=np.uint8)
    
    # Create gradient effect
    for i in range(600):
        for j in range(600):
            img[i, j, 0] = i % 256  # Blue channel
            img[i, j, 1] = j % 256  # Green channel
            img[i, j, 2] = (i + j) % 256  # Red channel
    
    # Add some shapes
    cv2.circle(img, (300, 300), 100, (255, 0, 0), -1)  # Blue circle
    cv2.rectangle(img, (100, 100), (200, 200), (0, 255, 0), -1)  # Green rectangle
    cv2.line(img, (400, 100), (500, 500), (0, 0, 255), 5)  # Red line
    
    # Save the image
    cv2.imwrite(filename, img)
    print(f"Test image created and saved as {filename}")
    return filename

if __name__ == "__main__":
    create_test_image()

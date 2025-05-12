import cv2
import numpy as np

def color_quantization(img, k=8):
    """
    Reduces the number of colors in the image using k-means clustering.
    """
    data = np.float32(img).reshape((-1, 3))
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 20, 0.001)
    _, labels, centers = cv2.kmeans(data, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    centers = np.uint8(centers)
    quantized = centers[labels.flatten()]
    quantized_img = quantized.reshape(img.shape)
    return quantized_img


def cartoonize_image(img_path):
    """
    Converts a real-life image into a cartoon-style image using OpenCV with improved cartoon effect.
    """
    # Load the image
    img = cv2.imread(img_path)
    if img is None:
        raise ValueError(f"Could not load image from {img_path}")
    img = cv2.resize(img, (600, 600))

    # 1. Color Quantization (reduce number of colors)
    quantized = color_quantization(img, k=8)

    # 2. Edge Detection with Bolder Outlines
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray_blur = cv2.medianBlur(gray, 7)
    edges = cv2.adaptiveThreshold(
        gray_blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 2
    )
    # Make edges bolder
    kernel = np.ones((3, 3), np.uint8)
    edges = cv2.dilate(edges, kernel, iterations=1)

    # 3. Smoothing (strong bilateral filter)
    smooth = cv2.bilateralFilter(quantized, d=9, sigmaColor=200, sigmaSpace=200)

    # 4. Combine quantized colors with bold edges
    cartoon = cv2.bitwise_and(smooth, smooth, mask=edges)

    # Display the images
    cv2.imshow("Original", img)
    cv2.imshow("Cartoon", cartoon)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Save the cartoon image
    cv2.imwrite("cartoon_output.jpg", cartoon)
    return cartoon

if __name__ == "__main__":
    cartoonize_image("best_sample.jpg")

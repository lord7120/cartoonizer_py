# Cartoonizer

A Python application that converts real-life images into cartoon-style images using OpenCV.

## Features

- Resizes images to a consistent size (600x600)
- Applies edge detection and color smoothing
- Displays both original and cartoonized images
- Saves the cartoon output as "cartoon_output.jpg"

## Requirements

- Python 3.x
- OpenCV library

## Installation

1. Clone or download this repository
2. Install the required dependency:

```
pip install opencv-python
```

## Usage

1. Place an image you want to cartoonize in the same directory as the script
2. Edit the script to point to your image:

```python
if __name__ == "__main__":
    cartoonize_image("your_image.jpg")  # Replace with your image path
```

3. Run the script:

```
python cartoonizer.py
```

4. The application will display both the original and cartoonized images and save the output as "cartoon_output.jpg"

## How It Works

The cartoonization process involves:
1. Converting the image to grayscale
2. Applying median blur to reduce noise
3. Using adaptive thresholding to detect edges
4. Applying bilateral filtering to smooth colors while preserving edges
5. Combining the filtered image with the detected edges

## Example

Input: Regular photograph
Output: Cartoon-style image with defined edges and smoothed colors

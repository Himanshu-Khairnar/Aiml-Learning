# Image Processing and Conversion

This project demonstrates fundamental image processing techniques using Python. It explores how digital images are represented as arrays and applies various transformations.

## Features

- **Channel Extraction**: Separating Red, Green, and Blue channels.
- **Grayscale Conversion**: Converting color images to grayscale using the formula $0.299R + 0.587G + 0.114B$.
- **Image Transformations**:
  - Creating negative images.
  - Converting to binary (black and white) images.
  - Cropping specific regions of an image.
- **Visualization**: Displaying original and processed images side-by-side.

## Observations

- **Color Channels**: Separating channels visualizes the intensity of Red, Green, and Blue components individually.
- **Grayscale Efficiency**: The weighted average method for grayscale conversion effectively retains the perceptual luminance of the original image.
- **Structural Highlights**: Binary thresholding and negative inversions effectively isolate high-contrast features, which is useful for edge detection or object segmentation.

## Technologies Used

- **Python**
- **Matplotlib**: For reading and displaying images.
- **NumPy**: For array manipulations and image processing algorithm.

## Files

- `ImageConvertor.ipynb`: Code for image processing.
- `Askelad.webp`: Sample image used for demonstration.

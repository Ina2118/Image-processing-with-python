# Image-processing-with-python
The project is a coursework on image processing with Python. It includes various techniques such as filtering, segmentation, noise removal, edge and contour detection. OpenCV and NumPy are used.
## Description

1.**Gaussian Blur** – Gaussian blur is an image processing technique that uses a mathematical function to smooth and blur an image, reducing image noise and detail by averaging pixels based on their proximity.

2. **Thresholding** – Thresholding is the simplest method of segmenting images. From a grayscale image, thresholding can be used to create binary images.

3. **Erosion & Dilation** – Erosion in image processing is a morphological operation that shrinks and thins the boundaries of objects in an image by removing pixels on object edges, effectively making objects smaller and removing small white noise. Dilation is a morphological operation that expands the boundaries of objects in an image by adding pixels to object edges making objects appear larger and filling in small gaps or holes.

4. **Edge Detection** – Edge detection is a technique used to identify the boundaries of objects within images. It helps in simplifying the image data by reducing the amount of information to be processed while preserving the structural properties of the image. This simplification is essential for various image analysis tasks, including object recognition, segmentation, and image enhancement.
   
6. **Contour Detection** – Contour detection extracts and visualizes the outlines of objects in an image. It is useful for shape analysis, object detection, and measuring properties like area or perimeter.
   
8. **Segmentation Remove Noise** – This module removes noise from images to improve the quality of segmentation. It helps generate cleaner masks and more accurate object boundaries.

## Installation
1. Make sure you have **Python 3.x** installed. You can download it from [python.org](https://www.python.org/).
2. Install the required libraries:
   
**OpenCV (opencv-python)**  
OpenCV is a powerful library for computer vision and image processing. It provides functions for:
- Reading and writing images and videos
- Image filtering and blurring (e.g., Gaussian Blur)
- Morphological operations (erosion, dilation)
- Edge detection (Canny)
- Contour detection and analysis
- Image segmentation (watershed, thresholding)

**NumPy**  
NumPy is a fundamental library for numerical computing in Python. It provides:
- Efficient multi-dimensional array handling
- Mathematical operations on arrays
- Image manipulation in combination with OpenCV

**Matplotlib**  
Matplotlib is a plotting library used for data visualization. In this project, it is used to:
- Display images in a notebook or window
- Compare original and processed images side by side
- Visualize results such as edge detection or segmentation masks
     
3. Install the libraries using `pip`:

```bash
pip install numpy
pip install opencv-python
pip install matplotlib
```

## Usage

Before running any script, you need to specify the path to your input image.  
For example:

```python
path = r'C:\Users\User\Desktop\irina\TI\segmentation\yes\segmentation\9.png'
img = cv2.imread(path)
```
**path** should point to the location of your **input image** on your computer.
Make sure to use **raw string (r'')** or **double backslashes (\\)** in Windows paths to avoid errors.
After setting the **path**, you can run the **script**

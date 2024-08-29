# FaceDetection and Filtering Project using OpenCV
## Overview
This project is a collection of Python scripts that utilize OpenCV for real-time face detection, image processing, and applying custom filters to video frames captured from a webcam. The scripts cover various functionalities such as face detection, background removal, overlaying custom images on detected faces, and applying Snapchat-like filters.


## Project Structure
The project contains the following Python scripts:

face_detection.py
trackface.py
rembg.py
overlayfilter.py
blurface.py
Each of these scripts serves a specific purpose in the overall project. Below is a description of each script:

### 1. DetectFace.py
This script performs real-time face detection using the Haar Cascade classifier provided by OpenCV. It captures video from the default webcam, detects faces in each frame, and draws a rectangle around them. The detection works on grayscale images, and the rectangles are drawn on the original color frames.


### 2. trackface.py
This script is similar to face_detection.py but emphasizes the ability to track faces across frames. The primary functionality is to detect faces and maintain focus on them across video frames.


### 3. rembg.py
This script is designed to remove the background from an image, particularly where the background is predominantly white. It creates a negative of the image, converts it to grayscale, and then applies a binary threshold to isolate the foreground from the background. The result is saved as a new image with an alpha channel to represent transparency.


### 4. overlayfilter.py
This script applies a custom filter, akin to a Snapchat filter, over detected faces in real-time. It detects faces and overlays a custom image (e.g., an apple) on the detected face, centering it appropriately. The overlay is blended with the original frame to create a seamless effect.


### 5. blurface.py
Similar to overlayfilter.py, this script detects faces and applies a filter to them. However, this filter is more focused on manipulating the appearance of the face, such as blurring or overlaying specific images to achieve a desired effect. This script could be extended to include a "magic eraser" feature to remove extra, smaller faces in a frame.


## How to Run the Scripts
- Ensure you have Python installed (preferably Python 3.7+).
- Install OpenCV if not already installed:
- pip install opencv-python
- Download or clone the project folder.
- Place the required images (e.g., apple.png) in the specified paths in the scripts or update the paths as needed.
- Run each script using Python:
- python face_detection.py
- Replace face_detection.py with the script name you wish to run.


## Notes
These scripts are designed for experimentation and demonstration purposes. They can be expanded and modified to include more complex filters, detection algorithms, or integration with other libraries.
Make sure to have the correct paths for any images used in overlayfilter.py and blurface.py.
License
This project is open-source and free to use. You are encouraged to modify, distribute, and improve upon the code.

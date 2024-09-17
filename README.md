# Image Editor

This is a comprehensive Python package designed to simplify and streamline image editing tasks. While currently focused on image cropping, it is built with extensibility in mind, allowing for future additions of various image manipulation features.

## Description:

This is a comprehensive Python package designed to simplify and streamline image editing tasks. While currently focused on image cropping, it is built with extensibility in mind, allowing for future additions of various image manipulation features.

Key features of the current version include:
- Aspect Ratio-Based Cropping: The package offers a powerful crop_image function that allows users to crop images to specific aspect ratios, maintaining the image's height while adjusting the width accordingly.
- Flexible Aspect Ratio Handling: Utilizes an AspectRatio enum for easy specification of common aspect ratios, making it simple to crop images to standard dimensions.
- Precise Dimension Calculation: Includes a closest_resolution_by_height function that calculates the optimal dimensions based on the desired aspect ratio and the original image height.
- Comprehensive Logging: Incorporates detailed logging at various levels (INFO, DEBUG, ERROR) to provide insights into the cropping process, facilitating easier debugging and monitoring.
- Error Handling: Robust error handling for common issues such as file I/O errors and unexpected exceptions during the cropping process.
- PIL Integration: Built on top of the Python Imaging Library (PIL), ensuring high-quality image processing and compatibility with a wide range of image formats.

The package is designed with both ease of use and performance in mind, making it suitable for both small-scale projects and larger applications requiring batch image processing. Its modular structure and use of logging make it easy to extend with additional image editing features in the future, such as resizing, filtering, or format conversion.

Whether you're a developer working on a photography application, a data scientist preparing images for machine learning models, or simply need to process a large number of images, image_utils provides a solid foundation for your image editing needs.

## How to install:

Run the following command in your python venv:

```bash
pip install git+https://github.com/avivilloz/image_utils.git@main#egg=image_utils
```

Or add the following line to your project's `requirement.txt` file:

```
git+https://github.com/avivilloz/image_utils.git@main#egg=image_utils
```

And run the following command:

```bash
pip install -r requirements.txt
```

## How to use:

```python
from image_utils import *

# Use image editor functions
```
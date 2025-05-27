# broccoli vision OpenCV using oak-d camera
## Overview

This project demonstrates how to use an OAK-D camera with OpenCV for real-time computer vision applications. The OAK-D camera provides depth and AI capabilities, making it suitable for a variety of vision-based tasks.

## Features

- Real-time video capture using OAK-D
- Depth estimation and visualization
- Integration with OpenCV for image processing
- Example scripts for common vision tasks

## Requirements

- OAK-D camera
- Python 3.7+
- [DepthAI](https://github.com/luxonis/depthai) library
- OpenCV (`opencv-python`)

## Getting Started

1. Clone this repository.
2. Install the required Python packages:
    ```bash
    pip install depthai opencv-python
    ```
3. Connect your OAK-D camera.
4. Run the example script:
    ```bash
    python main.py
    ```

## Example Usage

```python
import cv2
import depthai as dai

# Initialize pipeline and camera
pipeline = dai.Pipeline()
# ... pipeline setup code ...

# Start pipeline and capture frames
with dai.Device(pipeline) as device:
     # ... frame capture and processing code ...
```

## Resources

- [OAK-D Documentation](https://docs.luxonis.com/)
- [OpenCV Documentation](https://docs.opencv.org/)

## License

This project is licensed under the MIT License.

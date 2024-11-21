# Human Detection from Camera

This repository contains code example of human detection with camera on machines capable of running Python. The code utilizes OpenCV module for object detection with the SVM (support vector machine) technique.

The recommended way to test this code is with Python's virtual environment feature. On Debian and derivatives, they require `python3-venv` to be installed (if you're on another distro, check the corresponding package manager to find the right package name). On Windows and macOS, it comes with regular installation of Python.

- Clone this repo.
- Create a virtual environment folder for your projects and activate it. For example to create `env` folder run `python3 -m venv env`. Activate it with `source env/bin/activate` (for UNIX-like systems like Linux or macOS) or `.\env\Scripts\activate.bat` if you`re on Windows.
- Change directory to the cloned repo (`./human-detection-from-camera`).
- Install the requirements with `pip install -r requirements.txt`.
- Run the code with `python main.py`

## Optimizing the Code

You can try to optimize the detection with changing the value inside the tuple of `winStride` and `padding` with any positive integer.

# Prostate Segmentation MoE [![psmoe](https://img.shields.io/pypi/v/psmoe)](https://pypi.org/project/psmoe/)

A simple Python module for easy segmentation of the prostate in T2-weighted MRI images in NIfTI format. This module utilizes a mixture of U-Net architectures for segmentation tasks and aims to provide a straightforward solution for users working with prostate MRI data.


## Features

- Segmentation of prostate regions in T2-weighted MRI images.
- Uses a combination of trained U-Net models for accurate and efficient segmentation.
- Supports input in the NIfTI format, a common format for medical imaging.
- Returns 3D masks aswell as the volume estimation.

## Recommended before installation (Windows)

### Install virtualenv if not already
```pip install virtualenv```
### Create a virtual environment
```python -m venv venv```
### Activate it
```venv\Scripts\activate```
- You may need to run ```Set-ExecutionPolicy Unrestricted -Scope Process``` before activation

## Recommended before installation (Linux)

### Install virtualenv if not already
```pip install virtualenv```
### Create a virtual environment
```python -m venv venv```
### Activate it
```source venv/bin/activate```

If creating your own repository don't forget to ignore the `venv` folder in the `.gitignore` file


## Installation
- Upgrade pip if not already

```pip install --upgrade pip```

- Install the library using pip:

```pip install psmoe``` for last version

## Usage
### Example
Check for `example.py` 

## License
This project is licensed under the MIT License - see the LICENSE file for details.


For more details, visit the [GitHub repository](https://github.com/mpierangeli/prostate_segmentation_moe).


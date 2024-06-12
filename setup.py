from setuptools import setup, find_packages

setup(
    name='car-security-system',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'opencv-python',
        'pytesseract',
        'picamera',
        'RPi.GPIO',
    ],
)

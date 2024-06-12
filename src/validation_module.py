import pytesseract
import cv2

def validate_license(image_path='images/sample_driver_license.jpg'):
    img = cv2.imread(image_path)
    text = pytesseract.image_to_string(img)
    return "VALID_LICENSE_NUMBER" in text
